from django import forms

# Создайте форму UserRegister, наследованную от Django формы с аналогичными параметрами, как и в шаблоне.

class UserRegister(forms.Form):
    username= forms.CharField(max_length=30,label="Введите Ваш логин")
    password = forms.CharField(min_length=8, label="Введите Ваш пароль")
    repeat_password = forms.CharField(min_length=8, label="Повторите Ваш пароль")
    age = forms.CharField(max_length=8, label="Введите свой возраст")




