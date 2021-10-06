from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config

#전역 변수로 만들어 객체로 만듬
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config) #app.config를 환경 변수로 부르기 위해서추가함

    # ORM  create_app함수 안에서 전역변수 초기화 해주기
    db.init_app(app)
    migrate.init_app(app,db)
    from . import models

    # 블루 프린트
    from.views import main_views, question_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)

    return app
