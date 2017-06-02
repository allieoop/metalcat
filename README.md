# MetalCat
```
metalcat - python app that'll overlay lyrics from metrolyrics onto cat photos

     /\ /\    
    > ^ ^ <
  \m/  `  \m/
    \ / \ /
     (___)_____
```

## Usage
```sh
$ python3 test.py --help
usage: test.py [-h] [-s SONG] [-a ARTIST] [-i IMAGE] [-u URL]

optional arguments:
  -h, --help                  show this help message and exit
  -s SONG, --song SONG        The name of a song, with dashes instead of spaces
  -a ARTIST, --artist ARTIST  The name of an artist, with dashes instead of spaces
  -i IMAGE, --image IMAGE     The path of the image file
  -u URL, --url URL           The url of the image file
```

## Running Locally

```sh
$ git clone git@github.com:creviera/metalcat.git
$ cd metalcat

$ pip install -r requirements.txt

$ python test.py

$ python test.py --song dopesmoker --artist sleep
```

## Running Locally with Heroku

```sh
$ git clone git@github.com:creviera/metalcat.git
$ cd metalcat

$ pip install -r requirements.txt

$ scrapy crawl metrolyrics_spider -a song=dopesmoker -a artist=sleep -o output/lyrics.json
$ heroku local
```

Check the output folder in the project directory for your metalcat image :metal:

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run scrapy crawl metrolyrics_spider -a song=dopesmoker -a artist=sleep -o output/lyrics.json
$ heroku open
```

## Example

https://metalcat.herokuapp.com/
