

#######################################################
# How to serialize a dictionary with datetime objects #
#######################################################

import json
import datetime

employee = {
    "id": 456,
    "name": "William Smith",
    "salary": 8000,
    "joindate": datetime.datetime.now()
}

print("Encode DateTime Object into JSON using custom JSONEncoder")
employeeJSONData = json.dumps(employee)
print(employeeJSONData)
