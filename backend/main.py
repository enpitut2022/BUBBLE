from flask import Flask, render_template
from models import get_all, init_db, insert
from makecloud import api_bp
from flask_cors import CORS

app = Flask(__name__, static_folder='../dist/img', template_folder='../dist')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myspa.db'
app.register_blueprint(api_bp)

CORS(
    app,
    supports_credentials=True
)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        init_db(app)
        if not get_all():
            insert('foo', 'This is foo.')
            insert('bar', 'This is bar.')
    app.run()