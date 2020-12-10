FROM python:3.7.9
WORKDIR /user/src/app
COPY . .
RUN apt-get -y update
#RUN apt-get -y install python3
RUN apt-get -y install python3-pip
#RUN apt-get install python3-tk
RUN pip3 install PyMySQL
RUN pip3 install requests
RUN pip3 install jsonlib-python3
RUN pip3 install DateTime
#RUN apt-get -y install nano
#RUN apt-get -y install x11-xserver-utils
#ENV DISPLAY :0
EXPOSE 4200
#CMD xhost +
#CMD export DISPLAY=unix$DISPLAY
#CMD cp ~/.Xauthority ~root/
CMD python3 Billetera_Criptomoneda.py