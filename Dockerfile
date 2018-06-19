# Run build python
FROM ubuntu:18.10
MAINTAINER alainchiasson

#RUN echo "deb http://archive.ubuntu.com/ubuntu/ $(lsb_release -sc) main universe" >> /etc/apt/sources.list
RUN apt-get update

# Add some tools
RUN apt-get install -y tar \
                       curl \
                       wget \
                       dialog \
                       net-tools \
                       build-essential\
                       python \
                       python-dev \
                       python-distribute \
                       python-pip \
                       libmysqlclient-dev

COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip install -r requirements.txt

EXPOSE 5000

CMD python api.py
