import warnings
from bottle import route, run, request, response
from time import time
import uuid
import os
import spacy
import socket
import sign2img
from pose_format.pose_visualizer import PoseVisualizer
import gloss2pose

POSE_LOOKUP = gloss2pose.PoseLookup("lexicon", "asl")
warnings.filterwarnings("ignore")

try:
    import text2sign
except Exception as e:
    print("text2sign", e)


############ for pickle ############

try:
    class PreSettings:
        lang_src = "en"
        lang_trg = "en"
        save_data = "text2gloss_data.pkl"

        data_src = None
        data_trg = None

        max_len = 100
        min_word_count = 3

        keep_case = False
        share_vocab = True

    preOpt = PreSettings()
    src_lang_model = spacy.load(preOpt.lang_src)
    trg_lang_model = spacy.load(preOpt.lang_trg)

    STOP_WORDS = ['X-', 'DESC-']
    MAX_LEN = preOpt.max_len
    MIN_FREQ = preOpt.min_word_count

    def tokenize_src(text):
        for w in STOP_WORDS:
            text = text.replace(w, '')
        return [tok.text for tok in src_lang_model.tokenizer(text)]

    def tokenize_trg(text):
        for w in STOP_WORDS:
            text = text.replace(w, '')
        return [tok.text for tok in trg_lang_model.tokenizer(text)]

    def filter_examples_with_length(x):
        return len(vars(x)['src']) <= MAX_LEN and len(vars(x)['trg']) <= MAX_LEN
except Exception as e:
    print("text2gloss", e)

try:
    import text2gloss
except Exception as e:
    print("text2gloss", e)

####################


@route("/text2sign")
def translate_text():
    text = request.query.get("text", None)
    if not text:
        response.status = 400
        return {"error": "No text provided"}

    try:
        start = time()
        symbol = text2sign.translate(text)
        return {"sign": symbol, "time-taken": time() - start}
    except Exception as e:
        response.status = 404
        return {"error": str(e)}


@route("/sign2img")
def convert_text():
    sign = request.query.get("sign", None)
    line_color = request.query.get("line_color", None)
    if line_color:
        line_color = tuple([int(x) for x in line_color.split(",")])

    if not sign:
        response.status = 400
        return {"error": "No sign provided"}

    try:
        img = sign2img.convert(sign, line_color)
        response.content_type = 'image/png'
        return img
    except Exception as e:
        response.status = 404
        return {"error": str(e)}


@route("/text2gloss")
def translate_gloss():
    text = request.query.get("text", None)
    if not text:
        response.status = 400
        return {"error": "No text provided"}

    try:
        start = time()
        gloss = text2gloss.translate(text)
        return {"gloss": gloss, "time-taken": time() - start}
    except Exception as e:
        response.status = 404
        return {"error": str(e)}


@route("/gloss2pose")
def make_pose():
    gloss = request.query.get("gloss", None)
    if not gloss:
        response.status = 400
        return {"error": "No gloss provided"}

    try:
        start = time()
        glosses = gloss2pose.prepare_glosses(gloss)
        print(glosses)

        if not glosses:
            response.status = 404
            return {"error": "No gloss found"}

        pose, words = POSE_LOOKUP.gloss_to_pose(glosses)
        if not pose:
            response.status = 404
            return {"error": "No pose found"}

        gloss2pose.scale_down(pose, 512)
        p = PoseVisualizer(pose, thickness=2)

        unqid = str(uuid.uuid4()) + ".png"
        p.save_png(unqid, p.draw(transparency=True))

        with open(unqid, "rb") as f:
            img = f.read()
        os.remove(unqid)

        return {"img": img, "words": words, "time-taken": time() - start}
    except Exception as e:
        response.status = 404
        return {"error": str(e)}


@route("/")
def index():
    return {"signbridge-server": "OK"}


if __name__ == "__main__":
    def print_local_ip():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        print(f"http://{s.getsockname()[0]}:7860/")
        s.close()

    print_local_ip()
    run(host="0.0.0.0", port=7860)
