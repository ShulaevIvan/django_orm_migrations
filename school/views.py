from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    ordering = 'group'
    obj = Student.objects.prefetch_related('teacher').order_by(ordering)
    # for i in obj:
    #     print(i.teacher)
    context = {
        'object_list': obj,
    }

    

    return render(request, template, context)
