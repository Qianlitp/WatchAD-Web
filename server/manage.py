#!/usr/bin/python3
# coding: utf-8

from flask_script import Manager
from flask_cors import CORS
from app import app

CORS(app)
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
