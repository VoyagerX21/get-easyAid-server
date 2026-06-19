from marshmallow import fields, Schema

class HealthRes(Schema):

    success=fields.Str()