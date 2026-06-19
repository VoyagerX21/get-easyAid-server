from marshmallow import fields, Schema, validate

class PromptReq(Schema):

    courseType = fields.Str(required=True)
    status = fields.Str(required=True, validate=validate.OneOf(["student", "working"]))
    courses = fields.List(fields.Str)
    institute = fields.Str()
    name=fields.Str()
    organization=fields.Str()
    position=fields.Str()
    specialization=fields.Url()
    year=fields.Str()

class PromptRes(Schema):

    success=fields.Bool()
    job_id=fields.UUID()