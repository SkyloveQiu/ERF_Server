# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import request
from flask_restx import Api, Resource, fields

from api.models import db, running_records

rest_api = Api(version="1.0", title="Datas API")

"""
API Interface:
   
   - /datas
       - GET: return all items
       - POST: create a new item
   
   - /datas/:id
       - GET    : get item
       - PUT    : update item
       - DELETE : delete item
"""

"""
Flask-RestX models Request & Response DATA
"""

# Used to validate input data for creation
create_records = rest_api.model('CreateRecords', {"robot_id": fields.Integer(),
                                                "data": fields.String(required=True, min_length=1, max_length=255),
                                                "time_use":fields.Float(required=True),
                                                "success":fields.Boolean(),
                                                "power_use":fields.Float()})

# Used to validate input data for update

"""
    Flask-Restx routes
"""

@rest_api.route('/api/datas')
class Items(Resource):

    """
       Return all items
    """
    def get(self):

        items = running_records.query.all()
        
        return {"success" : True,
                "msg"     : "Items found ("+ str(len( items ))+")",
                "datas"   : str( items ) }, 200

    """
       Create new item
    """
    @rest_api.expect(create_records, validate=True)
    def post(self):

        # Read ALL input  
        req_data = request.get_json()

        # Get the information    
        item_data = req_data.get("data")
        robot_id = req_data.get("robot_id")
        time_use = req_data.get("time_use")
        success = req_data.get("success")
        power_use = req_data.get("power_use")
        # Create new object
        new_item = running_records(robot_id=robot_id,data=data,time_use=time_use,success=success,power_use=power_use)

        # Save the data
        new_item.save()
        
        return {"success": True,
                "msg"    : "Item successfully created ["+ str(new_item.id)+"]"}, 200

@rest_api.route('/api/datas/<int:id>')
class ItemManager(Resource):

    """
       Return Item
    """
    def get(self, id):

        item = running_records.get_by_id(id)

        if not item:
            return {"success": False,
                    "msg": "Item not found."}, 400

        return {"success" : True,
                "msg"     : "Successfully return item [" +str(id)+ "]",
                "data"    :  item.toJSON()}, 200


    """
       Delete Item
    """
    def delete(self, id):

        # Locate the Item
        item = running_records.get_by_id(id)

        if not item:
            return {"success": False,
                    "msg": "Item not found."}, 400

        # Delete and save the change
        running_records.query.filter_by(id=id).delete()
        db.session.commit()

        return {"success" : True,
                "msg"     : "Item [" +str(id)+ "] successfully deleted"}, 200                           
