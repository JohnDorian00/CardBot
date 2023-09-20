FROM python:3.11.5-alpine3.17
WORKDIR /code
COPY requirements.txt /code
RUN pip install -r requirements.txt --no-cache-dir
COPY app.py /code
COPY requirements.txt /code
CMD python app.pyp