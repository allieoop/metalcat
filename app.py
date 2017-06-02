import json
import os

import scrapy
from flask import Flask, render_template, request

from common.imagemaker import overlayLyrics, selectImage

app = Flask(__name__)
app.config.update(DEBUG = True)

@app.route("/", methods=['GET'])
def main():
    image = selectImage(request.args.get('url'))
    image_with_lyrics = overlayLyrics(image)
    return render_template(
        'index.html',
        title='MetalCat',
        img_src=image_with_lyrics
    )

if __name__ == "__main__":
    app.run()
