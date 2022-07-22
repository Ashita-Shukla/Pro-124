from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {
    'Name': u'Raju',
    'id': 1,
    'Contact': 9987644456,
    'done': False
    }, 
    {
    'Name': u'Rahul',
    'id': 2,
    'Contact': 9987644487,
    'done': False
}]

@app.route("/add-data", methods=["POST"])
def contact():
    if not request.json:
        return jsonify({
            "status": "error",
            "message":"please, provide the data"
        }, 400)
    task = {
        'id': tasks[-1]['id']+1,
        'name': request.json['Name'],
        'contact': request.json.get['Contact', ""]
    }

    tasks.append(task)
    return jsonify({
        'status':'success',
        'message':'task added successfully'
    })

@app.route('/get-data')
def get_task():
    return jsonify({
        "data": tasks
    })

if(__name__ == "__main__"):
    app.run(debug = True)