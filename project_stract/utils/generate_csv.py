import csv
from io import StringIO
from flask import Response

def generator_csv(data, *,filename):
    if not data:
        return Response('No data', mimetype='text/csv')
    
    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=data.keys())

    writer.writeheader()
    writer.writerow(data)

    response = Response(output.getvalue(), mimetype="text/csv")
    response.headers["Content-Disposition"] = f"attachment; filename={filename}"

    return response
