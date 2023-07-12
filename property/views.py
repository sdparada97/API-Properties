
import json
import jsonschema
from werkzeug.wrappers import Request, Response
from werkzeug.exceptions import HTTPException, NotFound, BadRequest

from property import get_properties_db


# ENDPOINTS
def get_properties(request: Request):
    with open('property/schemas/property_request.json') as schema_file:
        schema = json.load(schema_file)
    body_params = request.get_json()

    try:
        jsonschema.validate(body_params,schema)
        properties = get_properties_db(body_params)
        
        if len(properties) == 0:
            raise NotFound()
        
        properties_json = json.dumps(properties, ensure_ascii=False)
        return Response(properties_json, mimetype='application/json')
    except NotFound as e:
        raise NotFound(description='Properties not found') from e
    except jsonschema.ValidationError as e:
        raise BadRequest(description='The input was not valid') from e
    except HTTPException as e:
        return e



