from flask import Flask, render_template, request, send_file, redirect, url_for
from io import BytesIO
from pytube import YouTube

app = Flask(__name__)
app.secret_key = '1JM(g/hIyi#sg_adNf>/_&SVC!v.ZOR,},nBs!n~;9u$}|}?0c7'

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/download', methods = ["GET", "POST"])
def download():
    if request.method =='POST':
        buffer = BytesIO()
        urlyt = request.form.get('url')
        yt = YouTube(urlyt)
        stream = yt.streams.get_by_itag(22)
        stream.stream_to_buffer(buffer)
        buffer.seek(0)
        return send_file(buffer, as_attachment=True, download_name="Video - {yt.title}", mimetype="video/mp4")
    return redirect(url_for('home'))

if __name__ =='__main__':
    app.run(threaded =True)
    