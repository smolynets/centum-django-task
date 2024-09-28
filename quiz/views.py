from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from .forms import QuestionareForm, QuestionForm, AnswerForm
from .models import Questionare, Question, Answer


class HomeView(TemplateView):
    template_name = 'quiz/home.html'


def create_questionare_with_questions(request):
    QuestionFormSet = modelformset_factory(Question, form=QuestionForm, extra=1)
    AnswerFormSet = modelformset_factory(Answer, form=AnswerForm, extra=4)

    if request.method == 'POST':
        questionare_form = QuestionareForm(request.POST)
        question_formset = QuestionFormSet(request.POST, prefix='questions')
        answer_formset = AnswerFormSet(request.POST, prefix='answers')

        if questionare_form.is_valid() and question_formset.is_valid() and answer_formset.is_valid():
            questionare = questionare_form.save()
            questions = question_formset.save(commit=False)
            for question in questions:
                question.questionare = questionare
                question.save()

            answers = answer_formset.save(commit=False)
            for answer in answers:
                question = questions[0]  # Додаємо відповіді до першого питання (зможете це налаштувати на свій розсуд)
                answer.question = question
                answer.save()

            return redirect('home')

    else:
        questionare_form = QuestionareForm()
        question_formset = QuestionFormSet(prefix='questions')
        answer_formset = AnswerFormSet(prefix='answers')

    return render(request, 'quiz/create_questionare_with_questions.html', {
        'questionare_form': questionare_form,
        'question_formset': question_formset,
        'answer_formset': answer_formset,
    })

