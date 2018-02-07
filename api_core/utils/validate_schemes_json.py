from jsonschema import validate
from jsonschema.exceptions import ValidationError
import json




def validate_schema(json_meeting, schema ):
    schema_ = json.loads(open('test/schemes/'+schema+'.json.').read())
    try:
        validate(json_meeting, schema_)
        return True
    except ValidationError:
        return False

