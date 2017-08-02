import os
from flask import Flask, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename


ALLOWED_EXTENSIONS = set(['txt', 'png', 'jpg', 'jpeg', 'mp3'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def uploaded_file(filename, upload_location):
    return send_from_directory(upload_location, filename)

def upload_file(upload_location):
    if request.method == 'POST':
    # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(upload_location, filename))
            return filename




def upload_UI(upload_location, shipment_location):
    return '''
            <!doctype html>
            <title>Upload new File</title>
            <h1>Upload new File</h1>
            <form method=post enctype=multipart/form-data>
              <p><input type=file name=file>
                 <input type=submit value=Upload>
            </form>
            ''' + str(os.path.join(upload_location))\
            +str('<br>')\
           + str(os.path.join(shipment_location))