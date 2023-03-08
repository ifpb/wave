FROM python:3-alpine3.17

WORKDIR /var/www
ADD . /var/www


RUN pip install -r requirements.txt

# define the port number the container should expose
EXPOSE 5000

CMD ["python", "app/run.py"]
