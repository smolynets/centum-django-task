from django.urls import path
from .views import HomeView, create_questionare_with_questions


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create-questionare/', create_questionare_with_questions, name='create_questionare')
]
