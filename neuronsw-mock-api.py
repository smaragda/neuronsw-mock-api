from flask import Flask, jsonify, request

from src.model.project import Project

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Neuron Soundware inc.'


@app.route('/projects')
def get_projects():
    data = [111, 222, 333]
    return jsonify(data)


@app.route('/projects/<project_id>')
def get_one_projects(project_id):
    data = create_one_project(project_id)
    return data.toJSON()


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/Users/janmarcis/source/NEURON/neuron-flask3/upload/uploaded_file.txt')
        # f.save('uploaded_file.txt')
    return '{"status":"ok"}'


def create_one_project(project_id):
    return Project(iid=project_id,
                   iname='nejm',
                   izip_location='mezip')


if __name__ == '__main__':
    app.run()
