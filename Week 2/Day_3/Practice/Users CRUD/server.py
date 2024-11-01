from flask import Flask, render_template, Request, redirect
from friend import Friend

app = Flask(__name__)

@app.route('/')
def index():
    friends = Friend.get_all()
    return render_template("index.html", friends=friends)


@app.route('/users/new')
def new_user():
    return render_template('new_friend.html')

@app.route('/friends/create', methods=['POST'])
def create_user(friend_id):
    friend=Friend.get_one(friend_id)
    return render_template("show_friend.html",friend=friend)

@app.route('/friends/<int:friend_id>')
def show_user(friend_id):
    friend = Friend.get_one(friend_id)
    return render_template('show_user.html', friend = friend)

@app.route('/friends/<int:friend_id>/edit')
def edit_user(friend_id):
    friend = Friend.get_one(friend_id)
    return render_template('edit_user.html', friend = friend)


@app.route('/friends/<int:friend_id>/edit', methods=['POST'])
def update_user(friend_id):
    data = {
        "id": friend_id,
        "first_name": Request.form['first_name'],
        "last_name": Request.form['last_name'],
        "email": Request.form['email']
    }
    Friend.update(data)
    return redirect('/users/{friend_id}')

@app.route('/friends/delete/<int:friend_id>')
def delete_user(friend_id):
    Friend.delete(friend_id)
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)