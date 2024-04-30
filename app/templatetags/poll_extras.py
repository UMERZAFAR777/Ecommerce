from django import template
import math
register = template.Library()


@register.simple_tag

def calculate_price(price,discount):
    if discount == 0 or discount is None:
        return price
    
    progress = price
    progress = price - (price*discount/100)
    return math.floor(progress)

@register.simple_tag
def calculate_bar(total_quantity,availability):
    bar = availability
    bar = availability * (100/total_quantity)

    return math.floor(bar)






