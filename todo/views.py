from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .models import Todo
from .forms import TodoForm
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.


def registerForm(request):
    if request.method == 'GET':
        return render(request, 'todo/registerForm.html', {'form':UserCreationForm()})
    else:
        # create new user
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('mainpage')
            except IntegrityError:
                return render(request,'todo/registerForm.html',{'form':UserCreationForm(), "errMsg":"User exists. Choose a diffrent one"})
        else:
            return render(request,'todo/registerForm.html',{'form':UserCreationForm(), "errMsg":"Password didn't match"})

@login_required
def myitems(request):
    todos = Todo.objects.filter(user_id = request.user).order_by('-dateCreated')
    return render(request, 'todo/myitems.html', {'allitems': todos})


def homepage(request):
    return render(request,'todo/index.html')

@login_required
def logoutuser(request):
    if request.method == 'POST':
      logout(request)
      return redirect('homepage')

# def loginuser(request):
#     if (request.method == 'GET'):
#         return render(request, 'todo/loginform.html', {'form': AuthenticationForm()})
#     else:
#         user = authenticate(request, username=request.POST['username'], password = request.POST['password'])
#         if user is None:
#             return render(request, 'todo/loginform.html', {'form': AuthenticationForm(),"errMsg":"User doesn't exist"})
#         else:
#             login(request, user)
#             return redirect('myitems')

def loginuser(request):
    if (request.method == 'GET'):
        return render(request, 'todo/loginform.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password = request.POST['password'])
        if user is None:
            return render(request, 'todo/loginform.html', {'form': AuthenticationForm(),"errMsg":"User doesn't exist"})
        else:
            login(request, user)
            return redirect('mainpage')

def baskets(request):
    return render(request, 'todo/baskets.html')

def darksoft(request):
    return render(request, 'todo/darksoft.html')
            
@login_required
def newitem(request):
    if request.method == 'GET':
        return render(request, 'todo/newitem.html', {'form': TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            newTodo = form.save(commit=False)
            newTodo.user_id = request.user
            newTodo.save()
            return redirect('myitems')
        except ValueError:
            return render(request, 'todo/newitem.html', {'form': TodoForm(), 'errMsg': 'Data mismatch'})

@login_required
def edititem(request, todo_pk):
    # todo = get_object_or_404(Todo, pk=todo_pk)
    todo = get_object_or_404(Todo, pk=todo_pk, user_id=request.user)

    if (request.method == 'GET'):
        form = TodoForm(instance=todo)
        return render(request, 'todo/edititem.html', {'todo': todo, 'form': form})
    else:
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('myitems')
        except ValueError:
            return render(request, 'todo/edititem.html', {'form': TodoForm, 'errMsg': "Data mismatch"})

@login_required
def donetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user_id=request.user)

    if request.method == 'POST':
        # todo.dateCompleted = timezone.now()
        todo.save()
        return redirect('myitems')

@login_required
def deleteTodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user_id=request.user)

    if (request.method == 'POST'):
        todo.delete()
    return redirect('myitems') 

@login_required
def allitems(request):
    users = User.objects.all()
    todos = Todo.objects.filter(isImportant=True) #basket = 'Dark Soft')
    return render(request, 'todo/allitems.html', {'allitems': todos, 'users': users})

@login_required
def assigntome(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk)
    todo.user_id_id = request.user.id
    todo.save()
    return redirect('allitems')

def mainpage(request):
    return render(request,'todo/mainpage.html')