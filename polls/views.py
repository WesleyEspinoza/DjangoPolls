"""temp Doc String"""
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import View, generic
from django.shortcuts import get_object_or_404, render
from polls.models import Question, Choice



class IndexView(generic.ListView):
    """temp Doc String"""
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    """temp Doc String"""
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    """temp Doc String"""
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    """temp Doc String"""
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question' : question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

class ShowTimeView(View):
    """temp Doc String"""
    def get(self, request):
        """temp Doc String"""
        now = timezone.now()
        html = '<html><body> Time is %s</body></html>' % now
        return HttpResponse(html)
