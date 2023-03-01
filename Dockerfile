FROM python:3.9

WORKDIR /app

COPY Pipfile /app
COPY Pipfile.lock /app
RUN pip install pipenv 
RUN pipenv install --deploy
COPY django-q-1.0.tar.gz /app
RUN pipenv install django-q-1.0.tar.gz --skip-lock

COPY . /app
ENTRYPOINT ["pipenv","run","python","manage.py","runserver","0.0.0.0:8000"]

