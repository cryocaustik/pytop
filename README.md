# PyTop

quick view of local processes via Django Rest Framework for API, VueJS for Web Interface, C3JS for charts, and Bulma for quick CSS framework. 

## Pre-Requisites

PyTop is build with [Python](https://www.python.org/) and makes use of [Poetry](https://poetry.eustace.io/) for quick and simple dependency management.

- [Python ^3.7](https://www.python.org/)
- [Poetry ^0.12.17](https://poetry.eustace.io/)

## Local Usage

from the project directory, run:

```bash
# install python dependencies
poetry install --no-dev

# run django migrations to build the database
python manage.py migrate

# run django dev server
python manage.py runserver
```

the application should now be running at http://localhost:8000


## Dependencies/Libraries used

### Python 

- [Poetry](https://poetry.eustace.io/)
- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [apscheduler](https://github.com/agronholm/apscheduler)
- [django-apscheduler](https://github.com/jarekwg/django-apscheduler)
- [psutil](https://github.com/giampaolo/psutil)

### CSS/JS

- [VueJS](https://vuejs.org/)
- [Bulma](https://bulma.io/)
- [Bulmaswatch](https://jenil.github.io/bulmaswatch/)
- [c3js](https://c3js.org/)
- [axios](https://github.com/axios/axios)
- [Moment.js](https://momentjs.com/)


### Python Dev 

- [Black](https://github.com/psf/black)
- [PyLint](https://github.com/PyCQA/pylint)