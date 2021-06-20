from flask import Flask, request
from flask.json import jsonify
from flask_sqlalchemy import SQLAlchemy

from  datetime import datetime
import random

import linked_list
import hastable
import binarysearchtree
import queue


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)
now = datetime.now()

class User(db.Model):
    __tablename__='user'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30))
    email = db.Column(db.String(length=50))
    address = db.Column(db.String(length=250))
    phone = db.Column(db.String(length=10))
    posts = db.relationship('Blogs', cascade="all, delete")


class Blogs(db.Model):
    __tablename__= 'blog_post'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(length=50))
    body = db.Column(db.String(length=250))
    date = db.Column(db.Date)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable = False)





@app.route('/user', methods = ["POST"])
def create_user():
    data = request.get_json()
    new_user = User(
        username = data["name"],
        email = data["email"],
        address = data["add"],
        phone = data["phone"],
    )
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"Message":"User is created"}),200

@app.route('/user/ascending', methods = ["GET"])
def arrange_ascending():
    users = User.query.all()
    user_ll = linked_list.linked_list()
    for u in users:
        user_ll.insert_end(
            {
                "id":u.id,
                "name":u.username,
                "email":u.email,
                "address":u.address,
                "phone":u.phone
            }
        )
    
    return jsonify(user_ll.to_list()),200
    

@app.route('/user/descending', methods = ["GET"])
def arrange_descending():
    users = User.query.all()
    user_ll = linked_list.linked_list()
    for u in users:
        user_ll.insert_beginning(
            {
                "id":u.id,
                "name":u.username,
                "email":u.email,
                "address":u.address,
                "phone":u.phone
            }
        )
    
    return jsonify(user_ll.to_list()),200


@app.route('/user/<user_id>', methods = ["GET"])
def get_user(user_id):
    users = User.query.all()
    user_ll = linked_list.linked_list()
    for u in users:
        user_ll.insert_beginning(
            {
                "id":u.id,
                "name":u.username,
                "email":u.email,
                "address":u.address,
                "phone":u.phone
            }
        )
    
    data = user_ll.get_data_by_id(user_id)

    return jsonify(data),200
    
    

@app.route('/user/<user_id>', methods = ["DELETE"])
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"Message":"User deleted"}), 200
    else:
        return ({"Message":"User doesnt exist, cant delete"})


@app.route('/user/<user_id>', methods = ["POST"])
def create_blog(user_id):
    
    data = request.get_json()
    user = User.query.filter_by(id=user_id).first()

    if not user:
        return jsonify({"message":"User not found"})

    h = hastable.HashTable(10)

    h.add_key("title",data["title"])
    h.add_key("body",data["body"])
    h.add_key("date",now)
    h.add_key("user",user_id)

    h.print_table()
    new_blog = Blogs(
        title = h.get_val("title"),
        body = h.get_val("body"),
        date = h.get_val("date"),
        user_id = h.get_val("user")
    )
    db.session.add(new_blog)
    db.session.commit()

    return ({"Message":"Blog added"})

@app.route('/blog_post/<blog_id>', methods = ["GET"])
def get_one_blog(blog_id):
    blogs = Blogs.query.all()
    random.shuffle(blogs)

    bst = binarysearchtree.binarysearchtree()
    
    for b in blogs:
        bst.insert(
            {
                "id":b.id,
                "title":b.title,
                "body":b.body,
                "user_id":b.user_id

            }
        )
    
    blog_id = int(blog_id)
    post = bst.search_node(blog_id)

    #print("Post is ",post)
    if not post:
        return({"Message":"Blog is not present"})
    
    return jsonify(post)

@app.route('/blog_post/numeric', methods = ["GET"])
def get_blog_numeric():
    
    posts = Blogs.query.all()
    q = queue.Queue()
    
    for p in posts:
        q.enqueue(p)

    return_list = {}
    for j in range(len(posts)):
        post = q.dequeue()

        p = {
            "id":post.id,
            "title":post.title,
            "user":post.user_id

        }

        return_list[j]=p

    return return_list        

if __name__ == "__main__":
    app.run(debug=True)

