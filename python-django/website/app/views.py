from django.shortcuts import render, redirect
from django.views import View
from .models import Shop, Item, Department, Statistic
from django.db.models import Q, Avg, Count, Max, Sum, QuerySet


class ViewShops(View):

    def get(self, request):
        return render(request, 'app/index.html', context={
            'shops': [shop.name for shop in Shop.objects.all()]
        })

    def post(self, request):
        return redirect(
            f'shop/{Shop.objects.prefetch_related("departments__items").get(name=request.POST.get("name")).id}'
        )


class ShopDetail(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'app/shop_detail.html', context={
            'shop': Shop.objects.get(id=kwargs.get('id'))
        })

    def post(self, request, *args, **kwargs):
        return redirect(f'{kwargs.get("id")}')


def get_shop_info(request, *args, **kwargs):
    if request.GET.get('_method') == 'DELETE':
        Department.objects.get(
            sphere=request.GET.get('_sphere'),
            shop=Shop.objects.get(id=kwargs.get('id'))
        ).delete()
        return redirect(f'../../shop/{kwargs.get("id")}')
    return render(request, 'app/shop.html', context={
        'shop': Shop.objects.get(id=kwargs.get('id'))
    })


class ItemChange(View):
    http_method_names = ['get', 'post', 'put', 'delete']

    def get(self, request, *args, **kwargs):
        if request.GET.get('_method') == 'delete':
            Item.objects.get(id=kwargs.get('item_id')).delete()
            return redirect(f'../../../../shop/{kwargs.get("shop_id")}')
        return render(request, 'app/edit_items.html', context={
            'item': Item.objects.get(id=kwargs.get('item_id')),
            'shop_id': kwargs.get('shop_id'),
            'item_id': kwargs.get('item_id'),
        })

    def post(self, request, *args, **kwargs):
        if request.POST.get('_method') == 'PUT':
            item = Item.objects.get(id=kwargs.get('item_id'))
            item.name = request.POST.get('item_name')
            item.description = request.POST.get('item_description')
            item.price = request.POST.get('item_price')
            item.is_sold = True if request.POST.get('item_is_sold') == 'true' else False
            item.save()
            return redirect(f'../../../{kwargs.get("shop_id")}')


class AddItem(View):

    def get(self, request, *args, **kwargs):
        print(request.GET)
        request.session['_sphere'] = request.GET.get('_sphere')
        return render(request, 'app/add_item.html', context={
            'shop_id': kwargs.get('shop_id')
        })

    def post(self, request, *args, **kwargs):
        dep = Department.objects.get(
            sphere=request.session.get('_sphere'),
            shop=Shop.objects.get(id=kwargs.get('shop_id'))
        )
        request.session.clear()
        item = Item()
        item.name = request.POST.get('item_name')
        item.description = request.POST.get('item_description')
        item.price = request.POST.get('item_price')
        item.is_sold = True if request.POST.get('item_is_sold') == 'true' else False
        item.comments = request.POST.get('item_comment').split('\n')
        item.department = dep
        item.save()

        return redirect(f'../../../{kwargs.get("shop_id")}')
        pass


class DepChange(View):
    http_method_names = ['get', 'post', 'put', 'delete']

    def get(self, request, *args, **kwargs):
        return render(request, 'app/edit_dep.html', context={
            'dep': Department.objects.get(id=kwargs.get('dep_id')),
            'shop_id': kwargs.get('shop_id'),
            'item_id': kwargs.get('item_id'),
        })

    def post(self, request, *args, **kwargs):
        if request.POST.get('_method') == 'PUT':
            dep = Department.objects.get(id=kwargs.get('dep_id'))
            dep.sphere = request.POST.get('dep_sphere')
            dep.staff_amount = request.POST.get('dep_staff_amount')
            dep.save()
            return redirect(f'../../../{kwargs.get("shop_id")}')


class AddDep(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'app/add_dep.html', context={
            'shop_id': kwargs.get('shop_id')
        })

    def post(self, request, *args, **kwargs):
        dep = Department()
        dep.sphere = request.POST.get('dep_sphere')
        dep.staff_amount = request.POST.get('dep_staff_amount')
        dep.shop = Shop.objects.get(id=kwargs.get("shop_id"))
        dep.save()
        return redirect(f'../../../{kwargs.get("shop_id")}')


class FilterItem(View):

    def get(self, request, *args, **kwargs):
        if kwargs.get('number') == 1:
            items = Item.objects.filter(name__istartswith='a')
        if kwargs.get('number') == 2:
            items = Item.objects.filter(price__gt=10, department__staff_amount__lte=50)
        if kwargs.get('number') == 3:
            items = Item.objects.filter(Q(price__gt=20) | Q(department__staff_amount__gt=50))
        if kwargs.get('number') == 4:
            items = Item.objects.filter(Q(id=1) | Q(id=3) | Q(id=5) | Q(id=6))
        if kwargs.get('number') == 5:
            items = Item.objects.filter(
                Q(
                    Q(price__gt=10) & Q(name__icontains="a")
                ) | Q(
                    Q(price__lt=20) & Q(name__icontains="o")
                )
            )
        if kwargs.get('number') == 6:
            items = Item.objects.select_related('department').all()
            items = [item for item in items if item.price == item.department.staff_amount + 10]
        return render(request, 'app/filter_item.html', context={
            'items': items
        })


class FilterShop(View):

    def get(self, request, *args, **kwargs):
        if kwargs.get('number') == 1:
            shops = Shop.objects.all().annotate(
                employees=Sum('departments__staff_amount'),
            )
            shops = [shop for shop in shops if shop.staff_amount != shop.employees]
        if kwargs.get('number') == 2:
            shops = Shop.objects.filter(departments__items__price__lt=5)
        if kwargs.get('number') == 3:
            shops = Shop.objects.all().annotate(
                employees=Sum('departments__staff_amount'),
                deps=Count('departments'),
                items_amount=Count('departments__items'),
                max_price=Max('departments__items__price')
            )
        if kwargs.get('number') == 4:
            shops = Shop.objects.all().annotate(
                items_amount=Count('departments', filter=Q(departments__items__price__gt=10))
            )
        return render(request, 'app/filter_shop.html', context={
            'shops': shops
        })


class DepComparison(View):

    def get(self, request):
        return render(request, 'app/compare.html', context={
            'deps': Department.objects.all()
        })

    def post(self, request, *args, **kwargs):
        return redirect('comparison-details')


class ComparisonDetails(View):

    def post(self, request, *args, **kwargs):
        deps = Department.objects.filter(Q(id=request.POST.get('dep1')) | Q(id=request.POST.get('dep2')))
        if request.POST.get('v2'):
            deps = deps.annotate(sold_items_price=Sum('items__price', filter=Q(items__is_sold=True)))
        if request.POST.get('v3'):
            deps = deps.annotate(unsold_items_price=Sum('items__price', filter=Q(items__is_sold=False)))
        if request.POST.get('v4'):
            deps = deps.annotate(all_items_price=Sum('items__price'))
        if request.POST.get('v5'):
            deps = deps.annotate(sold_items_amount=Count('items', filter=Q(items__is_sold=True)))
        if request.POST.get('v6'):
            deps = deps.annotate(unsold_items_amount=Count('items', filter=Q(items__is_sold=False)))
        if request.POST.get('v7'):
            deps = deps.annotate(all_items_amount=Count('items'))
        return render(request, 'app/comparison_detail.html', context={
            'deps': deps,
            'v1': request.POST.get('v1', ''),
            'dep11': deps[0],
            'dep12': deps[1],
            'shop1': Shop.objects.get(id=2),
            'item1': Item.objects.get(id=3),
        })


def get_notice(request):
    return render(request, 'app/notice.html')
