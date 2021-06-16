from app.__init__ import app, db, ma
from app.models.Service import ServiceModel, ServiceSchema

from flask import request, jsonify, flash


@app.route("/service", methods=["GET"])
def get_services():
    service = ServiceModel.query.all()
    json = ServiceSchema(many=True).dumps(service)
    return jsonify(json), 200


@app.route("/service/<service_id>", methods=["GET"])
def get_service_id(service_id):
    service = ServiceModel().load(request.get(service_id))
    json = ServiceSchema().dump(service)
    return jsonify(json), 200


@app.route("/service", methods=["POST"])
def post_service():
    req_data = ServiceSchema().load(request.get_json())
    db.session.add(req_data)
    db.session.commit()
    return "OK", 201


@app.route("/service/<service_id>", methods=["DELETE"])
def delete_service(service_id):
    update = ServiceModel.query.filter_by(service_id=service_id).first()
    update.activate = False
    db.session.commit()
    return "OK", 200


@app.route("/service/<service_id>", methods=["PUT"])
def put_service(service_id):
    req_data = request.get_json()
    update = ServiceModel.query.filter_by(service_id=service_id).first()

    update.name = req_data["name"]
    update.amount = req_data["amount"]
    update.service_price = req_data["service_price"]

    db.session.commit()

    return "OK", 202
