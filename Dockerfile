FROM rasa/rasa:2.6.1-full

USER root

RUN apt-get update -qq

WORKDIR /app

ADD . .

ENTRYPOINT []

USER 1001

CMD $(echo “rasa run -p $PORT -m models --credentials credentials.yml --enable-api --log-file out.log --endpoints endpoints.yml” | sed ‘s/=//’)