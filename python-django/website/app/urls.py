from django.urls import path
from .views import ViewShops, get_shop_info,\
    ItemChange, AddItem, AddDep, DepChange, ShopDetail,\
    FilterItem, FilterShop, DepComparison, ComparisonDetails, get_notice

urlpatterns = [
    path('', ViewShops.as_view(), name='main'),
    path('shop/<int:id>/', get_shop_info, name='shop'),
    path('shop/<int:id>/detail/', ShopDetail.as_view(), name='shop-detail'),
    path('shop/<int:shop_id>/item/<int:item_id>/', ItemChange.as_view(), name='item'),
    path('shop/<int:shop_id>/item/add/', AddItem.as_view(), name='item-add'),
    path('shop/<int:shop_id>/dep/add/', AddDep.as_view(), name='dep-add'),
    path('shop/<int:shop_id>/dep/<int:dep_id>/', DepChange.as_view(), name='dep'),
    path('filter/item/<int:number>', FilterItem.as_view(), name='filter-item'),
    path('filter/shop/<int:number>', FilterShop.as_view(), name='filter-shop'),
    path('compare/', DepComparison.as_view(), name='compare'),
    path('compare/details/', ComparisonDetails.as_view(), name='comparison-details'),
    path('notice', get_notice, name='notice')
]
