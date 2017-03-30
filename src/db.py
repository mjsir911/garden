#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
from os import path

__appname__     = ""
__author__      = "Marco Sirabella"
__copyright__   = ""
__credits__     = ["Marco Sirabella"]  # Authors and bug reporters
__license__     = "GPL"
__version__     = "1.0"
__maintainers__ = "Marco Sirabella"
__email__       = "msirabel@gmail.com"
__status__      = "Prototype"  # "Prototype", "Development" or "Production"
__module__      = ""

db = 'garden.db'
def __init__():
    if not path.exists(db):
        with sqlite3.connect(db) as conn:
            with open('garden.sql', 'r') as file:
                contents = file.read()

            cmds = contents.split(';')
            for cmd in cmds:
                conn.execute(cmd)




import datetime

def logplant(id, humidity):
    with sqlite3.connect(db) as conn:
        c = conn.cursor()
        c.execute('SELECT MAX(ROWID) from plant_log')
        maxr = c.fetchone()[0]
        if maxr is None:
            maxr = 0
        db_args = (maxr + 1, id, humidity, datetime.datetime.now())

        c.execute('INSERT INTO plant_log VALUES (?, ?, ?, ?)', db_args)

def logplants(all_plants):
        for id, moisture in all_plants.items():
            logplant(id, moisture)

def logoffice(temp, humidity):
    with sqlite3.connect(db) as conn:
        c = conn.cursor()
        c.execute('SELECT MAX(ROWID) from office_log')
        maxr = c.fetchone()[0]
        if maxr is None:
            maxr = 0
        db_args = (maxr + 1, humidity, temp, datetime.datetime.now())

        c.execute('INSERT INTO office_log VALUES (?, ?, ?, ?)', db_args)

#addvalues({1: 5, 2: 6, 3: 100, 4: 1})
#addvalue(1, 3)
__init__()
logoffice(50, 30)
