from flask import Flask, request
import logging
import json
from google_trans_new import google_translator

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

translator = google_translator()
structure = [["переведи", "переведите"], ["слово"], None]


def match(structure, words):
    if len(structure) != len(words):
        return False

    matched = []
    for i, pattern in enumerate(structure):
        if pattern is not None:
            if words[i] not in pattern:
                return False
        else:
            matched.append(words[i])

    return matched


@app.route('/post', methods=['POST'])
def main():
    logging.info('Request: %r', request.json)
    response = {
        'session': request.json['session'],
        'version': request.json['version'],
        'response': {
            'end_session': False
        }
    }
    handle_dialog(response, request.json)
    logging.info('Response: %r', response)
    return json.dumps(response)


def handle_dialog(res, req):
    if req['session']['new']:
        res['response']['text'] = "Привет! Попросите меня перевести слово по следующей форме: переведи слово " \
                                  "<слово>, и я переведу его!"
        return

    words = req['request']['original_utterance'].lower().split()
    matched = match(structure, words)
    if matched:
        res['response']['text'] = f"{translator.translate(matched[-1], lang_tgt='en')}"
    else:
        res['response']['text'] = "Извините, я вас не понимаю. Попросите меня перевести слово, и я переведу " \
                                  "его на английский."


if __name__ == '__main__':
    app.run()
