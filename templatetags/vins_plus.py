from django import template
from vins.models import Category, Tag, Vin


register = template.Library()


@register.inclusion_tag('mytag-list.html')
def get_tag_list():
    return {'tags': Tag.objects.all(), 'counter': Tag.objects.filter().count()}


@register.inclusion_tag('mycategory-list.html')
def get_category_list():
    return {'cats': Category.objects.all(), 'counter': Category.objects.filter().count()}


# compter le nb de Vins
@register.simple_tag
def total_vins():
    return Vin.objects.all().count()

@register.inclusion_tag('score.html')
def show_score_vins():
    # retrouver les scores pour chaque id
    vin_list_score = Vin.objects.filter('score') #Vin.objects.order_by('score')
    return {'vin_list_score':  vin_list_score  }



