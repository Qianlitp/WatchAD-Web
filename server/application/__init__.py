#!/usr/bin/python3
# coding: utf-8

from flask import Flask
from config.config import config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from application.controller import IndexController
    app.register_blueprint(IndexController.index_blueprint)

    from application.controller import ActivityController
    app.register_blueprint(ActivityController.activity_blueprint)

    from application.controller import ConfigController
    app.register_blueprint(ConfigController.config_blueprint)

    from application.controller import EntryController
    app.register_blueprint(EntryController.entry_blueprint)

    from application.controller import InvasionController
    app.register_blueprint(InvasionController.invasion_blueprint)

    from application.controller import SettingsController
    app.register_blueprint(SettingsController.setting_blueprint)

    from application.controller import RecordController
    app.register_blueprint(RecordController.record_blueprint)

    return app
