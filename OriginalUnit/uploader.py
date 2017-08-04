import os
from flask import request, redirect, flash, send_from_directory
from werkzeug.utils import secure_filename


ALLOWED_EXTENSIONS = set(['txt', 'png', 'jpg', 'jpeg', 'mp3'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def uploaded_file(filename, upload_location):
    return send_from_directory(upload_location, filename)

def upload_file(upload_location, file_key):
    if request.method == 'POST':
    # check if the post request has the file part
        if file_key not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files[file_key]
        # if user does not select file, browser also
        if file.filename == '':         # 파일 이름체크
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(upload_location, filename))
            return filename

def upload_file_arrays(upload_location, array_name):
    # check if the post request has the file part
        if array_name not in request.files:
            flash('No file part')
            return redirect(request.url)
        files = request.files.getlist(array_name)
        # if user does not select file, browser also
        for file in files:
            if file.filename == '':         # 파일 이름체크
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(upload_location, filename))

        return files


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