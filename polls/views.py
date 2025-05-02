# polls/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()           # створюємо користувача
            login(request, user)         # одразу логінимо
            return redirect('home')      # перенаправлення після успіху
    else:
        form = UserRegistrationForm()     # порожня форма для GET

    return render(request, 'register.html', {'form': form})
