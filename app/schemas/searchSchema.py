from marshmallow import fields, Schema

class SearchQuery(Schema):

    query=fields.Str()

class SearchRes(Schema):

    success=fields.Bool()
    results=fields.List(fields.Dict)