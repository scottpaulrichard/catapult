from flask import Flask
from catapult import catapult
from jinja2 import Environment

HTML = """
<html>
<head>
<title>catapult</title>
</head>
<body>
<h1>Catapult</h1>
<h2>Cost: {{cost}} USD</h2>
<table style="text-align:center;">
<tr>
<th>Bucket Name</th>
<th>Creation Date (UTC)</th>
<th>Num Files</th>
<th>Total Size(Bytes)</th>
<th>Last Modified (UTC)</th>
</tr>
{% for item in items %}
<tr>
<td>{{item.BucketName}}</td>
<td>{{item.CreationDate}}</td>
<td>{{item.NumFiles}}</td>
<td>{{item.TotalSize}}</td>
<td>{{item.LastModifiedDate}}</td>
</tr>
{% endfor %}
</table>
</body>
</html>
"""

app = Flask(__name__)

@app.route('/')
def index():
    cost,rows = catapult()
    return Environment().from_string(HTML).render(items=rows,cost=cost)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
