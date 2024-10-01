from django.views.generic import TemplateView, ListView
from django.shortcuts import render, redirect
from .models import Questionare, Question, Answer
from django.forms import inlineformset_factory


class HomeView(TemplateView):
    template_name = 'quiz/home.html'


class QuestionareListView(ListView):
    model = Questionare
    template_name = 'questionare_list.html'
    context_object_name = 'questionares'

    def get_queryset(self):
        return Questionare.objects.prefetch_related('questions__answers')
