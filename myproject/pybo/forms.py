from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class QuestionForm(FlaskForm):
    subject = StringField('제목',validators=[DataRequired('제목을 입력해주세용')]) #글자수 제한있음
    content = TextAreaField('내용',validators=[DataRequired('내용을 입력해주세요ㅠㅠ')]) #글자수 제한없음
    # "제목" 은 폼 라벨임 이걸 이용해서 라벨 출력 가능함 validators 검증을 위해 사용되는 도구
    # DataRequired Eamil Lengh 등이 있음

class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])

class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])#사용자 이름
    #password1 비밀번호 password2 비밀번호 확인
    password1 = PasswordField('비밀번호', validators=[
        DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired(), Email()])#email 함수 쓰는거 그거 ㅇㅇ

class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])