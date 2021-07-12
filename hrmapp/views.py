from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Todo
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
# Create your views here.

class TaskListview(ListView):
    model = Todo
    template_name = 'home.html'
    context_object_name = 'task2'
class TaskDetailView(DetailView):
    model = Todo
    template_name = 'detail.html'
    context_object_name = 'task2'
class TaskUpdateView(UpdateView):
    model = Todo
    template_name = 'update.html'
    context_object_name = 'task2'
    fields = ('data','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model = Todo
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')

def add(request):
    task1 = Todo.objects.all()
    if request.method=="POST":
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('Date','')
        task=Todo(data=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'task2':task1})
def delete(request,taskid):
    task3=Todo.objects.get(id=taskid)
    if request.method=='POST':
        task3.delete()
        return redirect('/')
    return render(request,'delete.html')


def update(request,id):
    datas=Todo.objects.get(id=id)
    f=TodoForm(request.POST or None,instance=datas)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'task':datas,'form':f})