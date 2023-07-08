from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In-memory storage for todo items
todos = []


@app.route('/')
def index():
    return render_template('index.html', todos=todos)


@app.route('/api/todo', methods=['POST'])
def create_todo():
    todo = request.form['title']
    todos.append(todo)
    return jsonify(todo), 201


@app.route('/api/todo/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = request.form['title']
    todos[todo_id] = todo
    return jsonify(todo)


@app.route('/api/todo/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    del todos[todo_id]
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)
