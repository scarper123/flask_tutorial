# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from flask import Flask

__authors__ = "Shanming Liu"

app = Flask(__name__)
app.config.from_object('config')

from app import views
