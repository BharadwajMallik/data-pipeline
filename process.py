import sys
from util import get_tables,load_db_details
from read import read_table

def process():
    env=sys.argv[1]
    db_details=load_db_details(env)
    tables=get_tables('tables_list')
    for table in tables['table_name']:
        print(f'reading data for {table}')
        data,column_names=read_table(db_details,table)
        print(f'loading data for {table}')

    for rec in data:
        print(rec)






if __name__=='__main__':
    process()