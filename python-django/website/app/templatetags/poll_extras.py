from django import template
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from ..models import Shop, Department, Item


register = template.Library()


@register.filter()
def url(value):
    if isinstance(value, Shop):
        res = mark_safe(f"<a href={reverse_lazy('shop', args=[value.id, ])}>{value}</a>")
    if isinstance(value, Department):
        res = mark_safe(f"<a href={reverse_lazy('shop', args=[value.shop.id, ])}>{value}</a>")
    if isinstance(value, Item):
        res = mark_safe(f"<a href={reverse_lazy('shop', args=[value.department.shop.id, ])}>{value}</a>")
    return res


@register.simple_tag
def get_leader(dep1, dep2, comparison_detail):
    if comparison_detail == 1:
        if dep1.staff_amount > dep2.staff_amount:
            res_str = f'<td style="background-color: greenyellow">{dep1.staff_amount}</td><td>{dep2.staff_amount}</td>'
        elif dep1.staff_amount < dep2.staff_amount:
            res_str = f'<td>{dep1.staff_amount}</td><td style="background-color: greenyellow">{dep2.staff_amount}</td>'
        else:
            res_str = ''
    if comparison_detail == 2:
        dep1_res = sum([i.price for i in dep1.items.filter(is_sold=True)])
        dep2_res = sum([i.price for i in dep2.items.filter(is_sold=True)])
        if dep1_res > dep2_res:
            res_str = f'<td style="background-color: greenyellow">{dep1_res}</td><td>{dep2_res}</td>'
        elif dep1_res < dep2_res:
            res_str = f'<td">{dep1_res}</td><td style="background-color: greenyellow>{dep2_res}</td>'
        else:
            res_str = ''
    if comparison_detail == 3:
        dep1_res = sum([i.price for i in dep1.items.filter(is_sold=False)])
        dep2_res = sum([i.price for i in dep2.items.filter(is_sold=False)])
        if dep1_res > dep2_res:
            res_str = f'<td style="background-color: greenyellow">{dep1_res}</td><td>{dep2_res}</td>'
        elif dep1_res < dep2_res:
            res_str = f'<td">{dep1_res}</td><td style="background-color: greenyellow>{dep2_res}</td>'
        else:
            res_str = ''
    if comparison_detail == 4:
        dep1_res = sum([i.price for i in dep1.items.all()])
        dep2_res = sum([i.price for i in dep2.items.all()])
        if dep1_res > dep2_res:
            res_str = f'<td style="background-color: greenyellow">{dep1_res}</td><td>{dep2_res}</td>'
        elif dep1_res < dep2_res:
            res_str = f'<td">{dep1_res}</td><td style="background-color: greenyellow>{dep2_res}</td>'
        else:
            res_str = ''
    if comparison_detail == 5:
        dep1_res = len(dep1.items.filter(is_sold=True))
        dep2_res = len(dep2.items.filter(is_sold=True))
        if dep1_res > dep2_res:
            res_str = f'<td style="background-color: greenyellow">{dep1_res}</td><td>{dep2_res}</td>'
        elif dep1_res < dep2_res:
            res_str = f'<td">{dep1_res}</td><td style="background-color: greenyellow>{dep2_res}</td>'
        else:
            res_str = ''
    if comparison_detail == 6:
        dep1_res = len(dep1.items.filter(is_sold=False))
        dep2_res = len(dep2.items.filter(is_sold=False))
        if dep1_res > dep2_res:
            res_str = f'<td style="background-color: greenyellow">{dep1_res}</td><td>{dep2_res}</td>'
        elif dep1_res < dep2_res:
            res_str = f'<td">{dep1_res}</td><td style="background-color: greenyellow>{dep2_res}</td>'
        else:
            res_str = ''
    if comparison_detail == 7:
        dep1_res = len(dep1.items.all())
        dep2_res = len(dep2.items.all())
        if dep1_res > dep2_res:
            res_str = f'<td style="background-color: greenyellow">{dep1_res}</td><td>{dep2_res}</td>'
        elif dep1_res < dep2_res:
            res_str = f'<td">{dep1_res}</td><td style="background-color: greenyellow>{dep2_res}</td>'
        else:
            res_str = ''
    return mark_safe(
        f'<table id="tb1" width="200" border="1" align="center" cellpadding="4" cellspacing="0" style="margin-top: 10px">'
            f'<tr>'
            f'<td>{dep1}</td>'
            f'<td>{dep2}</td>'
            f'</tr>'
            f'<tr>' +
            res_str +
            '</tr>'
        f'</table>')
