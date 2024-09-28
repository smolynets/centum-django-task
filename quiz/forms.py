from django import forms
from .models import Questionare, Question, Answer

class QuestionareForm(forms.ModelForm):
    class Meta:
        model = Questionare
        fields = ['name', 'description']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'questionare']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_text', 'is_correct', 'question']
