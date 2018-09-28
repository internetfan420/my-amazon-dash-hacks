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
    "GOOOOOAAAAAAAAAAALLLLLLLLLLLLLLL",
    "BACK OF THE NETTTTT",
    "GOALLLLLLLL",
    "GOOOOOOAAAAALLLLLL",
    "THATS WHAT IM TALKING ABOUTTTTTT",
    "GOOOOOOOOAAAAAAAAAAAAAAAAAAAAAAAAAAAALLLLLLLLL",
    "TEAM GGGGGG-OAL UNIT",
    "GOALGOALGOALS",
    "GOAL BOYZ ENT",
    "GOOOOOOAAAALLLLLL",
    "GGGGGGGGGGGGOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOAAAAAAAAAAAAAAAAAAAAALLLLL",
    "VAMOSSSSSSSSS",
    "ESO ESO ESO GOAL",
    
    ]

message = random.choice(messages)

twitter.update_status(status=message)
print("Tweeted: " + message)
