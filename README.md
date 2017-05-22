# MetalCat

    metalcat - python app that overlays heavy metal lyrics onto cat photos, which can easily be deployed to Heroku

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/).

```sh
$ git clone git@github.com:creviera/metalcat.git
$ cd metalcat

$ pip install -r requirements.txt

$ heroku local
```

MetalCat should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run scrapy crawl metrolyrics_spider
$ heroku open
```
