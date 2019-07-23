# Hemnav

Hem NAV API package.

## Package installation
Having this package in the Pipfile and running `pipenv install` is not sufficient since that will not install dependencies. One has to run `pipenv install -e git+https://github.com/hemdesignstudio/hemnav@<version>#egg=hemnav` where `<version>` is the wanted version (git tags).

# Continous development

## Install everything
Create the virtual environment:
`$ pipenv shell`

Install dependencies:
`$ pipenv install`

## Development
To run tests, run:
`$ python -m unittest`