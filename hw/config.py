# -*- coding: utf-8 -*-
import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'nk3k7527'

