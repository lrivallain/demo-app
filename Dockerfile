FROM python:3.9-slim-buster

WORKDIR /app

COPY . .
RUN pip install -r requirements.txt
ENV FLASK_APP="main.py"

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=80"]
