from pybo import db

class Question(db.Model): #class "Question"은 모든 모델의 기본 클래스인 db.Model을 상속받음 db = init 파일에서 생성한 sqlalcemy 객체
    id = db.Column(db.Integer,primary_key=True) #db.Column() <-- 안에 데이터 타입을 의미
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(),nullable=False)
    create_date = db.Column(db.DateTime(),nullable=False)
    #db.Integer는 숫자값에 사용
    #db.String 은 글자
    #db.Text 글자수를 제한할 수 없는 텍스트 
    #db.DateTime = 날짜와 시각에 해당함 
    # primary key 중복되면 안되는 값
    # nullable 빈값을 허용할 것인지
class Answer(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete = 'CASCADE'))
    question = db.relationship('Question', backref = db.backref('answer_set'))
    content = db.Column(db.Text(),nullable=False)
    create_date = db.Column(db.DateTime(),nullable=False)
    #question_id 속성은 질문 모델과 연결하려고 추가했다. 
    #답변 모델 데이터는 어떤 질문에 대한 답변인지 알아야 하므로 
    #2단계에서 생성한 질문 모델과 연결된 속성을 포함해야 한다. 
    #이처럼 어떤 속성을 기존 모델과 연결하려면 db.ForeignKey를 사용해야 한다

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique = True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    #unique = True 같은 값을 저장할 수 없다