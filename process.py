import sys
from config import db_details
from util import get_tables

def process():
    env=sys.argv[1]
    db_detail=db_details[env]
    tables=get_tables('tables_list')
    # for table in tables['table_name']:
    #     print(table)






if __name__=='__main__':
    process()