import json
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from iris_model.predict import make_prediction

def handler(event, context):
    print("started prediction for the iris parameters in event : ", event)
    result = make_prediction(input_data=event)
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(result)
    }
