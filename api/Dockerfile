FROM python:3.8-alpine
ENV PYTHONUNBUFFERED 1

WORKDIR "/api"
COPY . .
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev
RUN pip install -r requirements.txt
RUN apk del .tmp-build-deps

RUN adduser -D user
USER user
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]