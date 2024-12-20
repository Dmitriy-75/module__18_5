from django.shortcuts import render

# Create your views here.

# В представлении где вы использовали context измените словарь следующим образом: {'first': ''Atomic Heart", 'second': "Cyberpunk 2077" }"
# " -> {'games': ['Atomic Heart", "Cyberpunk 2077"]}. Т.е. вместо передачи нескольких значений будет передаваться один единый список из этих значений.

def menu(request):
    title="Игровая платформа"
    text="Главная страница"
    context = {
        "title": title,
        "text": text
    }
    return render(request, 'main_page.html', context)


def basket(request):

    text1 = "Корзина"
    text2 = "Извините, Ваша корзина пуста"

    context = {
        "text1": text1,
        "text2": text2
    }
    return render(request, 'basket.html', context)


def shop(request):

    context = {
        "games": ['Шахматы', 'Шашки', 'Шиша-беша'],
    }
    return render(request, 'shop.html', context)




