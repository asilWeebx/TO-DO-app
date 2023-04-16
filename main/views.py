from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from .models import ToDo
from user.models import User
from .forms import *


# https://qna.habr.com/q/236166
# https://dev-gang.ru/article/kak-razvernut-prilozhenie-django-v-heroku-s-pomosczu-git-cli-oclmngimkd/

# Create your views here.
@login_required(login_url='/login/')
def index(request):
    todos = ToDo.objects.all()
    return render(request, 'main/index.html', {'todo_list': todos, 'title': 'Asosiy Sahifa'})


@require_http_methods(['POST'])
@csrf_exempt
def add(request):
    title = request.POST['title']
    info = request.POST['info']
    yakunlaniwi = request.POST['yakunlaniwi']
    todo = ToDo(title=title,info=info,yakunlaniwi=yakunlaniwi)
    todo.save()
    return redirect('index')

def update(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('index')

def delete(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')

@login_required(login_url='/login')
def edit(request,id):
    model = ToDo.objects.get(id=id)
    form = ToDoForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('index')
            messages.success(request, 'Record Are Successfully Updated !')
    ctx = {
        "form": form
    }


    return render(request, 'main/edit.html',ctx)
