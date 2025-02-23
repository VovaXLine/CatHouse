from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import VolunteerForm
import random

def home(request):
    return render(request, 'home.html')

def about(request):
    fun_facts_list = ['Всего существует 33 основных кошачьих породы. А количество домашних кошек в мире достигает 500 миллионов.',
                    'Рисунок кожи на носу у кошки по своей уникальности сравним с отпечатками пальцев.',
                    'Кошка чувствует запах в среднем в 14 раз лучше, чем человек.',
                    'У кошек потеют только подушечки на лапках.',
                    'В Англии по статистике на десять жителей приходится девять домашних кошек.',
                    'Домашняя кошка проводит во сне около 70% своей жизни.',
                    'Коты чаще всего левши, а кошки – правши.']
    fun_fact = random.choice(fun_facts_list)
    return render(request, 'about.html', {'fun_fact': fun_fact})


def how_to_help(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000//how_to_help')
    else:
        form = VolunteerForm()
    
    return render(request, 'help.html', {'form': form})