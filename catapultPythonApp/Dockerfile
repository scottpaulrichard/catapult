FROM tiangolo/uwsgi-nginx-flask:python3.7
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./app /app
RUN mkdir /root/.aws
COPY credentials /root/.aws/credentials
COPY ./uwsgi.ini uwsgi.ini
