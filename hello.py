from flask import Flask, send_file

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/video_feed')
def video_feed():
    return send_file(r'C:\Users\smsha\Downloads\star_trails_hls.m3u8', attachment_filename="video.m3u8")


if __name__ == "__main__":
    app.run()