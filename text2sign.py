import mxnet as mx
from sockeye import inference, model
import sentencepiece as spm


DEVICE = mx.cpu()
MODEL_FOLDER = "text2sign"
SPM_PATH = MODEL_FOLDER + "/spm.model"


MODELS, SRC_VOCABS, TARG_VOCABS = model.load_models(
    context=DEVICE, dtype=None, model_folders=[MODEL_FOLDER], inference_only=True)
SPM_MODEL = spm.SentencePieceProcessor(model_file=SPM_PATH)


LANG_CODE = "en"
CONT_CODE = "ase"  # "us"
TRANS_TYPE = "sent"
N_BEST = 3
BEAM_SIZE = N_BEST

TRANSLATOR = inference.Translator(
	context=DEVICE,
	ensemble_mode="linear",
	scorer=inference.CandidateScorer(),
	output_scores=True,
	batch_size=1,
	beam_size=BEAM_SIZE,
	beam_search_stop="all",
	nbest_size=N_BEST,
	models=MODELS,
	source_vocabs=SRC_VOCABS,
	target_vocabs=TARG_VOCABS,
)


def translate(text):
    print(text)

    tag_str = f"<2{LANG_CODE}> <4{CONT_CODE}> <{TRANS_TYPE}>"
    formatted = f"{tag_str} {text}"

    encoded = " ".join(SPM_MODEL.encode(formatted, out_type=str))
    print(encoded)

    encoded = inference.make_input_from_plain_string(0, encoded)
    print(encoded)
    
    output = TRANSLATOR.translate([encoded])[0]
    print(output)

    # translations = []
    symbols_candidates = output.nbest_translations
    factors_candidates = output.nbest_factor_translations
    for symbols, factors in zip(symbols_candidates, factors_candidates):
        symbols = symbols.split(" ")
        xs = factors[0].split(" ")
        ys = factors[1].split(" ")
        fsw = ""

        for i, (symbol, x, y) in enumerate(zip(symbols, xs, ys)):
            if symbol != "P":
                if i != 0:
                    if (
                        not symbol.startswith("S")
                        or symbol.startswith("S387")
                        or symbol.startswith("S388")
                        or symbol.startswith("S389")
                        or symbol.startswith("S38a")
                        or symbol.startswith("S38b")
                    ):
                        fsw += " "
                fsw += symbol
                fsw += x
                fsw += "x"
                fsw += y

        # translations.append(fsw)
        print(fsw)
        return fsw

    # return translations
