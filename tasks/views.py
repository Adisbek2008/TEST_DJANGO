from django.shortcuts import render, get_object_or_404, redirect
from .models import Task, Category
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()
    categories = Category.objects.all()
    query = request.GET.get('q')
    selected_category = request.GET.get('category')

    if query:
        tasks = tasks.filter(title__icontains=query)
    if selected_category:
        tasks = tasks.filter(category__id=selected_category)

    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'categories': categories,
        'request': request,
    })

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_create.html', {'form': form})
