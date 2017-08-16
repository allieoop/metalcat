import json

from flask import Flask, render_template, request

from common.imagemaker import get_image, get_overlay_text, draw_text_on_image, get_cat_images, delete_images, archive_image, song_lyrics_exist
from metalcat.runner import run_spider

SCRAPED_ITEMS_FILE = 'output/lyrics.jl'
DEFAULT_SONG = 'countdown-to-extinction'
DEFAULT_ARTIST = 'megadeth'
METAL_CAT_DIR = 'static/metalcats/'
METAL_CAT_ARCHIVE = 'static/metalcats/archive/'

app = Flask(__name__)
app.config.update(DEBUG = True)

def crawl(song, artist):
    return run_spider(song=song, artist=artist, feed_uri=SCRAPED_ITEMS_FILE)

@app.route("/favorites")
def favorites():
    images = get_cat_images(METAL_CAT_ARCHIVE)
    return render_template(
        'favorites.html',
        title='MetalCat',
        images=images
    )

@app.route("/", methods=['GET'])
def main():
    song = request.args.get('song', DEFAULT_SONG)
    artist = request.args.get('artist', DEFAULT_ARTIST)
    url = request.args.get('url')
    image_to_save = request.args.get('image_to_save')
    if image_to_save:
        saved_image = archive_image(image_to_save)
        return render_template(
            'index.html',
            title='MetalCat',
            song=song,
            artist=artist,
            url=url,
            img_src=saved_image
        )
    if not song_lyrics_exist(song, artist):
        crawl(song, artist)
    image = get_image(image_url=url)
    lyrics = get_overlay_text(song, artist)
    delete_images(METAL_CAT_DIR)
    image_with_lyrics = draw_text_on_image(image, lyrics)
    return render_template(
        'index.html',
        title='MetalCat',
        song=song,
        artist=artist,
        url=url,
        img_src=image_with_lyrics
    )

if __name__ == "__main__":
    logging.getLogger('PIL').setLevel(logging.WARNING)
    logging.getLogger('requests').setLevel(logging.WARNING)
    app.run()
