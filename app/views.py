"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from crypt import methods
import os
import jwt
from app import app, db, login_manager
from flask import request, jsonify, session, send_file, send_from_directory
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import LoginForm, RegistrationForm, AddNewPostForm
from app.middleware import requires_auth
from app.models import Users, Posts, Likes, Follows
from flask_wtf.csrf import generate_csrf
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta


###
# Routing for your application.
###
@login_manager.user_loader
def user_loader(user_id):
    """Given *user_id*, return the associated User object.
    :param unicode user_id: user_id (email) user to retrieve
    """
    return Users.query.get(user_id)

@app.route('/')
def index():
 return send_file(os.path.join('../dist/', 'index.html'))

####Accepts user information and saves it to the database
@app.route('/api/v1/register', methods = ['POST'])
def register():
    try:
        form = RegistrationForm()
        if request.method == "POST" and form.validate_on_submit():
            
            check_username = Users.query.filter_by(username=form.username.data).first()
            check_email = Users.query.filter_by(email=form.email.data).first()
            
            if check_username is not None or check_email is not None:
                return jsonify({
                    "errors": ["User is in the system"]
                }), 401


            username = form.username.data
            password = form.password.data
            firstname =  form.firstname.data
            lastname =  form.lastname.data
            email = form.email.data
            location = form.location.data
            biography = form.biography.data
            upload = form.photo.data
            filename = secure_filename(upload.filename)
            joined_on= datetime.now()
            
            user = Users(username, password, firstname, lastname, email, location, biography, filename, joined_on)
            db.session.add(user)
            db.session.commit()
            upload.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            return jsonify({
                'id': user.id,
                'username': username,
                'firstname': firstname,
                'lastname' : lastname,
                'photo': filename,
                'email': email,
                'location': location,
                'biography': biography,
                'joined_on': user.joined_on
            }), 201
        return jsonify(errors=form_errors(form)), 401
    except:
        return jsonify({ "errors": form.errors}), 500


####Accepts login credentials as username and password
@app.route("/api/v1/auth/login", methods=["POST"])###Revisit
def login():
    form = LoginForm()

    if request.method == "POST" and form.validate_on_submit():
        # Get the username and password values from the form.
        username = form.username.data
        password = form.password.data

        # This queries database for a user based on the username
        # and password submitted.
        user = Users.query.filter_by(username=username).first()

        # Compares the submited password and username to the hash password and
        # username in the database.
        if user is not None and check_password_hash(user.password, password):
            session['logged_in'] = True

            #Creates the token for the user currently logging in
            payload = {
                'sub': user.id, # subject, usually a unique identifier
                'user': username,
                'iat': datetime.utcnow(),# issued at time
                'exp': datetime.utcnow() + timedelta(hours=2) # expiration time
            }

            token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
            login_user(user)

            return jsonify(
                { 
                    "token": token , 
                    "message": "Login Successfully",
                    "id": user.id
                }), 200
        return jsonify(
                { 
                    "errors": ['Invalid credentials']
                }), 401
    
    return jsonify(errors=form_errors(form)), 401

#### Logout a user
@app.route('/api/v1/auth/logout', methods=["POST"])
@login_required
@requires_auth
def logout():
    logout_user()

    return jsonify({
        "message": "Log out successful"
    }), 200



####Used for adding posts to the users feed
@app.route('/api/v1/users/<user_id>/posts', methods=['POST'])
def addNewPost(user_id):
    try:
        # Get the user from the database
        user = Users.query.filter_by(id=user_id).first()

        if not user:
            return jsonify({"error": "User not found"}), 404

        # Create an instance of the AddNewPostForm
        form = AddNewPostForm()

        # Check if the request contains form data and the form is valid
        if request.method == 'POST' and form.validate_on_submit():
            # Save the uploaded photo to the server
            photo_filename = secure_filename(form.photo.data.filename)
            photo_path = os.path.join(app.config['UPLOAD_FOLDER'], photo_filename)
            form.photo.data.save(photo_path)

            # Create a new post object with the form data
            new_post = Posts(
                user_id=user.id,
                photo=photo_filename,
                caption=form.caption.data,
                created_on=datetime.utcnow()
            )

            # Add the post to the database
            db.session.add(new_post)
            db.session.commit()

            # Return a success message
            return jsonify({"message": "Post added successfully"}), 201

        # Return form validation errors if the form is invalid
        return jsonify({"errors": form.errors}), 400

    except Exception as e:
        return jsonify({"errors": str(e)}), 500




####Returns a user's posts
@app.route('/api/v1/users/<user_id>/posts', methods =['GET'])##Revisit
@login_required
@requires_auth
def getUserPost(user_id):
    try:
        if request.method == 'GET':
            users = Users.query.filter_by(id=user_id).all()

            data = []
            for user in users:
                user_data = {
                    'id': user.id,
                    'username': user.username,
                    'name': user.name,
                    'photo': user.photo,
                    'email': user.email,
                    'location': user.location,
                    'biography': user.biography,
                    'date_joined': user.date_joined
                }
                data.append(user_data)

            return jsonify(data), 200
    except Exception as e:
        return jsonify({"errors": e}), 401



###Create a Follow relationship between the current user and the target user.
@app.route('/api/v1/users/<user_id>/follow', methods=['POST'])
@login_required
@requires_auth
def follow(user_id):
    try:
        # Check if the user exists
        user = Users.query.filter_by(id=user_id).first()
        if user is None:
            return jsonify({'error': 'User not found'}), 404

        # Add the follower and user to the Follows table
        follow = Follows(follower_id=current_user.id, user_id=user_id)
        db.session.add(follow)
        db.session.commit()

        return jsonify({'message': 'You are now following {}!'.format(user.username)}), 200
    except:
        return jsonify({'error': 'Unable to follow user'}), 500


####Returns all the posts for all users
@app.route('/api/v1/posts', methods=['GET'])
@login_required
@requires_auth
def getPosts():
    try:
        if request.method == "GET":
            #Retrieve data from the database
            posts = db.session.query(Posts).all()
            
            data = []
            
            for post in posts:
                user = Users.query.get(post.user_id)
                likes = Likes.query.get(post.id) ###Revisit 
                data.append ({
                    'id': post.id,
                    'caption': post.caption,
                    'photo': post.photo,
                    'username' : user.username,
                    'profile_photo' : user.profile_photo,
                    'created_on' : post.created_on,
                    'num_likes': len(likes)
                    
                })
            return jsonify (data=data), 200 
    except:
        return jsonify({"errors": "Request Failed"}), 401



###Set a like on the current Post by the logged in User
@app.route('/api/v1/posts/<post_id>/like', methods=['POST'])
@login_required
@requires_auth
def follow(post_id):
    try:
        # Check if the posts exists
        post = Posts.query.filter_by(id=post_id).first()
        if post is None:
            return jsonify({'error': 'Post not found'}), 404

        # Add the like and user to the Likes table
        like = Likes(follower_id=current_user.id, post_id=post_id)
        db.session.add(like)
        db.session.commit()

        return jsonify({'message': 'You liked a post {}!'.format(post.user_id)}), 200
    except:
        return jsonify({'error': 'Unable to like the post'}), 500




@app.route('/api/csrf-token', methods=['GET'])
def get_csrf():
    return jsonify({'csrf_token': generate_csrf()})

"""
    ROUTE to retrieve images from upload folder
"""
@app.route('/uploads/<filename>')
def get_image(filename):
    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)

###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return jsonify(error="Page Not Found"), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")