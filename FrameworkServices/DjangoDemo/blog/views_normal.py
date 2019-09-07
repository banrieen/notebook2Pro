from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
# from django.template import loader # 使用render快捷方法替代
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from . models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('blog/index.html')
    context = {
        'latest_question_list':latest_question_list,
    }
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(template.render(context, request))
    return render(request, 'blog/index.html',context)


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=questioin_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist')
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "blog/detail.html", {'question':question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'blog/results.html',{'question':question})
    # response = "You are looking at the results of question %s."
    # return HttpResponse(response % question_id)

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

