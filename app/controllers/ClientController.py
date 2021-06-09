from app.__init__ import app, db, ma
from app.models.Client import ClientModel, ClientSchema

from flask import request, jsonify, flash


@app.route("/clients", methods=["GET"])
def get_clients():
    clients = ClientModel.query.all()
    json = ClientSchema(many=True).dumps(clients)
    return jsonify(json), 200


@app.route("/client/<client_id>", methods=["GET"])
def get_client_id(client_id):
    client = ClientSchema().load(request.get(client_id))
    json = ClientSchema().dump(client)
    return jsonify(json), 200


@app.route("/client", methods=["POST"])
def post_client():
    req_data = ClientSchema().load(request.get_json())
    db.session.add(req_data)
    db.session.commit()
    return "OK", 201


@app.route("/client/<client_id>", methods=["DELETE"])
def delete_client(client_id):
    update = ClientModel.query.filter_by(client_id=client_id).first()
    update.activate = False
    db.session.commit()
    return "OK", 200


@app.route("/client/<client_id>", methods=["PUT"])
def put_client_password(client_id):
    req_data = request.get_json()
    new_password = req_data["password"]
    update = ClientModel.query.filter_by(client_id=client_id).first()
    if update.password != new_password:
        update.password = new_password
        db.session.commit()
        return "The password was updated successfully", 202
    else:
        return "Choose a different password than the previous one", 200
