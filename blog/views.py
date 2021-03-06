from django.shortcuts import render
from .models import Project
from django.http import HttpResponse

def add(request):
    print(int(request.POST['id']))
    Project.objects.create(id=int(request.POST['id']),
                            position=Project.objects.count()+1)
    return HttpResponse(status=200)

def delete(request):
    object = Project.objects.filter(id=int(request.POST['id']))
    for el in Project.objects.filter(position_gt=object.position):
        el.position -= 1
    object.delete()
    return HttpResponse(status=200)
# def change_up(request):
#     object = Project.objects.filter(position=int(request.POST['position']))[0]
#     print(object)
#     object2 = Project.objects.filter(position__gt=min(int(request.POST['position']), int(request.POST['new_position'])+1 ),
#                         position__lte=max(int(request.POST['new_position'])+1, int(request.POST['position'])))
#     print(object2)
#     if int(request.POST['new_position'])+1 > int(request.POST['position']):
#         co = -1
#     else:
#         co = 1
#     print(co)
#     for i in object2:
#                    i.position += co
#                    print(i.id, i.position)
#                    i.save()
#     object.position = int(request.POST['new_position'])+1
#     object.save()
#     return HttpResponse(status=200)
# # clon1234 admin
# def change_down(request):
#    object = Project.objects.filter(position=int(request.POST['position']))[0]
#    object2 = Project.objects.filter(position__lt=int(request.POST['position']), position__gte=int(request.POST['new_position']))
#    print(object2)
#    for i in object2:
#                   i.position += 1
#                   i.save()
#    object.position = int(request.POST['new_position'])+1
#    object.save()
#    return HttpResponse(status=200)

def chage(request):
    if int(request.POST['position'])>=int(request.POST['new_position']):
        object = Project.objects.filter(position=int(request.POST['position']))[0]
        object2 = Project.objects.filter(position__lt=int(request.POST['position']), position__gte=int(request.POST['new_position']))
        print(object2)
        for i in object2:
            i.position += 1
            i.save()
        object.position = int(request.POST['new_position'])+1
        object.save()
        return HttpResponse(status=200)
    else:
        object = Project.objects.filter(position=int(request.POST['position']))[0]
        print(object)
        object2 = Project.objects.filter(position__gt=min(int(request.POST['position']), int(request.POST['new_position'])+1 ),
                             position__lte=max(int(request.POST['new_position'])+1, int(request.POST['position'])))
        print(object2)
        if int(request.POST['new_position'])+1 > int(request.POST['position']):
            co = -1
        else:
            co = 1
        print(co)
        for i in object2:
            i.position += co
            print(i.id, i.position)
            i.save()
        object.position = int(request.POST['new_position'])+1
        object.save()
        return HttpResponse(status=200)
