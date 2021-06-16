
class PlanModel(db.Model):
    __tablename__ = "Plan"
    PK_ID_PLAN = db.Column(db.Integer, primary_key = True)
    FK_TYPE_PLAN = db.Column(db.Integer(50), nullable = False, unique=True)
    INIT_PRICE = db.Column(db.Integer)
    ACTIVE = db.Column(db.Integer)
    FK_ID_TYPE_PLAN = db.Column(db.Integer, db.ForeignKey('TypePlan.PK_ID_TYPE_PLAN'))

class PlanSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PlanModel
        include_fk = True
    
    @post_load
    def make_plan(self, data, **kwargs):
        return PlanModel(**data)