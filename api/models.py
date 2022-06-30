# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from datetime import datetime

import json

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class running_records(db.Model):
    __tablename__ = 'running_records'
    id           = db.Column(db.Integer()   , primary_key=True)
    robot_id     = db.Column(db.Integer()   , nullable=False)
    data         = db.Column(db.String(256) , nullable=False)
    run_time     = db.Column(db.DateTime()  , default=datetime.utcnow)
    time_use     = db.Column(db.Float()     , default=0.0)
    success      = db.Column(db.Boolean()   , nullable=False)
    power_use    = db.Column(db.Float()     ,nullable=False)


    def __repr__(self):
        return str( self.id ) 

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update_data(self, new_data):
        self.data = new_data

    @classmethod
    def get_by_id(cls, robot_id):
        return cls.query.filter_by(robot_id=robot_id).first()

    def toDICT(self):

        cls_dict         = {}
        cls_dict['_id']  = self.id
        cls_dict['data'] = self.data
        cls_dict['run_time'] = self.run_time
        cls_dict['time_use'] = self.time_use
        cls_dict['success'] = self.success
        cls_dict['power_use'] = self.power_use

        return cls_dict

    def toJSON(self):

        return self.toDICT()

class maintain_record(db.Model):
    __tablename__        = 'maintain_record'
    id                   = db.Column(db.Integer()        ,primary_key=True)
    robot_id             = db.Column(db.Integer()        ,nullable=False)
    maintain_time        = db.Column(db.DateTime()       ,default=datetime.utcnow)
    maintain_note        = db.Column(db.String(512)      ,nullable=True)
    next_maintain_time   = db.Column(db.DateTime()       ,nullable=False)
    maintained_part      = db.Column(db.String(512)      ,nullable=True)

    def __repr__(self):
        return str( self.id ) 

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update_data(self, new_data):
        self.data = new_data

    @classmethod
    def get_by_robot_id(cls, id):
        return cls.query.filter_by(robot_id=robot_id)

    def toDICT(self):

        cls_dict         = {}
        cls_dict['_id']  = self.id
        cls_dict['robot_id'] = self.robot_id
        cls_dict['maintain_time'] = self.maintain_time
        cls_dict['maintain_note'] = self.maintain_note
        cls_dict["next_maintain_time"] = self.next_maintain_time
        cls_dict["maintained_part"] = self.maintained_part

        return cls_dict

    def toJSON(self):

        return self.toDICT()

class sensor_record(db.Model):
    __tablename__ = "sensor_record"
    id                   = db.Column(db.Integer()    ,primary_key=True)
    robot_id             = db.Column(db.Integer()    ,nullable=False)
    timestamp            = db.Column(db.DateTime()   ,default=datetime.utcnow)
    sensor_data_0        = db.Column(db.Float()      ,default=0.0)
    sensor_data_1        = db.Column(db.Float()      ,default=0.0)
    sensor_data_2        = db.Column(db.Float()      ,default=0.0)
    sensor_data_3        = db.Column(db.Float()      ,default=0.0)
    maintained_part      = db.Column(db.String(512))

    def __repr__(self):
        return str( self.id ) 

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update_data(self, new_data):
        self.data = new_data

    @classmethod
    def get_by_robot_id(cls, id):
        return cls.query.filter_by(robot_id=robot_id)

    def toDICT(self):

        cls_dict         = {}
        cls_dict['_id']  = self.id
        cls_dict['robot_id'] = self.robot_id
        cls_dict['timestamp'] = self.timestamp
        cls_dict['sensor_data_0'] = self.sensor_data_0
        cls_dict['sensor_data_1'] = self.sensor_data_1
        cls_dict['sensor_data_2'] = self.sensor_data_2
        cls_dict['sensor_data_3'] = self.sensor_data_3
        cls_dict['maintained_part'] = self.maintained_part

        return cls_dict

    def toJSON(self):

        return self.toDICT()


class product_record(db.Model):
    __tablename__ = "product_record"
    robot_id             = db.Column(db.Integer()    ,primary_key=True)
    company_info         = db.Column(db.String(512)  ,default=datetime.utcnow)
    telephone            = db.Column(db.String(256)  ,nullable=False)
    purchace_date        = db.Column(db.DateTime()   ,nullable=False)

    def __repr__(self):
        return str( self.id ) 

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update_data(self, new_data):
        self.data = new_data

    @classmethod
    def get_by_robot_id(cls, id):
        return cls.query.filter_by(robot_id=robot_id)

    def toDICT(self):

        cls_dict         = {}
        cls_dict['_id']  = self.id
        cls_dict['robot_id'] = self.robot_id
        cls_dict['timestamp'] = self.timestamp
        cls_dict['sensor_data_0'] = self.sensor_data_0
        cls_dict['sensor_data_1'] = self.sensor_data_1
        cls_dict['sensor_data_2'] = self.sensor_data_2
        cls_dict['sensor_data_3'] = self.sensor_data_3
        cls_dict['maintained_part'] = self.maintained_part

        return cls_dict

    def toJSON(self):

        return self.toDICT()
