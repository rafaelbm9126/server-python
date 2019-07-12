from sqlite3 import (
    connect
)

class DataBase:
    conn = None

    def __init__(self):
        self.conn = connect('db.sqlite3')

    def migrate(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS
                sh_lote (
                    id VARCHAR(50) PRIMARY KEY,
                    email VARCHAR(80) NOT NULL,
                    password VARCHAR(100) NOT NULL,
                    subject VARCHAR(200) NOT NULL,
                    template TEXT NOT NULL,
                    created TIMESTAMP NOT NULL
                )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS
                sh_item (
                    id VARCHAR(50) PRIMARY KEY,
                    id_contact VARCHAR(50) NOT NULL,
                    id_lote VARCHAR(50) NOT NULL,
                    email VARCHAR(80) NOT NULL,
                    created TIMESTAMP NOT NULL,
                    FOREIGN KEY(id_lote) REFERENCES sh_lote(id)
                )
        ''')
        self.conn.commit()
        cursor.close()

    def register(self, insert):
        if (self.conn != None):
            cursor = self.conn.cursor()
            lote   = insert.get('lote', {})
            keys_insert = [ v for v in lote.keys() ]
            values_insert = [ v for v in lote.values() ]
            cursor.execute('''
                INSERT INTO
                sh_lote %s
                VALUES %s
            ''' % (tuple(keys_insert), tuple(values_insert)))
            for item in insert.get('items', []):
                keys_insert = [ v for v in item.keys() ]
                values_insert = [ v for v in item.values() ]
                cursor.execute('''
                    INSERT INTO
                    sh_item %s
                    VALUES %s
                ''' % (tuple(keys_insert), tuple(values_insert)))
            self.conn.commit()
            cursor.close()
        else:
            raise Exception('[Error register.connection]')
