
# Atlas Skolstvi Data Collection

## About

This project aims to demonstrate basic scraping techniques using Python scrapy library on the school catalogue published at https://www.atlasskolstvi.cz.

## Requirements

```
Python 3.9+
pip package installer
virtualenv library
```

## Installation

Go to a folder and create a pyhon

```bash
cd your-parent-folder
virtualenv venv
```
This should create a `venv` environment in your folder.
Further, run  the below command to activate your virtual environement.

```bash
./venv/Scripts/activate

pip install -r requirements.txt
pip list
```

## Scrapy setup

Generate a basic scrapy project and your first spider

```
scrapy startproject src
scrapy genspider atlasskol atlasskolstvi.cz

```

## Settings 

Set `DATA_OUT` in `src/settings.py` to a path on your computer where crawled data will be stored.

Inspect other settings to fit your needs.


## Run

Woohoo!

```
scrapy crawl atlasskol
```