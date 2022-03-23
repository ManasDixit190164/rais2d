RUN apt update && apt upgrade -y

RUN apt install git curl python3-pip ffmpeg -y

RUN pip3 install -U pip

RUN cd /

RUN git clone https://github.com/ManasDixit190164/rais2d

RUN cd rais2d

WORKDIR /rais2d

RUN pip3 install -U -r requirements.txt

CMD python3 PROCFILE
