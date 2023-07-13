""" 
    UNIT TESTS FOR VIEWS OF PROPERTY
"""
import pytest
from werkzeug.wrappers import Request
from werkzeug.exceptions import NotFound, BadRequest

from property import get_properties

"TEST-DATA"
body_params = [
    ({"status":[3],"city": ["bogota"],"year": ["2021"]},200),
    pytest.param({"status":["3"],"city": ["bogota"],"year": [2021]},
                    400,
                    marks=pytest.mark.xfail(raises=BadRequest)),
    pytest.param({"status":[3],"city": ["derfgrg"],"year": ["5"]},
                    404,
                    marks=pytest.mark.xfail(raises=NotFound)),
    ]
"FIXTURES"
@pytest.fixture
def request_fixture(request):
    return Request(
        {
            'REQUEST_METHOD': 'POST',
            'wsgi.input': 'sample_input',
            'CONTENT_TYPE': 'application/json',
            'CONTENT_LENGTH': '100',
        }
    )

"TESTS"
@pytest.mark.parametrize("body_params, expected",body_params)
def test_get_properties(request_fixture,body_params,expected):
    request_fixture.get_json = lambda: body_params
    response = get_properties(request_fixture)

    assert response.status_code == expected

