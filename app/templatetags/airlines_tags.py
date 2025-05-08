from django import template
from ..models import AirlinesList, Information, Slider

register = template.Library()

@register.inclusion_tag('airlines.html')
def render_airlines_section():
    try:
        info = Information.objects.latest('id')
    except Information.DoesNotExist:
        info = None

    airlines_list = AirlinesList.objects.all()
    images = Slider.objects.filter(is_active=True).order_by('-created_at')

    return {
        'info': info,
        'images': images,
        'airlines_list': airlines_list
    }
