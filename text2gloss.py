import pickle
import torch
from transformers import *
import re


class Settings:
    model = "text2gloss/text2gloss.model"
    data_pkl = "text2gloss/text2gloss_data.pkl"
    beam_size = 5
    max_seq_len = 100


opt = Settings()
data = pickle.load(open(opt.data_pkl, "rb"))
SRC, TRG = data["vocab"]["src"], data["vocab"]["trg"]
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
unk_idx = SRC.vocab.stoi[SRC.unk_token]

opt.src_pad_idx = SRC.vocab.stoi[Constants.PAD_WORD]
opt.trg_pad_idx = TRG.vocab.stoi[Constants.PAD_WORD]
opt.trg_bos_idx = TRG.vocab.stoi[Constants.BOS_WORD]
opt.trg_eos_idx = TRG.vocab.stoi[Constants.EOS_WORD]


def load_model(device):

    checkpoint = torch.load(opt.model, map_location=device)
    model_opt = checkpoint["settings"]

    model = Transformer(
        model_opt.src_vocab_size,
        model_opt.trg_vocab_size,
        model_opt.src_pad_idx,
        model_opt.trg_pad_idx,
        trg_emb_prj_weight_sharing=model_opt.proj_share_weight,
        emb_src_trg_weight_sharing=model_opt.embs_share_weight,
        d_k=model_opt.d_k,
        d_v=model_opt.d_v,
        d_model=model_opt.d_model,
        d_word_vec=model_opt.d_word_vec,
        d_inner=model_opt.d_inner_hid,
        n_layers=model_opt.n_layers,
        n_head=model_opt.n_head,
        dropout=model_opt.dropout,
    ).to(device)

    model.load_state_dict(checkpoint["model"])
    return model


TRANSLATOR = Translator(
    model=load_model(device),
    beam_size=opt.beam_size,
    max_seq_len=opt.max_seq_len,
    src_pad_idx=opt.src_pad_idx,
    trg_pad_idx=opt.trg_pad_idx,
    trg_bos_idx=opt.trg_bos_idx,
    trg_eos_idx=opt.trg_eos_idx,
).to(device)


def translate(text: str) -> str:
    spoken = text.lower().strip().split()

    if all(c.isdigit() for c in spoken):
        return text

    spoken.append(".")

    src_seq = [SRC.vocab.stoi.get(word, unk_idx) for word in spoken]
    pred_seq = TRANSLATOR.translate_sentence(torch.LongTensor([src_seq]).to(device))
    pred_seq = set(pred_seq)
    pred_line = " ".join(TRG.vocab.itos[idx] for idx in pred_seq)
    pred_line = (
        pred_line.replace(Constants.BOS_WORD, "")
        .replace(Constants.EOS_WORD, "")
        .replace(Constants.PAD_WORD, "")
        .replace(Constants.UNK_WORD, "")
    )

    final = str(pred_line.strip())

    if not contains_alpha_or_digits(final):
        return text.lower().strip()

    final = remove_special_characters(final.strip())

    for k in common_words:
        v = common_words[k]
        if k in spoken and v not in final.split():
            final = v + " " + final

    print(final)
    return final


def contains_alpha_or_digits(s: str) -> bool:
    contains_alpha = any(c.isalpha() for c in s)
    contains_digits = any(c.isdigit() for c in s)
    return any([contains_alpha, contains_digits])


def remove_special_characters(input_string):
    pattern = re.compile(r"[^a-zA-Z0-9\s]")
    clean_string = re.sub(pattern, "", input_string)
    clean_string = re.sub(r'\s+', ' ', clean_string)
    return clean_string.strip()


common_words = {
    "eat": "eat",
    "we": "we",
    "she": "she",
    "he": "he",
    "i": "me",
}
