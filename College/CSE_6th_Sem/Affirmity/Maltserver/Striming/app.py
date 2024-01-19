from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

video_paths = [
    'C://Users//deepa//Desktop//Maltserver//Striming//Videoes//video1.mp4',
    'C://Users//deepa//Desktop//Maltserver//Striming//Videoes//video2.mp4',
    'C://Users//deepa//Desktop//Maltserver//Striming//Videoes//video3.mp4',
    'C://Users//deepa//Desktop//Maltserver//Striming//Videoes//video4.mp4',
    'C://Users//deepa//Desktop//Maltserver//Striming//Videoes//video5.mp4'
]

cameras = [cv2.VideoCapture(path) for path in video_paths]
print(cameras)

def generate_frames(camera_id):
    camera = cameras[camera_id]
    while True:
        success, frame = camera.read()
        if not success:
            camera.set(cv2.CAP_PROP_POS_FRAMES, 0)
            success, frame = camera.read()
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video/<int:id>')
def video(id):
    return Response(generate_frames(id), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)






















# from flask import Flask, render_template
# import threading

# app = Flask(__name__)

# def run_server(port):
#     app.run(host='0.0.0.0', port=port)

# @app.route('/')
# def index():
#     return render_template('index.html')

# if __name__ == '__main__':
#     main_port = 5000
    
#     # Start the main Flask server
#     thread_main = threading.Thread(target=run_server, args=(main_port,))
#     thread_main.start()
    
#     # Start additional Flask servers on different ports
#     for i in range(1, 6):  # Create 5 additional servers
#         sub_port = main_port + i
#         thread = threading.Thread(target=run_server, args=(sub_port,))
#         thread.start()



















# from flask import Flask, Response, render_template
# import cv2
# import threading

# app = Flask(__name__)

# CAMERA_FEEDS = list(range(55))

# def generate_frames(camera_index):
#     # ... Your video feed generation logic ...
#     cap = cv2.VideoCapture(camera_index)

#     while True:
#         success, frame = cap.read()
#         if not success:
#             break
#         _, buffer = cv2.imencode('.jpg', frame)
#         frame = buffer.tobytes()
#         yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

#     cap.release()

# def run_server(port):
#     app.run(host='0.0.0.0', port=port)

# @app.route('/')
# def index():
#     return render_template('index.html', num_cameras=len(CAMERA_FEEDS))

# @app.route('/video_feed/<int:camera_index>')
# def video_feed(camera_index):
#     return Response(generate_frames(camera_index),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')

# if __name__ == '__main__':
#     if len(CAMERA_FEEDS) <= 5:
#         app.run(debug=True)
#     else:
#         main_port = 5000
#         for i in range(0, len(CAMERA_FEEDS), 5):
#             sub_cameras = CAMERA_FEEDS[i:i+5]
#             sub_app = Flask(__name__)

#             for camera_index in sub_cameras:
#                 sub_app.add_url_rule(
#                     f'/video_feed/{camera_index}',
#                     view_func=video_feed,
#                     endpoint=f'video_feed_{camera_index}'
#                 )

#             thread = threading.Thread(target=run_server, args=(main_port,))
#             thread.start()
#             main_port += 1



























# from flask import Flask, Response, render_template , request, url_for
# import cv2

# app = Flask(__name__)

# CAMERA_FEEDS = [0,1,2,3,4,5,6,7 ]

# @app.route('/')
# def index():
#     return render_template('index.html', num_cameras=len(CAMERA_FEEDS))

# def generate_frames(camera_index):
#     cap = cv2.VideoCapture(camera_index)

#     while True:
#         success, frame = cap.read()
#         if not success:
#             break
#         _, buffer = cv2.imencode('.jpg', frame)
#         frame = buffer.tobytes()
#         yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

#     cap.release()

# @app.route('/video_feed/<int:camera_index>')
# def video_feed(camera_index):
#     return Response(generate_frames(camera_index),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')

# # import Detect



# if __name__ == '__main__':
#     app.run(debug=True)