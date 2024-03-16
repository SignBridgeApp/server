from flask import Flask, jsonify, request
import spoken2sign

app = Flask(__name__)

@app.route('/translate', methods=['GET'])
def translate_text():
    spoken_text = request.args.get('text', '')
    if not spoken_text:
        return jsonify({'error': 'No text provided'}), 400
    
    symbol = spoken2sign.translate(spoken_text)
    return jsonify({'translation': symbol})

if __name__ == '__main__':
    app.run()
