from marshmallow import (
    Schema,
    fields
)

class Lote(Schema):
    id       = fields.Str(required=True)
    email    = fields.Str(required=True)
    password = fields.Str(required=True)
    subject  = fields.Str(required=True)
    template = fields.Str(required=True)
    created  = fields.Str(required=True)

class Item(Schema):
    id         = fields.Str(required=True)
    id_contact = fields.Str(required=True)
    email      = fields.Str(required=True)
    id_lote    = fields.Str(required=True)
    created   = fields.Str(required=True)

class LoteItemInsert(Schema):
    lote  = fields.Nested(Lote)
    items = fields.List(fields.Nested(Item), required=True)
