import torch
from IPython.display import Image, clear_output  # to display images
import os
import cv2
from flask import Flask, redirect, url_for, request, render_template


app = Flask(__name__)
# routes
@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")


@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
    if request.method == 'POST':
        img = request.files['my_image']
        img_path = "static/" + img.filename
        img.save("static/im2.jpg")

        #cv2.imwrite('img1.jpg', image)


        command = "python yolov5/detect.py --weights yolov5/best.pt --img 416 --conf 0.4 --source static/im2.jpg"
        os.system(command)

        p='hi'

    return render_template("index.html", prediction = p, img_path = img_path)




#@app.route('/predict', methods=['POST'])
#def home():
#return render_template('video.html')



if __name__ == "__main__":
    app.run(debug=True)