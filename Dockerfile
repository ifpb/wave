FROM python:3-alpine3.17

WORKDIR /var/www
ADD . /var/www

ENV STATIC_URL /static
ENV STATIC_PATH app/static
RUN pip install -r requirements.txt

# define the port number the container should expose
EXPOSE 5000

CMD ["python", "app/app.py"]
