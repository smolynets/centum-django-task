from django.urls import path
from .views import HomeView, QuestionareListView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('questionares/', QuestionareListView.as_view(), name='questionare_list')
]
