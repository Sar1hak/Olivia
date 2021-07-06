cd app/
#Start Rasa Server with nlu model
rasa run --model models --enable-apt --cors "*" --debug \
         -p $PORT