from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse, Http404
from .models import Menu, Option
#from django.utils.timezone import now

def index_view(request):
    return render(request, 'manager/index.html')
  

def menu_list(request):
    menus =Menu.objects.all()
    context = {
        "menus_to_page": menus,
        "cafe_name": "Sanaria"
    }
    return render(request, 'manager/menu_list.html', context)
    
def menu_add(request):
    return render(request, 'manager/menu_add.html')


def add_menu_data(request):
    menu_name_from_form = request.POST['menu_name']
    if menu_name_from_form.strip()=='': # 제대로 된 값이 맞는지 검증해서 처리
        context = {"message":"메뉴 이름을 넣으셔야 됩니다."}
        return render(request, 'manager/menu_add.html', context)
    menu_price_from_form = request.POST['menu_price']
    Menu.objects.create(menu_name=menu_name_from_form, menu_price=menu_price_from_form)
    print(f"메뉴이름 : {menu_name_from_form}, 가격 : {menu_price_from_form} 이 추가되었습니다. ")
    return render(request, 'manager/menu_add.html')

def menu_detail(request, menu_id):
    menu=Menu.objects.get(pk=menu_id)
    context = {
        'menu_to_page': menu
    }
    #print("menu_id":menu_id)
    return render(request, 'manager/menu_detail.html', context) # 완료

def add_option(request, menu_id):
    menu = Menu.objects.get(pk=menu_id)
    context = {"menu":menu}
    return render(request, 'manager/add_option.html', context=context)
                  

def add_option_data(request):
    menu_id_from_form = request.POST['menu_id']
    menu = Menu.objects.get(pk=menu_id_from_form)
    option_name_from_form = request.POST['option_name']
    option_price_from_form = request.POST['option_price']
    Option.objects.create(menu=menu, option_name=option_name_from_form, option_price=option_price_from_form)
    context = {"menu": menu}
    print(f"메뉴 : {menu.menu_name}, 옵션 : {option_name_from_form}, 가격 : {option_price_from_form} 이 추가되었습니다. ")
    return render(request, 'manager/add_option.html', context)