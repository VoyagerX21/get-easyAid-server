from marshmallow import fields, Schema, validate
from flask_smorest.pagination import PaginationMetadataSchema

class Pagination(PaginationMetadataSchema):
    has_next = fields.Bool()
    has_prev = fields.Bool()

class SearchQuery(Schema):
    query = fields.Str(required=True)
    page = fields.Int(validate=validate.Range(min=1), load_default=1)
    limit = fields.Int(validate=validate.Range(min=1, max=50), load_default=10)

class SearchRes(Schema):
    success = fields.Bool()
    results = fields.List(fields.Dict)
    metadata = fields.Nested(Pagination)