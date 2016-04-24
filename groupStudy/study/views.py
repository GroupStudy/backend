from django.http import HttpResponse

from django.template import RequestContext, loader

from .models import *


def index(request):


    buildings = Places.objects.all()

    template = loader.get_template('study/test.html')




    context = RequestContext(request, {

        'build':buildings,

    })
    return HttpResponse(template.render(context))



def inbuilding(request,build_id):

    checked = checkedIn.objects.filter(atBuilding = build_id)

    template = loader.get_template('study/selected.html')


    context = RequestContext(request, {

        'checked':checked,

    })
    return HttpResponse(template.render(context))

def openUser(request,build_id,student_id):

    classes = studentClasses.objects.filter(student = student_id)

    student = Student.objects.filter(id = student_id)

    current = Current.objects.filter(user = student_id)


    template = loader.get_template('study/viewUser.html')

    context = RequestContext(request, {
        'student':student,
        'class':classes,
        'cur':current,

    })
    return HttpResponse(template.render(context))

