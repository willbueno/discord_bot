FROM python:3

COPY /api /api
COPY /bot /bot
COPY main.py main.py
COPY credentials.json credentials.json
COPY token.json token.json
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD ["python", "main.py"]