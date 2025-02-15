import csv
from io import StringIO
from flask import Response

def generator_csv(data, *, filename):
    if not data:
        return Response('No data', mimetype='text/csv')

    output = StringIO()

    if isinstance(data, dict):
        data = [data]


    keys = data[0].keys()
    writer = csv.DictWriter(output, fieldnames=keys)

    writer.writeheader()
    writer.writerows(data)

    response = Response(output.getvalue(), mimetype="text/csv")
    response.headers["Content-Disposition"] = f"attachment; filename={filename}"
    
    return response
