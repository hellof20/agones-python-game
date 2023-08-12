FROM python:3.8-slim-buster
WORKDIR /game
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY main.py main.py
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8888"]
EXPOSE 8888