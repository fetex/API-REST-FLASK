class SubscriptionModel(db.Model):
    __tablename__ = "Subscription"
    pk_idSubscription = db.Column(db.Integer, primary_key = True)
    share = db.Column(db.Integer, nullable = False, unique=True, default=1)
    active = db.Column(db.TINYINT, nullable = False, default=1)

class SubscriptionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = SubscriptionModel
        include_fk = False
    
    @post_load
    def make_Subscription(self, data, **kwargs):
        return SubscriptionModel(**data)