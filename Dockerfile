FROM ubuntu:18.04
ENTRYPOINT []
RUN apt-get update && apt-get install -y python3 python2-pip && python3 -m pip pip install --no-cache --u$he --upgrade pip && pip3 install --no-cache rasa==2.6.1
ADD . /app/
RUN chmod +x /app/start_services.sh
CMD /app/start_services.sh