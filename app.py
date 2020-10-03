from flask import Flask, render_template, request
import boto3
app = Flask(__name__)
from werkzeug.utils import secure_filename


s3 = boto3.client('s3')

BUCKET_NAME='testeflask'

@app.route('/')  
def home():
    return render_template("index2.html")

@app.route('/upload',methods=['post'])
def upload():
    if request.method == 'POST':
        img = request.files['file']
        if img:
                filename = secure_filename(img.filename)
                img.save(filename)
                s3.upload_file(
                    Bucket = BUCKET_NAME,
                    Filename=filename,
                    Key = filename
                )
                msg = "Upload realizado com sucesso!"

    return render_template("index2.html",msg =msg)


#if __name__ == "__main__":
    
app.run()
