from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.show import Show
from flask_app.models.user import User

@app.route('/new/show')
def new_show():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('new_show.html',user=User.get_user_by_this_id(data))

@app.route('/create/show',methods=['POST'])
def create_show():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Show.validate_show(request.form):
        return redirect('/new/show')
    data = {
        "title": request.form["title"],
        "network": request.form["network"],
        "release_date": request.form["release_date"],
        "description": request.form["description"],
        "user_id": request.form["id"]
    }
    Show.save(data)
    return redirect('/dashboard')

@app.route('/edit/show/<int:show_id>')
def edit_show(show_id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "show_id": show_id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit_show.html",one_show=Show.get_one_show(data),user=User.get_user_by_this_id(user_data))

@app.route('/update/show',methods=['POST'])
def update_show():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Show.validate_show(request.form):
        return redirect('/new/show')
    data = {
        "title": request.form["title"],
        "network": request.form["network"],
        "release_date": request.form["release_date"],
        "description": request.form["description"],
        "show_id": request.form["show_id"]
    }
    print(data)
    Show.update_show(data)
    return redirect('/dashboard')


@app.route('/destroy/show/<int:show_id>')
def destroy_show(show_id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "show_id":show_id
    }
    Show.destroy(data)
    return redirect('/dashboard')