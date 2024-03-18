from bottle import route, run, request, response
import sign2img
import text2sign


@route("/text2sign")
def translate_text():
    text = request.query.get("text", None)
    if not text:
        response.status_code = 400
        return {"error": "No text provided"}

    symbol = text2sign.translate(text)
    return {"sign": symbol}


@route("/sign2img")
def convert_text():
    sign = request.query.get("sign", None)
    if not sign:
        response.status_code = 400
        return {"error": "No sign provided"}

    img = sign2img.convert(sign)
    response.content_type = 'image/png'
    return img


@route("/")
def index():
    return {"signbridge-server": "OK"}


if __name__ == "__main__":
    run(host="0.0.0.0", port=7860)
