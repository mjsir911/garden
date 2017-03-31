#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import paho.mqtt.client
import db

__appname__     = ""
__author__      = "CJ Adams"
__copyright__   = ""
__credits__     = ["Marco Sirabella"]  # Authors and bug reporters
__license__     = "GPL"
__version__     = "1.0"
__maintainers__ = "Marco Sirabella"
__email__       = "msirabel@gmail.com"
__status__      = "Prototype"  # "Prototype", "Development" or "Production"
__module__      = ""

class MyClient(paho.mqtt.client.Client):
    def __init__(self, server, creds):
        super().__init__(client_id="db_server", clean_session=False)
        self.username_pw_set(creds[0], creds[1])
        self.connect(server[0], server[1])

    def on_message(self, client, userdata, message):
        type = message.topic.split('/')[0]
        if type == 'plants':
            self.plant_log(message)

    def plant_log(self, message):
        id = message.topic.split('/')[1]
        db.logplant(id, int(message.payload))


with open("mqtt.auth", "r") as file:
    server = file.readline().split()
    server[1] = int(server[1])
    credentials = file.readline().split()

mqttc = MyClient(server, credentials)
for i in range(4):
    mqttc.subscribe('plants/{}/moisture'.format(i))
while True:
    mqttc.loop()
