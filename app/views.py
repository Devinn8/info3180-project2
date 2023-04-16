"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, jsonify, send_file, url_for, send_from_directory
import os
from app.models import Movies
from app.forms import MovieForm
from werkzeug.utils import secure_filename
from flask_wtf.csrf import generate_csrf
import datetime


###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")

@app.route('/api/v1/movies', methods=['GET','POST'])
def movies():
    if request.method == 'GET':
        movies = db.session.execute(db.select(Movies)).scalars()
        print(movies)
        movie_list =[]
        for movie in movies:
            movie_list.append(
            {
                "id": movie.id,
                "title": movie.title,   
                "description": movie.description,
                "poster": url_for('get_image', filename=movie.poster)
            }
        )
        print(movie_list)
        return jsonify(movies=movie_list)
    
    form = MovieForm()
    if form.validate_on_submit():
        title = request.form['title']
        description = request.form['description']
        file = request.files['poster']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        newmovie = Movies(title, description, filename, created_at=datetime.datetime.now())
        db.session.add(newmovie)
        db.session.commit()

        response = jsonify({
            'message': 'Movie successfully added',
            'title': newmovie.title,
            'poster': filename,
            'description': newmovie.description
        })
        response.status_code = 201
        return response
    else:
        response = jsonify({'errors': form_errors(form)})
        #response.status_code = 400
        return response

@app.route('/api/v1/csrf-token', methods=['GET']) 
def get_csrf():     
    return jsonify({'csrf_token': generate_csrf()}) 

@app.route("/api/v1/posters/<filename>")
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
    return render_template('404.html'), 404