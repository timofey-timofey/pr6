from django.shortcuts import render, redirect
from .models import Fruit
from .forms import FruitForm

def fruit_list(request):

    fruits = Fruit.objects.all().order_by('-created_at')
    return render(request, 'fruits/list.html', {'fruits': fruits})

def add_fruit(request):

    if request.method == 'POST':
        form = FruitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fruit_list')
    else:
        form = FruitForm()
    return render(request, 'fruits/add.html', {'form': form})

def delete_fruit(request, fruit_id):

    Fruit.objects.get(id=fruit_id).delete()
    return redirect('fruit_list')