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
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    """temp Doc String"""
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


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
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        revrs = reverse('polls:results', args=(question.id,))
        reponse = HttpResponseRedirect(revrs)

        return reponse


class ShowTimeView(View):
    """temp Doc String"""
    def get(self, request):
        """temp Doc String"""
        now = timezone.now()
        html = '<html><body> Time is %s</body></html>' % now
        return HttpResponse(html)
