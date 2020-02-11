"""temp Doc String"""
from django.http import HttpResponse
from django.utils import timezone
from django.views import View
from django.shortcuts import get_object_or_404, render
from polls.models import Question


def index(request):
    """temp Doc String"""
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    """temp Doc String"""
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question,
    }
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    """temp Doc String"""
    return HttpResponse("you are looking at the results of question {}".format(question_id))

def vote(request, question_id):
    """temp Doc String"""
    return HttpResponse("you are looking at the voting page for question {}".format(question_id))

class ShowTimeView(View):
    """temp Doc String"""
    def get(self, request):
        """temp Doc String"""
        now = timezone.now()
        html = '<html><body> Time is %s</body></html>' % now
        return HttpResponse(html)
