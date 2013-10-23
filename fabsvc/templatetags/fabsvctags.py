from django import template
register = template.Library()

@register.filter
def state_color(value):
    return {
        "running": "success",
        "stoped": "warning",
        "error": "danger",
    }.get(value, "active")
