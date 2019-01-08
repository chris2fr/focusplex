from django import template

class TaskLevelCounter:
    counter = 1

register = template.Library()

@register.filter(is_safe=True)
def level(value):
    return TaskLevelCounter.counter



# @register.simple_tag
# def levelout():
#    return TaskLevelCounter.counter

@register.simple_tag
def levelup():
    # retval = counter
    TaskLevelCounter.counter += 1
    return ""

@register.simple_tag
def levelone():
    # retval = counter
    TaskLevelCounter.counter = 1
    return ""