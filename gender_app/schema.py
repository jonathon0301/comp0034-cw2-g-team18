from app import ma, db
from models import Gender_pay
from marshmallow import Schema, fields


class GenderPay(Schema):
    id = fields.Integer()
    DiffMeanHourlyPercent = fields.String()
    DiffMedianHourlyPercent = fields.String()
    DiffMeanBonusPercent = fields.String()
    DiffMedianBonusPercent = fields.String()
    MaleBonusPercent = fields.String()
    FemaleBonusPercent = fields.String()
    MaleLowerQuartile = fields.String()
    FemaleLowerQuartile = fields.String()
    MaleLowerMiddleQuartile = fields.String()
    FemaleLowerMiddleQuartile = fields.String()
    MaleUpperMiddleQuartile = fields.String()
    FemaleUpperMiddleQuartile = fields.String()
    MaleTopQuartile = fields.String()
    FemaleTopQuartile = fields.String()
    EmployerSizeMedian = fields.String()
    Region = fields.String()
    Industry = fields.String()
    EmployerSize = fields.String()
    # class Meta:
    #     model = Gender_pay
    #     load_instance = True
    #     sqla_session = db.session
    #     include_relationships = True
