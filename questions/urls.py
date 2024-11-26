from django.urls import path
from . import views
urlpatterns = [
    path('', views.get_list_of_questions, name='get_list_of_questions'),
    path('<str:question_text>/get/', views.get_question, name='get_question'),
    path('<str:question_text>/update/',views.update_question,name='update_question'),
    path('<str:question_text>/delete/',views.delete_question,name='delete_question')# URL for listing questions
]
