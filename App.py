from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# import FCMManager as fcm
from create_table import create_tables
import os

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://test_db_uodg_user:xLjrLk3HhNOZSdn2DZa2jFznzRqEfxO5@dpg-ce3cl3la4999gmei5i9g-a.oregon-postgres.render.com/test_db_uodg"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app) 

create_tables()

class Testdb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    u_id = db.Column(db.Integer)
    d_token = db.Column(db.String(1000))

    def __init__(self, u_id, d_token):
        self.u_id = u_id
        self.d_token = d_token


class PostSchema(ma.Schema):
    class Meta:
        fields = ("u_id", "d_token")

post_schema = PostSchema()
posts_schema = PostSchema(many=True)


@app.route('/post', methods=['POST'])
def add_post():
    print("inside route")
    u_id = request.json['u_id']
    print("u_id", u_id)
    # u_id = 10
    d_token = request.json['d_token']
    # fcm.sendPush("Hi", "This is my next msg", [d_token])
    print("d_token=", d_token)
    # d_token = "test data"
    my_posts = Testdb(u_id, d_token)
    db.session.add(my_posts)
    db.session.commit()
    return post_schema.jsonify(my_posts)
    # return 1


if __name__ == "__main__":
    app.run(debug=True)
    # sendPushNotification()