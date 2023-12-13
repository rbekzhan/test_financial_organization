FROM python:3.8
WORKDIR /code
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH /code

COPY requirements.txt  ./
RUN pip install -U pip
RUN pip install -r requirements.txt


COPY . ./

ENTRYPOINT ["sh", "./entrypoint.sh"]