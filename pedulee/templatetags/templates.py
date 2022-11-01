from django import template

register = template.Library()


@register.inclusion_tag("_components/navbar.html")
def navbar():
    return {}


@register.inclusion_tag("_components/cards/project.html")
def card_project(title, description, link, image, alt):
    return {
        'title': title,
        'description': description,
        'link': link,
        'image': image,
        'alt': alt
    }
