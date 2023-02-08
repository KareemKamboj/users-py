from Flask_app import app
from flask import render_template, request, session, redirect
from Flask_app.models.users_model import Users

@app.route('/')
def index():
    all_users = Users.get_all()
    print(f"this is all users: {all_users}")
    return render_template('index.html', all_users = all_users)

@app.route('/users/<int:id>')
def one_user(id):
    one_user = Users.get_one({'id':id})
    return render_template('read_one.html', one_user=one_user)

@app.route('/users/new')
def add_user():
    return render_template('add_user.html')

@app.route('/users/create', methods = ['POST'])
def create_user():
    id = Users.create(request.form)
    return redirect(f'/users/{id}')

@app.route('/users/<int:id>/edit')
def edit_user_form(id):
    data = {
        'id' : id
    }
    this_user = Users.get_one(data)
    return render_template('user_edit.html', this_user=this_user)

@app.route('/users/<int:id>/update', methods=['POST'])
def update_user(id):
    data = {
        **request.form,
        'id':id 
    }
    Users.update(data)
    return redirect('/')

@app.route('/users/<int:id>/delete')
def delete_user(id):
    data = {
        'id':id
    }
    Users.delete(data)
    return redirect('/')

