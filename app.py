from flask import Flask, jsonify, request, send_file
import psutil
import sign2img


def get_total_ram():
    total_ram_bytes = psutil.virtual_memory().total
    return total_ram_bytes / (1024 * 1024)


TOTAL_RAM = get_total_ram()
MIN_RAM = 800  # for text2sign
TEXT_SIGN = TOTAL_RAM > MIN_RAM
TEXT_SIGN = False  # temp

if TEXT_SIGN:
    import text2sign
    
app = Flask(__name__)


@app.route("/text2sign")
def translate_text():
    if not TEXT_SIGN:
        return jsonify({"error": f"No enough RAM, {MIN_RAM}/{TOTAL_RAM}"}), 400

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
    return send_file(img, mimetype='image/png', download_name="sign.png", as_attachment=True)


if __name__ == "__main__":
    app.run()
