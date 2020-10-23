from django.http import HttpResponse
from django.template import loader

from .models import Question


# Create your views here.
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	# output = ','.join(q.question_text for q in latest_question_list)
	template = loader.get_template('polls/index.html')
	context = {
		'latest_question_list': latest_question_list,
	}
	return HttpResponse(template.render(context, request))


def detail(request, question_id):
	return HttpResponse("you are looking at % s . " % question_id)


def results(request, question_id):
	return HttpResponse("You are seeing the results for % s . " % question_id)


def vote(request, question_id):
	return HttpResponse("You are voting for question %s ." % question_id) 