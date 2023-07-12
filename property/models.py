from enum import Enum

from toolz.dicttoolz import merge

from db import with_connection

class Status(Enum):
    PRE_VENTA = 3
    EN_VENTA = 4
    VENDIDO = 5

# UTILS: models
def add_params_to_query(params):
    status = {
        's.id': '(3,4,5)'
        if params.get('status') is None
        else f'({",".join(str(params.get("status")[0]))})'
    }
    
    city = {
        'p.city': None if params.get('city') is None 
        else f"""('{"','".join(params.get('city'))}')"""
    }
    
    year = {
        'YEAR(latest_status.max_date)': None 
        if params.get('year') is None 
        else f'({",".join(params.get("year"))})'
    }
    
    params_query = merge(status,city,year)
    return ' AND '.join(f'{k} in {v}' for k,v in params_query.items() if v is not None)

@with_connection
def get_properties_db(params: dict, *args, **kwargs) -> dict:
    conn = kwargs.pop("connection")
    cur = conn.cursor(buffered=True,dictionary=True)
    
    placeholders = add_params_to_query(params)
    
    query = f"""
            SELECT p.address, p.city, p.price, p.description, s.name AS status
            FROM property p
            INNER JOIN status_history sh ON p.id = sh.property_id
            INNER JOIN status s ON sh.status_id = s.id
            INNER JOIN (
                SELECT property_id, MAX(update_date) AS max_date
                FROM status_history
                GROUP BY property_id
            ) latest_status ON sh.property_id = latest_status.property_id AND sh.update_date = latest_status.max_date
            WHERE {placeholders};
    """
    cur.execute(query)
    
    return cur.fetchall()
