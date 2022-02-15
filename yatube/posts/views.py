from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'title': 'главная страница проекта YaTube',
        'text': 'Это главная страница проекта YaTube',
    }


    template = 'posts/index.html'
    return render(request, template, context)

def group_posts(request):
    context = {
        'title': 'информация о группах проекта Yatube',
        'text': 'Здесь будет информация о группах проекта Yatube',
    }

    template = 'posts/group_list.html'
    return render(request, template, context)

def group_posts1(request, any_slag):
    return HttpResponse(f'Посты Толстого {any_slag}')
