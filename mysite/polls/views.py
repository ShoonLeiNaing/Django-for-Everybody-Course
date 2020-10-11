from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import render,get_object_or_404
from . models import Question,Choice
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

class ProtectView(LoginRequiredMixin, View):
    def get(self,request):
      return render(request,'polls/main.html')




def owner(request):
    return HttpResponse("<p>a440a3d3</p><br> Hello, world. e0a0a422 is the polls index.")

class IndexView(View):
    def get(self,request):
        latest_question_list=Question.objects.order_by('-pub_date')[:5]
        context={'latest_question_list':latest_question_list}
        return render(request,'polls/index.html',context)

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(View):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question=get_object_or_404(Question,pk=question_id)

    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])

    except( KeyError, Choice.DoesNotExist ):
        return render(request, "polls/detail.html", {'question':question, 'error_message': "You did not select a choice"})

    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results',args=(question.id,)))



def checkguess(guess) :
    msg = False
    if guess :
        try:
            if int(guess) < 42 :
                msg = 'Guess too low'
            elif int(guess) > 42 :
                msg = 'Guess too high'
            else:
                msg = 'Congratulations!'
        except:
            msg = 'Bad format for guess:' + html.escape(guess)
    return msg


class guessingGame(View):
    def get(self,request):
        msg=request.session.get('msg', False)
        if ( msg ):del(request.session['msg'])
        return render(request,"polls/guess.html",{'message':msg})

    def post(self,request):
        guess=request.POST.get('guess')
        msg=checkguess(guess)
        request.session['msg']=msg
        return redirect(request.path)


def cookie(request):
    print(request.COOKIES)
    resp=HttpResponse("C for Cookies")
    resp.set_cookie('shoon',42)
    resp.set_cookie('shoonlei',33,max_age=1000)
    return resp






























