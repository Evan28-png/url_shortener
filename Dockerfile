FROM python:latest
WORKDIR /app

COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000

RUN useradd app
USER app

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:3000"]
