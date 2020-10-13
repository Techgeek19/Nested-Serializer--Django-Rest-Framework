from django.urls import path, include
from main.views import *

urlpatterns = [
    path('question/', QuestionListView.as_view()),
    path('question/<int:id>/', QuestionListView.as_view()) 
]


