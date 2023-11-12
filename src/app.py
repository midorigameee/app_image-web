from flask import Flask, render_template, request, url_for, redirect
import os
import sys


app = Flask(__name__, static_folder="static")
app.config["UPLOAD_FOLDER"] = "images"


@app.route('/')
def index():
    return render_template(
        "index.html"
        )


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    # URLでhttp://127.0.0.1:5000/uploadを指定したときはGETリクエストとなるのでこっち
    if request.method == 'GET':
        return render_template('upload.html')
    # formでsubmitボタンが押されるとPOSTリクエストとなるのでこっち
    elif request.method == 'POST':
        file = request.files['example']
        file.save(os.path.join('static', 'images', file.filename))
        return redirect(url_for('uploaded_file', filename=file.filename))


@app.route('/uploaded_file/<string:filename>')
def uploaded_file(filename):
    filepath = createImgPath(filename)

    print("[UPLOAD]filename : {}".format(filename))
    print("[UPLOAD]filepath : {}".format(filepath))

    return render_template(
        'uploaded_file.html',
        filename=filename,
        filepath=filepath
        )


# ./image/filenameのパスを生成するメソッド
def createImgPath(filename):
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)

    if os.name == "nt":
        filepath = converUrlForHtml(filepath)

    return filepath


# Windows環境でos.path.joinを使ってURL作成するとスラッシュがバックスラッシュになってしまうので修正するメソッド
def converUrlForHtml(url):
    return url.replace("\\", "/")


if __name__ == "__main__":
    if sys.argv[1] == "debug":
        app.run(host="0.0.0.0", debug=True)
    else:
        app.run(host="0.0.0.0", debug=False)