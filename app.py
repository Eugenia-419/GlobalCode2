from flask import Flask, jsonify

app = Flask(__name__)

studentDetails =[
{
    "id": 0.01, "name": "Eugenia", "age": 21, "program": "Computer Science"
},

{
    "id": 0.02, "name": "Olivia", "age": 27, "program": "Fashion Design"
},

{
    "id": 0.03, "name": "Patience", "age": 27, "program": "Data Science"
},

{
    "id": 0.04, "name": "Eunice", "age": 22, "program": "System Analysis and Design"
},

{
    "id": 0.05, "name": "Melinda", "age": 14, "program": "Communication"
}

]


@app.route('/api/data/<int:id>', methods=['GET'])
def get_studentDetails(id):
    for i in studentDetails:
        if i['id'] == id:
            return jsonify(i)
    return jsonify({'message': 'Student not found'}), 

if __name__ == '__main__':
    app.run(debug=True)