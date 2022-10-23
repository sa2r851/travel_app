FROM python:3.9.7
WORKDIR /app
COPY ./src ./
RUN pip install --upgrade pip --no-cache-dir
RUN pip install -r /app/requirements.txt --no-cache-dir
CMD [ "python","manage.py","runserver","0.0.0.0:8000" ]
