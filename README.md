# MetalCat

metalcat - python app that'll overlay lyrics from metrolyrics onto cat photos

## Usage
```sh
$ python metalcat.py --help

     /\ /\    
    > ^ ^ <
  \m/  `  \m/
    \ / \ /
     (___)______

usage: metalcat.py [-h] [-s SONG] [-a ARTIST] [-i IMAGE] [-u URL]

optional arguments:
  -h, --help                  show this help message and exit
  -s SONG, --song SONG        The name of the song to get lyrics from, with dashes instead of spaces
  -a ARTIST, --artist ARTIST  The name of the artist to get lyrics from, with dashes instead of spaces
  -i IMAGE, --image IMAGE     The path to the image file to draw lyrics on
  -u URL, --url URL           The url of the image to draw lyrics on

```

## Running Locally

```sh
$ git clone git@github.com:creviera/metalcat.git
$ cd metalcat

$ pip install -r requirements.txt

$ python metalcat.py
```

Check your `static/metalcats` folder in the project directory to see your metalcat image

## Running Locally with Heroku

```sh
$ git clone git@github.com:creviera/metalcat.git
$ cd metalcat

$ pip install -r requirements.txt

$ heroku local
```

View metalcat images on http://localhost:5000 :metal:

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku open
```

## Metrolyrics spider

The spider will automatically run when you refresh the page or run the metalcat.py script unless lyrics for the specified song already exist in `output/lyrics.jl`. You can change which Metrolyrics page the spider scrapes by specifying the song and artist in the url parameters, e.g. http://localhost:5000/?song=space-time&artist=gojira. 

If you want to run the spider manually:

```
$ scrapy crawl metrolyrics_spider -a song=space-time -a artist=gojira -o output/lyrics.jl
```

Or, with heroku:

```
$ heroku run scrapy crawl metrolyrics_spider -a song=space-time -a artist=gojira -o output/lyrics.jl
```

## Example

https://metalcat.herokuapp.com/

