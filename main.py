from rest import (
    Api
)
from db import (
    DataBase
)

def main():
    db = DataBase()
    try:
        db.migrate()
        api = Api(db)
    except Exception as e:
        print ('[Error main]: {0}'.format(e))

if "__main__" == __name__:
    main()
