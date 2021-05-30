from util import get_connection

def build_insert_query(table_name,column_names):

    query=(f'Insert into {table_name} {column_names} values (%s,%s)')
    return query



def insert_data(connection,cursor,query,data,batch_size=100):

