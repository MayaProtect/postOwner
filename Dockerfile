FROM python:3.10-bullseye

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

# ENV VARS

EXPOSE 8000

CMD python run.py