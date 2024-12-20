from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister


# Create your views here.

# Представления:
# Напишите 2 представления sign_up_by_django и sign_up_by_html.
# Оба представления должны обладать следующим функционалом:
# Псевдо-список users уже существующих пользователей. (имена пользователей придумайте самостоятельно).
# Пустой словарь info, который будет передаваться в context функции render. В случае формы в этом словаре будет и форма.
# Получение данных из POST запроса.
# Обработка данных из POST запроса:
# Если пароль и повторный пароль совпадают + возраст не менее 18 + пользователя ещё нет в users, то возвращается ответ
# "Приветствуем, <логин пользователя>!"

# В следующих случаях в словарь info добавляются следующие значения под ключом 'error':
# 1.'Пароли не совпадают', если не совпали введённые пароли.
# 'Вы должны быть старше 18', если возраст меньше 18.
# 'Пользователь уже существует', если username есть в users
# Соответственно необходимо выводить значение переменной error в шаблоне.
#
# Представления должны запускаться по маршрутам: '' и 'django_sign_up' соответственно.

users =['Anya','Lilya','Dima']


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        for i in users:
            if i == username:
                info['error'] = 'Пользователь уже  существует'

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'

        if int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'

        if not info:
            info['hello'] = f'Приветствуем, {username}!'

        print(f'username={username}')
        print(f'password={password}')
        print(f'age={age}')

        return render(request, "fifth_task/registration_page.html", info)

    return render(request, "fifth_task/registration_page.html", info)



def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            for i in users:
                if i == username:
                    info['error'] = 'Пользователь уже  существует'

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'

            if int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'

            if not info:
                info['hello'] = f'Приветствуем, {username}!'

            print(f'username={username}')
            print(f'password={password}')
            print(f'age={age}')

            return render(request, "fifth_task/registration_page.html", info)

    return render(request, "fifth_task/registration_page.html", info)














