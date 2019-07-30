# Hemnav

Hem NAV API package. [![CircleCI](https://circleci.com/gh/hemdesignstudio/hemnav.svg?style=svg)](https://circleci.com/gh/hemdesignstudio/hemnav)

## Package installation
Having this package in the Pipfile and running `pipenv install` is not sufficient since that will not install dependencies. One has to run `pipenv install -e git+https://github.com/hemdesignstudio/hemnav@<version>#egg=hemnav` where `<version>` is the wanted version (git tags).

## Setting up the config
This package reads a config yaml file to retireve the NAV url and store name. Username and password is still provided through environment variables.
Create a `config.yml` file in the root of your app-directory. Here's an example of how it should look.

```
dev:
  base_url: "https://wsmyway473.navmoln.se:47301/MyWay473Services/WS/"
  eu:
    store_name: "Hem FAL Sweden AB"
  us:
    store_name: "Hem FAL Inc"

test:
  base_url: "https://wsmyway473.navmoln.se:47301/MyWay473Services/WS/"
  eu:
    store_name: "Hem FAL Sweden AB"
  us:
    store_name: "Hem FAL Inc"

prod:
  base_url: "https://wsmyway473.navmoln.se:47301/MyWay473Services/WS/"
  eu:
    store_name: "Hem FAL Sweden AB"
  us:
    store_name: "Hem FAL Inc"
```

# Continous development

## Install everything
Create the virtual environment:
```sh
$ pipenv shell
```

Install dependencies:
```sh
$ pipenv install
```

## Development
To run tests, run:
```sh
$ python -m unittest
```

To run tests with coverage:
```sh
$ coverage run -m unittest
```

To see coverage resulst:
```sh
$ coverage report
```

## Releasing new versions of hemnav
To release a new version of hemnav you first have to create a tag (a github release).
You can read about tags here: https://git-scm.com/book/en/v2/Git-Basics-Tagging

First, change the version number in setup.py

Package your new version using this commnad:
```sh
$ python setup.py sdist
```
Release your new version using this command:
```sh
$ git tag -a <the new version> -m "Super short version description"
```
