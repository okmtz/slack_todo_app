FROM python:3.7

RUN mkdir /app
WORKDIR /app

COPY entrypoint.sh /app/entrypoint.sh
COPY app/ /app

RUN pip install --upgrade pip --no-cache-dir
RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 5000
ENV PYTHONPATH "${PYTHONPATH}:/app/"
ENV FLASK_APP "/app/run.py"
CMD ["/app/entrypoint.sh"]