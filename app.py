from bottle import route, run, request, response
from time import time
import sign2img
try:
    import text2sign
except Exception as e:
    print(e)


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
    if not sign:
        response.status = 400
        return {"error": "No sign provided"}

    try:
        img = sign2img.convert(sign)
        response.content_type = 'image/png'
        return img
    except Exception as e:
        response.status = 404
        return {"error": str(e)}


@route("/")
def index():
    return {"signbridge-server": "OK"}


if __name__ == "__main__":
    run(host="0.0.0.0", port=7860)
