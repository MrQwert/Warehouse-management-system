FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python -m pip install Django
RUN python -m pip install pillow

RUN apt update
WORKDIR /ecommerce_cosmetika
COPY ecommerce_cosmetika /ecommerce_cosmetika/


EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]
