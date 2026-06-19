from marshmallow import fields, Schema

class RetryRes(Schema):

    success=fields.Bool()