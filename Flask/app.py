from flask import Flask, request

app = Flask(__name__)  # http://127.0.0.1:5000

@app.route('/home')  # http://127.0.0.1:5000/home
def home():
    return "You are on the HOME page."


@app.route('/me')
def user_page():
    return "User Profile Page"


# @app.route('/<string:username>/<string:password>/<string:email>', methods=['POST'])
# @app.route('/registrate', methods=['POST'])
# def post_request2():
#     data = request.json
#     username = data['username']
#     password = data['password']
#     email = data['email']
#     return f"Username: {username}\nPassword: {password}\nEmail: {email}"



@app.route('/registrate', methods=['POST'])
def post_request():
    # username= request.form['username']
    # password = request.form['password']
    # email = request.form['email']
    data = request.json
    username = data['username']
    password = data['password']
    email = data['email']
    return f"Username: {username}\nPassword: {"*" * len(password)}\nEmail: {email}"

@app.route('/user-by-id/<int:user_id>')
def get_user_by_id(user_id):
    return f"User by ID {user_id}"


if __name__ == "__main__":
    app.run(debug=True)
