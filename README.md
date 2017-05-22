# MetalCat

metalcat - python app that overlays heavy metal lyrics onto cat photos

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/).

```sh
$ git clone git@github.com:creviera/metalcat.git
$ cd metalcat

$ pip install -r requirements.txt

$ scrapy crawl metrolyrics_spider -o output/lyrics.json
$ heroku local
```

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run scrapy crawl metrolyrics_spider -o output/lyrics.json
$ heroku open
```

## Example

https://metalcat.herokuapp.com/
