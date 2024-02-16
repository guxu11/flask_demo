# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     __init__.py
   Description :
   Author :       guxu
   date：          2/15/24
-------------------------------------------------
   Change Activity:
                   2/15/24:
-------------------------------------------------
"""
import os

from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return "hello world"