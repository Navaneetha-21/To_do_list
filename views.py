from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import To_do_model
from .form import To_do_form
from django.urls import reverse


def to_do_list(request):
    tasks = To_do_model.objects.all().order_by('-id')

    filter_param = request.GET.get('filter' , 'all')
    
    if filter_param=='active':
        tasks=tasks.filter(completed=False)
    elif filter_param=='completed':
        tasks=tasks.filter(completed=True)


    if request.method =="POST":
        form  = To_do_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=To_do_form()

    total = To_do_model.objects.count()
    active_count  = To_do_model.objects.filter(completed=False).count()
    completed_count = To_do_model.objects.filter(completed=True).count()

    context ={
        'Tasks':tasks,
        'form':form,
        'Total':total,
        'active_count' : active_count,
        'completed_count':completed_count,
        'current_filter':filter_param,     
    }

    return render(request,'to_do/home.html',context)


def to_do_delete(request,id):
    task = get_object_or_404(To_do_model,id=id)
    task.delete()
    return redirect('home')


def to_do_toggle(request,id):
    task = get_object_or_404(To_do_model,id=id)

    task.completed = not task.completed
    task.save()
    return redirect(f"{reverse('home')}?filter={request.GET.get('filter','all')}")
    
