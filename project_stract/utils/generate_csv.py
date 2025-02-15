import csv
from io import StringIO
from flask import Response

def generator_csv(data, *, filename):
    if not data:
        return Response('No data', mimetype='text/csv')

    output = StringIO(newline='')

    if isinstance(data, dict):
        data = [data]


    keys = data[0].keys()
    writer = csv.DictWriter(output, fieldnames=keys)

    writer.writeheader()
    writer.writerows(data)

    response = Response(output.getvalue().encode('utf-8-sig'), mimetype="text/csv")
    response.headers["Content-Disposition"] = f"attachment; filename={filename}"
    response.headers["Content-Type"] = "text/csv; charset=utf-8"
    
    return response
