from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.templatetags.static import static
print(static('css/styles.css'))


# Функция для регистрации пользователя
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')  # перенаправляем пользователя на страницу входа после регистрации
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
