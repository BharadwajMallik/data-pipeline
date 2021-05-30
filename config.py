import os

db_details={
    'dev':{
        'souce_db':{
            'db_type':'mysql',
            'db_host': '35.223.234.242',
            'db_name':'retail_db',
            'db_user':os.environ.get('source_db_user'),
            'db_password': os.environ.get('source_db_pass')
        },
        'target_db': {
            'db_type': 'postgres',
            'db_host': '35.223.234.242',
            'db_password': os.environ.get('target_db_user'),
            'db_name': 'retail_db',
            'db_user': os.environ.get('target_db_pass')
        }
    }
}