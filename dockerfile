FROM python

WORKDIR /usr/src/app
COPY . .

CMD [ "python", "./fatsecret.py"]