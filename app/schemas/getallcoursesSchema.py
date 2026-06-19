from marshmallow import fields, Schema, validate
from flask_smorest.pagination import PaginationMetadataSchema

class Pagination(PaginationMetadataSchema):

    has_next=fields.Bool()
    has_prev=fields.Bool()

class GetCourseReq(Schema):

    page = fields.Int(validate=validate.Range(min=1))
    limit = fields.Int(validate=validate.Range(min=10))

class GetCoursesRes(Schema):

    data = fields.List(fields.Dict)
    metadata = fields.Nested(Pagination)