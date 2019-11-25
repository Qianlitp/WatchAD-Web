FROM python:3.6

LABEL maintainer="9ian1i <9ian1itp@gmail.com>"

RUN mkdir /app

COPY . /app/

WORKDIR /app

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

CMD gunicorn -w 4 -b :5000 -u www-data -g www-data --access-logfile - manage:app