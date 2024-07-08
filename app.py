from flask import Flask
from flask_cors import CORS # type: ignore
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy # type: ignore

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a simple model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Create the database tables (if they don't exist)


# Route to handle user creation
@app.route('/user', methods=['POST'])
def create_user():
    username = request.json['username']
    new_user = User(username=username)
    db.session.add(new_user)
    db.session.commit()
    return 'User created successfully!'

# Route to list all users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return {'users': [user.username for user in users]}

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)