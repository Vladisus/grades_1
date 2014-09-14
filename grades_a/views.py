from django.shortcuts import render_to_response
from django.template import RequestContext
from grades_a.models import *

def home(request):
    context = RequestContext(request)
    new_list = new.objects.all()
    student_list = student.objects.all()
    context_dict = {'list' : student_list , 'news' : new_list}
    return render_to_response('index.html', context_dict , context)

def list(request):
    context = RequestContext(request)
    student_list = student.objects.all()
    context_dict = {'list' : student_list}
    return render_to_response('list.html' , context_dict, context)


def student_student(request, student_id=1):
    context = RequestContext(request)
    context_dict = {'student' : student.objects.get(id=student_id)}
    return render_to_response('single.html', context_dict, context)

def dz(request):
    contxet = RequestContext(request)
    context_dict = {'dz' : news.objects.all()}
    return render_to_response('dz.html', context_dict, contxet)