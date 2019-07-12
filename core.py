import json
import uuid
import datetime
from models import (
    Lote,
    Item,
    LoteItemInsert
)

class App:
    db = None

    def __init__(self, db):
        self.db = db

    def create(self, params):
        SchemaLote = Lote()
        SchemaItem = Item()
        LoItInsert = LoteItemInsert()
        id_lote    = str(uuid.uuid1())
        created    = datetime.datetime.now().__str__()
        lote       =  params.get('lote', None)
        lote.update({'id': id_lote})
        lote.update({'created': created})
        try:
            lote_obj   = SchemaLote.loads(json.dumps(lote))
            items      = params.get('items', None)
            items_list = []
            items_ok   = 0
            items_er   = 0
            for item in items:
                try:
                    id_item    = str(uuid.uuid1())
                    item.update({'id': id_item})
                    item.update({'id_lote': id_lote})
                    item.update({'created': created})
                    items_list.append( SchemaItem.loads(json.dumps(item)) )
                    items_ok += 1
                except Exception as e:
                    msg = '[Error App.create.items] {0}'.format(e)
                    print (msg)
                    items_er += 1
            insert = LoItInsert.loads(json.dumps({ 'lote': lote_obj, 'items': items_list }))
            self.db.register(insert)
            return [{
                'id_lote': id_lote,
                'items_ok': items_ok,
                'items_er': items_er
            }, 200]
        except Exception as e:
            msg = '[Error App.create.lote] {0}'.format(e)
            print (msg)
            return [msg, 400]
