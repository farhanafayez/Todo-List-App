from django.shortcuts import redirect, render
from lists.models import Item, List


def home_page(request):
    return render(request, 'home.html')


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    x = list_.id
    return redirect('/lists/{}/'.format(x))


def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    x = list_.id
    return redirect('/lists/{}/'.format(x))


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})


