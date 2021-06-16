from app import app, db, ma
from flask import request,jsonify
from app.Models.PlanModel import PlanModel, PlanSchema


@app.route('/crearPlan', methods=["POST"])
def crear_Plan():
    req_data =PlanSchema().load(request.get_json())
    db.session.add(req_data)
    db.session.commit()
    return "OK", 201


@app.route('/listarPlan', methods=["GET"])
def listar_Plan():
    plan = PlanModel.query.all()
    json = PlanSchema(many=True).dump(plan)
    return jsonify(json),200


@app.route('/categoria/<categoria_id>',methods=["GET"] )
def buscar_Plan(PK_ID_PLAN):
    plan = PlanModel.query.get(PK_ID_PLAN)
    json = PlanSchema().dump(plan)
    return jsonify(json),200


@app.route('/actualizarPlan',methods=["PUT"])
def actualizar_plan():
    req_data = request.get_json()
    PK_ID_PLAN = req_data['PK_ID_PLAN']
    nombre_plan = req_data['plan']
    update = PlanModel.query.filter_by(PK_ID_PLAN = PK_ID_PLAN).first()
    update.plan =  nombre_plan
    db.session.commit()
    return "OK",202

@app.route('/eliminarPlan/<PK_ID_PLAN>',methods=["DELETE"])
def eliminar_plan(PK_ID_PLAN):
    plan = PlanModel.query.get(PK_ID_PLAN)
    db.session.delete(plan)
    db.session.commit()
    return "OK", 200



    