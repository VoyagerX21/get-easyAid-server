from marshmallow import fields, Schema

class JobRes(Schema):

    job_id=fields.UUID()
    status=fields.Str()
    firstRes=fields.Str()
    secondRes=fields.Str()
    time=fields.Float()