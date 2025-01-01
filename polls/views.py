from django.http import Http404
from django.shortcuts import render
from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-created")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question-id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render (request, "polls/detail.html", {"question" question})

def results(request, question_id):
    response = "You are looking at %s."
    return HttpResponse (response % question_id)

def vote(request, question_id):
    return HttpResponse ("You are voting on question %s at %s." % question_id)

