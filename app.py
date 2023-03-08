from flask import Flask, render_template, Response

app = Flask(__name__)

# OpenCV로 카메라에서 영상을 읽어오는 함수
def gen_frames():
    import cv2
    cap = cv2.VideoCapture(0)
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            # 프레임에 대한 처리 (예: 이미지 회전, 필터링 등)
            # ...
            # 클라이언트로 보낼 프레임으로 인코딩된 데이터 생성
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# 카메라에서 영상을 스트리밍하는 Flask 라우트 함수
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# Flask 루트 경로에 대한 뷰 함수
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

