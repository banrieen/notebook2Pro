from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from . models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """ 返回最新的5个问题 """
        return Question.objects.filter(
            pub_date__lte = timezone.now()
        ).order_by('-pub_date')[:5]
        # Question.objects.order_by('-pub_date')[:5]

    

class DetailView(generic.DetailView):
    model = Question
    template_name = 'blog/detail.html'

    def get_queryset(self):
        """ 返回没有发布的question """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'blog/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question form
        return render(request, 'blog/detail.html',{
            'question': question,
            'error_message': 'You did`t select a choice.',
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        #  Always return an HttpResponseRedirect after successfully dealing with POST data.
        #  This prevents data from being posted twice if a user hits the Back button.
        return HttpResponseRedirect(reverse('blog:results',args=(question.id,)))

