from flask import Blueprint, render_template, request, url_for, g
from ..forms import QuestionForm, AnswerForm
from pybo.models import Question
from datetime import datetime
from pybo.views.auth_views import login_required
from werkzeug.utils import redirect
from .. import db
bp = Blueprint('question',__name__,url_prefix='/question')

@bp.route('/list/')
def _list():
    page= request.args.get('page', type=int, default=1) # 요청한 url 에서 page 값을 5를 가져옴 없으면 1
    question_list = Question.query.order_by(Question.create_date.desc())
    question_list = question_list.paginate(page,per_page=10)#page = 조회할 페이지 번호 per_page 페이지 마다 보여줄꺼 10개
    return render_template('question/question_list.html',question_list=question_list)

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    form = AnswerForm()
    question=Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html',question=question, form=form)

@bp.route('/create/', methods=('GET','POST'))
@login_required
def create():
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit():
        question = Question(subject=form.subject.data, content=form.content.data, create_date=datetime.now(),user=g.user)
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('question/question_form.html',form=form)