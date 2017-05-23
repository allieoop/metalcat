# MetalCat

metalcat - python app that'll overlay lyrics from metrolyrics onto cat photos

## Running Locally

```sh
$ git clone git@github.com:creviera/metalcat.git
$ cd metalcat

$ pip install -r requirements.txt

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
