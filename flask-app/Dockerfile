FROM python:3.9-slim
WORKDIR /code
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_APP=app.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1
ENV FLASK_RUN_PORT=8000
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 8000
CMD ["flask", "run"]
