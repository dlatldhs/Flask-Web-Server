from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class QuestionForm(FlaskForm):
    subject = StringField('제목',validators=[DataRequired()]) #글자수 제한있음
    content = TextAreaField('내용',validators=[DataRequired()]) #글자수 제한없음
    # "제목" 은 폼 라벨임 이걸 이용해서 라벨 출력 가능함 validators 검증을 위해 사용되는 도구
    # DataRequired Eamil Lengh 등이 있음 