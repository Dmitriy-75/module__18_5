from django.shortcuts import render

# Create your views here.


def main_page(request):
    title="Игровая платформа"
    text="Главная страница"
    context={
        "title": title,
        "text": text
    }

    return render(request, 'main_page.html',context)


def basket(request):
    title = "Игровая платформа"
    text = "Корзина"
    context = {
        "title": title,
        "text": text
    }
    return render(request, 'basket.html',context)


def shop(request):
    title = "Игровая платформа"
    text = "Магазин"
    context = {
        "title": title,
        "text": text
    }
    return render(request, 'shop.html',context)