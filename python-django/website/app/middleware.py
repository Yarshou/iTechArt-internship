from django.shortcuts import redirect
from .models import Shop, Department, Item, Statistic


class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.ITEMS_AMOUNT = len(Shop.objects.filter(departments__items__is_sold=False))
        response = self.get_response(request)
        stat_obj = Statistic.objects.get_or_create(
            url=request.path
        )[0]
        stat_obj.amount += 1
        stat_obj.save()
        if not request.ITEMS_AMOUNT and not request.path.startswith('/notice') \
                and not request.path.startswith('/admin'):
            return redirect('notice')
        return response
