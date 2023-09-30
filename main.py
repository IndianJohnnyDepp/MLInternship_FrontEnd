from flask import Flask,request,render_template,redirect
import os

import requests
import json

app = Flask(__name__)

app.config["IMAGE_UPLOADS"] = "./static"
from werkzeug.utils import secure_filename
from PIL import Image
import base64
import io
url = 'https://bwlwkhjj28.execute-api.ap-south-1.amazonaws.com/Production/predict-pneumonia'
filename = ''

@app.route('/home',methods = ["GET","POST"])
def upload_image():
    if request.method == "POST":
        image = request.files['file']
        
        if image.filename == '':
            print("Image must have a file name")
            return redirect(request.url)
        
        filename = secure_filename(image.filename)
        basedir = os.path.abspath(os.path.dirname(__file__))
        image.save(os.path.join(basedir,app.config["IMAGE_UPLOADS"],filename))
        img = Image.open(app.config["IMAGE_UPLOADS"] + "/" + filename)
        data = io.BytesIO()
        img.save(data,"JPEG")

        encoded_img_data = base64.b64encode(data.getvalue())

        decodedimage = base64.b64decode(encoded_img_data)
        headers = {'Content-type': 'application/x-image'}
        requestToAWS = requests.post(url, headers = headers, data=decodedimage)
        respFromAWS = requestToAWS.json()


        return render_template("main.html",result = respFromAWS)
    
    return render_template('main.html')

app.run(debug=True,port=2000)