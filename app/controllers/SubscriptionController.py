from app import app, db, ma
from flask import request,jsonify
from app.Models.SubscriptionModel import SubscriptionModel, SubscriptionSchema


@app.route('/crearSubscription', methods=["POST"])
def crear_Subscription():
    req_data =SubscriptionSchema().load(request.get_json())
    db.session.add(req_data)
    db.session.commit()
    return "OK", 201


@app.route('/listarSubscription', methods=["GET"])
def listar_Subscription():
    Subscription = SubscriptionModel.query.all()
    json = SubscriptionSchema(many=True).dump(Subscription)
    return jsonify(json),200


@app.route('/categoria/<categoria_id>',methods=["GET"] )
def buscar_Subscription(pk_idSubscription):
    Subscription = SubscriptionModel.query.get(pk_idSubscription)
    json = SubscriptionSchema().dump(Subscription)
    return jsonify(json),200


@app.route('/actualizarSubscription',methods=["PUT"])
def actualizar_Subscription():
    req_data = request.get_json()
    pk_idSubscription = req_data['pk_idSubscription']
    share = req_data['share']
    update = SubscriptionModel.query.filter_by(pk_idSubscription = pk_idSubscription).first()
    update.share =  share
    db.session.commit()
    return "OK",202

@app.route('/eliminarSubscription/<pk_idSubscription>',methods=["DELETE"])
def eliminar_Subscription(pk_idSubscription):
    Subscription = SubscriptionModel.query.get(pk_idSubscription)
    db.session.delete(Subscription)
    db.session.commit()
    return "OK", 200



    