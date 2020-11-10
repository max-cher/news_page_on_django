# pull official base image
#FROM python:3.8.3-alpine
#FROM python:3.7-slim
#FROM python:3.6
FROM python:3.8.3-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt


# copy project
COPY . .

CMD python manage.py collectstatic

#RUN python -c "import django; django.setup(); \
#   from django.contrib.auth.management.commands.createsuperuser import get_user_model; \
#   get_user_model()._default_manager.db_manager('$DJANGO_DB_NAME').create_superuser( \
#   username='$DJANGO_SU_NAME', \
#   email='$DJANGO_SU_EMAIL', \
#   password='$DJANGO_SU_PASSWORD')"

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
