
# Atlas Skolstvi Data Collection

## About

This project aims to demonstrate scraping techniques using Python scrapy library on the school catalogue published at https://www.atlasskolstvi.cz.

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

pip
```




## Scrapy setup

Generate a basic scrapy project and your first spider

```
scrapy startproject src
scrapy genspider atlasskol atlasskolstvi.cz

```


