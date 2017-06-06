import argparse
import logging

from common.imagemaker import get_image, get_overlay_text, draw_text_on_image, song_lyrics_exist
from metalcat.runner import run_spider

SCRAPED_ITEMS_FILE = 'output/lyrics.json'
DEFAULT_SONG = 'dopesmoker'
DEFAULT_ARTIST = 'sleep'

def crawl(song, artist): 
    return run_spider(song=song, artist=artist, feed_uri=SCRAPED_ITEMS_FILE)

def main():
    cat_logo = """     
       /\ /\ 
      > ^ ^ < 
    \m/  `  \m/ 
      \ / \ / 
       (___)_____ 
    """
    print(cat_logo)

    parser = argparse.ArgumentParser()
    parser.add_argument('-s',
                        '--song',
                        help='The name of the song to get lyrics from, with dashes instead of spaces',
                        default=DEFAULT_SONG,
                        required=False)
    parser.add_argument('-a',
                        '--artist',
                        help='The name of the artist to get lyrics from, with dashes instead of spaces',
                        default=DEFAULT_ARTIST,
                        required=False)
    parser.add_argument('-i',
                        '--image',
                        help='The path to the image file to draw lyrics on',
                        required=False)
    parser.add_argument('-u',
                        '--url',
                        help='The url of the image to draw lyrics on',
                        required=False)
    args = parser.parse_args()
    if not song_lyrics_exist(args.song, args.artist):
        crawl(args.song, args.artist)
    image = get_image(args.url, args.image)
    lyrics = get_overlay_text(args.song, args.artist)
    image_with_lyrics = draw_text_on_image(image, lyrics)

if __name__ == "__main__":
    logging.getLogger('PIL').setLevel(logging.WARNING)
    logging.getLogger('requests').setLevel(logging.WARNING)
    main()

