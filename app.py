from bottle import Bottle, request, response
import sign2img
import text2sign

app = Bottle()

@app.route("/text2sign")
def translate_text():
    text = request.query.get("text", None)
    if not text:
        response.status_code = 400
        return {"error": "No text provided"}

    symbol = text2sign.translate(text)
    return {"sign": symbol}


@app.route("/sign2img")
def covert_text():
    sign = request.query.get("sign", None)
    if not sign:
        response.status_code = 400
        return {"error": "No sign provided"}

    img = sign2img.convert(sign)
    response.content_type = 'image/png'
    return img


@app.route("/")
def index():
    return {"Server": "OK"}


@app.error(404)
def notfound(e):
    response.status_code = 404
    return {"error": "Not a path"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
