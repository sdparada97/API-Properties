""" 
    UNIT TESTS FOR MODELS OF PROPERTY
"""
import pytest
import mysql.connector

from property import get_properties_db, Status, add_params_to_query
from db import config

"TEST-DATA"
property_filters_data = [
        ({},0),
        ({'status':[Status.EN_VENTA.value],},0),
        ({'city':['bogota'],},0),
        ({'year': ['2021'],},0),
        ({
            'status':[Status.EN_VENTA.value],
            'city':['bogota'],
            'year': ['2021']
        },0)
]

"FIXTURES"
@pytest.fixture(scope='session')
def mysql_connection():
    connection = mysql.connector.connect(**config)
    
    yield connection
    
    connection.close()

@pytest.fixture(scope='session')
def mysql_cursor():
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    
    yield cursor
    
    cursor.close()
    connection.close()


"TESTS"
def test_mysql_connection(mysql_connection):
    assert mysql_connection.is_connected() == True

def test_add_params_to_query():
    params = {
        'status': [3],
        'city': ['bogota','pereira'],
        'year': ['2021', '2022']
    }
    expected_result = "s.id in (3) AND p.city in ('bogota','pereira') AND YEAR(latest_status.max_date) in (2021,2022)"
    assert add_params_to_query(params) == expected_result

@pytest.mark.parametrize("params, expected",property_filters_data)
def test_get_properties(params, expected):
    """ 
    *   Debe de devolver las propiedades con los inmuebles 
        con un status en especifico.
    *   Debe de devolver las propiedades con los inmuebles
        con una ciudad especifica.
    *   Debe de devolver las propiedades con los inmuebles
        con un año especifico.
    *   Debe de devolver las propiedades con los inmuebles
        con todos los filtros.
    *   Debe de devolver las propiedades con los inmuebles
        sin filtros.
    """
    result = get_properties_db(params)
    print(result)
    assert len(result) > expected 