FROM python:3.7

WORKDIR /opt/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /opt/app/rest-api

EXPOSE 5000

CMD ["python3", "app.py"]