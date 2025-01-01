from django.shortcuts import render, get_object_or_404

from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-created")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request,"polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(question=question_id)
    context =  {"question": question}
    return render (request, "polls/detail.html", context)

def results(request, question_id):
    response = "You are looking at %s."
    return render (request,context)

def vote(request, question_id):
    return HttpResponse ("You are voting on question %s at %s." % question_id)

