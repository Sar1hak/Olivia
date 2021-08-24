# 🐶Olivia - The Portfolio Assistant Bot
Olivia helps you go through the projects/achievements displayed in the author's Website:

https://sarthakchauhan-portfolio.herokuapp.com/

Basic Chitchat aspects also added to it.

## Rasa
Build Modern Chatbot using Rasa

Rasa is an open source machine learning framework for building AI assistants and chatbots. 
Mostly you don’t need any programming language experience to work in Rasa.

## Installation

To install Olivia, please clone the git repo on to your local system and run:

```sh
cd Olivia
make install
```

This will install the bot and all of its requirements.
Note that this bot should be used with python 3.7+.

## Train Olivia:

Use `rasa train` to train a model (this will take a significant amount of memory to train,
if you want to train it faster, try the training command with
`--augmentation 0`).

Then, to run, first set up your action server in one terminal window:
```bash
rasa run actions --actions actions.actions
```

## Test Olivia
Use `rasa train` to train a model (this will take a significant amount of memory to train,
if you want to train it faster, try the training command with
`--augmentation 0`).

Then to run Website on locahost, set up your local server in one terminal window:
```bash
rasa run -m models --enable-api --cors "*"
```

Open up the index.html file provided in the Olivia git folder to start testing Olivia.

## Debug Chatbot
To view the underlying operations which are excuted while conversing with Olivia,
set up your debug local server in one terminal window:
```bash
rasa run -m models --enable-api --cors "*" --debug
```
