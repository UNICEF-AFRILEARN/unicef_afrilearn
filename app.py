import json
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS
from recommender import recommend

base_html = """ 
<!doctype html> 
<html><head> <meta http-equiv="Content-type" content="text/html; charset=utf-8"> 
<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.2/jquery.min.js"></script>
<link rel="stylcd documeesheet" type="text/css" href="https://cdn.datatables.net/1.10.16/css/jquery.dataTables.css">
<script type="text/javascript" src="https://cdn.datatables.net/1.10.16/js/jquery.dataTables.js"></script>
</head><body>%s<script type="text/javascript">$(document).ready(function(){$('table').DataTable({
    "pageLength": 10
});});</script>
</body></html>
"""

app = Flask(__name__)
CORS(app, resources={r"*":{"origins":"*"}})

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/<school_level>/<subject>/<lesson>', methods=['GET'])
def reco(school_level,subject,lesson):
    if (school_level == '') or (subject == '') or (lesson == ''):
            return render_template('index.html', message='Please enter required fields')
    else:
        df = recommend(school_level, subject, lesson)
        return df.to_json(orient='records')

@app.route('/recommend', methods=['GET','POST'])
def reco_system():
    if request.method == 'GET':
        return jsonify({"response":"Get Request Called"})
    else:
        data = request.get_json()
        schoollevel = data['schoollevel']
        subject = data['subject']
        lesson = data['lesson']
        df = recommend(schoollevel, subject, lesson)
        return df.to_json(orient='records')

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST' or request.method == 'GET':
        school_level = request.form['school_level']
        subject = request.form['subject']
        lesson = request.form['lesson']
        if (school_level == '') or (subject == '') or (lesson == ''):
            return render_template('index.html', message='Please enter required fields')
        else:
            df = recommend(school_level, subject, lesson)
            return render_template('results.html', tables=[base_html % df.to_html(classes='data')], header="true")
    else:
        return render_template('index.html', message='Please enter required fields')


if __name__ == '__main__':
    app.debug = False
    app.run()