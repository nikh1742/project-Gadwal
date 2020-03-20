from django import template
from saree_collection.forms import CustomerContactForm
from saree_collection.models import CollectionModel, SareeModel

register = template.Library()

@register.simple_tag
def contact_form():
    """template tag of contact form on all pages"""
    return CustomerContactForm()

@register.simple_tag
def collection_thumbnail(collection_name):
    """template tag to display thumbnail of a collection.
    It is selected by the first image from the filtered query"""
    collection = CollectionModel.objects.get(collection_name=collection_name)
    thumb = SareeModel.objects.filter(collection_name=collection.id)[0].saree_img
    return thumb

@register.simple_tag
def number_of_items(collection_name):
    """template tag to return the number of SareeModel items
    associated with a particular collection"""
    collection = CollectionModel.objects.get(collection_name=collection_name)
    count = len(SareeModel.objects.filter(collection_name=collection.id))
    return count

@register.simple_tag
def reduced_collection_items():
    """template tag to return 3 random CollectionModel items"""
    collections = CollectionModel.objects.all().order_by('?')[:3]
    return collections