#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import paho.mqtt.client

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

with open("mqtt.auth", "r") as file:
    server = file.readline().split()
    credentials = file.readline().split()
mqttc = MyClient(server, credentials)
mqttc.subscribe("plants/*/moisture")

