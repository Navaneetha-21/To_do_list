from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import To_do_model
from .form import To_do_form
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


@login_required
def to_do_list(request):
    tasks = To_do_model.objects.filter(user=request.user).order_by('-id')

    filter_param = request.GET.get('filter' , 'all')
    
    if filter_param=='active':
        tasks=tasks.filter(completed=False)
    elif filter_param=='completed':
        tasks=tasks.filter(completed=True)


    if request.method =="POST":
        form  = To_do_form(request.POST)
        if form.is_valid():
            new_task=form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('home')
    else:
        form=To_do_form()

    total = To_do_model.objects.filter(user=request.user).count()
    active_count  = To_do_model.objects.filter(user=request.user,completed=False).count()
    completed_count = To_do_model.objects.filter(user=request.user,completed=True).count()

    context ={
        'Tasks':tasks,
        'form':form,
        'Total':total,
        'active_count' : active_count,
        'completed_count':completed_count,
        'current_filter':filter_param,     
    }

    return render(request,'to_do/home.html',context)

@login_required
def to_do_delete(request,id):
    task = get_object_or_404(To_do_model,id=id,user=request.user)
    task.delete()
    return redirect('home')

@login_required
def to_do_toggle(request,id):
    task = get_object_or_404(To_do_model,id=id,user=request.user)

    task.completed = not task.completed
    task.save()
    return redirect(f"{reverse('home')}?filter={request.GET.get('filter','all')}")
    

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserCreationForm()

    return render(request,'registration/register.html' ,{'form':form})