import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR,'pybo.db'))#데이터베이스 접속 주소
SQLALCHEMY_TRACK_MODIFICATIONS = False #sqlalchemy의 이벤트를 처리하는 옵션 설정
# "pybo.db" 라는 데이터베이스 파일을 프로젝트의 루트 리렉터리에 저장하려고 하는거임ㅇㅇ