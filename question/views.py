from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Question
def get_list_of_questions(request):
    Question.objects.create(text='question2',answer='answer2')
    questions=Question.objects.all()
    d={}
    for question in questions:
        d[question.text]=question.answer
    return JsonResponse(d)
def get_question(request,question_text):
    question = Question.objects.filter(text=question_text)
    if question:
        d={question.text: question.answer}
        return JsonResponse(d)
    else:
        return JsonResponse({"error":"question is required"})
def update_question(request,question_text):
    question=Question.objects.get(text=question_text)
    question.answer='Answer4'
    question.save()
    d={
        question.text:question.answer
    }
    return JsonResponse(d)
def delete_question(request,question_text):
    Question.objects.create(text='question4',answer='answer4')
    Question.objects.create(text='question1',answer='answer1')
    question=Question.objects.get(text=question_text)
    question.delete()
    questions=Question.objects.all()
    d={}
    for q in questions:
        if q.text in d:
            continue
        else:
            d[q.text]=q.answer
    return JsonResponse(d)