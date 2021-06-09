from app.__init__ import db


class Plan(db.Model):
    pk_idPlan = db.Column(db.Integer, primary_key=True)
    init_price = db.Column(db.Interger, nullable=False)
    duration = db.Column(db.Interger, nullable=False)
    active = db.Column(db.Boolean, nullable=False)

    # fk_TypePlan = db.Column(db.Integer, db.ForeignKey('Client.pk_idClient'))
