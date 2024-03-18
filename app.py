from flask import Flask, jsonify, request, send_file
import sign2img
import os

TEXT_SIGN = True if os.environ.get("TEXT_SIGN", False) else False
if TEXT_SIGN:
    import text2sign

app = Flask(__name__)


@app.route("/text2sign")
def translate_text():
    if not TEXT_SIGN:
        return jsonify({"error": f"TEXT_SIGN is not trie"}), 400

    text = request.args.get("text", None)
    if not text:
        return jsonify({"error": "No text provided"}), 400

    symbol = text2sign.translate(text)
    return jsonify({"translation": symbol})


@app.route("/sign2img")
def covert_text():
    sign = request.args.get("sign", None)
    if not sign:
        return jsonify({"error": "No sign provided"}), 400

    img = sign2img.convert(sign)
    return send_file(img, mimetype='image/png', download_name="sign.png")


@app.route("/")
def index():
    return jsonify({"Server": "OK"})


@app.errorhandler(404)
def notfound(e):
    return jsonify({"error": "Not a path"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
