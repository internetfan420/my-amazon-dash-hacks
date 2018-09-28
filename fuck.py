#!/usr/bin/python -tt
# -*- coding:utf-8 -*-

import random
from twython import Twython
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

messages = [
    "fuckkkkit",
    "fuck it",
    "fuckthisshit",
    "Ill never understand bullshit",
    "bullshit.",
    "horseshit",
    "realy?!?!?!?",
    "WHACK AS HELL",
    "BULLSHIT",
    "THIS IS BS",
    "FUCCC",
    "FUCK ",
    "fuck",
    
    ]

message = random.choice(messages)

twitter.update_status(status=message)
print("Tweeted: " + message)

