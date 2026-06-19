from marshmallow import fields, Schema, validate

class ObjectSchema(Schema):

    title=fields.Str(required=True)
    URL=fields.Url(required=True)
    cached=fields.Bool()
    id=fields.UUID()
    rating=fields.Str()

class SubmitReq(Schema):

    obj = fields.Nested(ObjectSchema, required=True)

class SubmitRes(Schema):

    courselist = fields.List(fields.List(fields.Raw()))
    obj = fields.Nested(ObjectSchema)
    success = fields.Bool()
    url = fields.Url()