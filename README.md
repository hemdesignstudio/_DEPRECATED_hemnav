# Hemnav

Hem NAV API package.

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
`$ pipenv shell`

Install dependencies:
`$ pipenv install`

## Development
To run tests, run:
`$ python -m unittest`