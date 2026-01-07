FROM ubuntu:noble-20251013
COPY pymysql_flask.py .
COPY static ./static
RUN sed -i 's/archive.ubuntu.com/free.nchc.org.tw/g' /etc/apt/sources.list.d/ubuntu.sources && \
    apt-get update && apt-get -y upgrade && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y openssh-server python3-dev python3-pip && \
    apt-get -y autoclean && apt-get -y autoremove && \
    python3 -m pip install --no-cache-dir pymysql cryptography flask flask_cors --break-system-packages --ignore-installed
CMD ["python3", "pymysql_flask.py"]



#用這個名稱建image
#docker build -t python3_image01 .
