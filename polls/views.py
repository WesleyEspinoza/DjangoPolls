"""temp Doc String"""
from django.http import HttpResponse
from django.utils import timezone
from django.views import View
from polls.models import Question

def index(request):
    """temp Doc String"""
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    ouput = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse("Latest Polls \n {}".format(ouput))

def detail(request, question_id):
    """temp Doc String"""
    return HttpResponse("you are looking at Questiion {}".format(question_id))

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
