#Flask 모듈 가져오기
from flask import Flask

#Flask 객체 생성
app=Flask( __name__)

# HTTP GET 매핑 설정
@app.route('/')
def index() : # 매핑 함수
    return 'Hello Flask'

#Flask 프레임워크 실행
if __name__ == '__main__':
    app.run(debug=True)

