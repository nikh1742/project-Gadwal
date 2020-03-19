import io
from PIL import Image
from django.shortcuts import render
from django.http import HttpResponse
from .models import SareeModel, CollectionModel, CustomerContactModel
from .forms import SareeModelForm, CollectionForm, CustomerContactForm

def home(request):
    """default home page view"""
    return render(request, 'saree_collection/index.html')

def add_new_collection(request):
    """Add new sarees to existing collection items."""
    if request.method == 'POST':
        images_form = SareeModelForm(request.POST, request.FILES)
        # making a list of all uploaded images
        images_list_from_form = request.FILES.getlist('saree_img')
        if images_form.is_valid():
            # getting the collection to which the images are being uploaded to 
            collection = images_form.instance.collection_name
            for f in images_list_from_form:
                file = SareeModel(saree_img=f, collection_name=collection)
                file.save()
        return HttpResponse('Done')
    else:
        form =  SareeModelForm()
    context = {
        'form': form,
    }
    return render(request, 'saree_collection/add_new_collection.html', context)

def collections(request):
    """A default homepage view."""
    return render(request, 'saree_collection/collections.html')

def all_collections(request):
    """All collections view."""
    collections = CollectionModel.objects.all().order_by('-collection_date')
    context = {
        'collections': collections
    }
    return render(request, 'saree_collection/all_collections.html', context)


def sarees_in_collection(request, collection):
    """A view to show all sarees in a particular collection."""
    collection_pk_id = CollectionModel.objects.get(collection_name=collection).id
    sarees = SareeModel.objects.filter(collection_name=collection_pk_id)
    context = {
        'sarees': sarees,
        'collection': collection
    }
    return render(request, 'saree_collection/sarees.html', context)

def CustomerContactModel_view(request):
    fields = CustomerContactForm()
    context = {'fields': fields}
    return render(request, 'saree_collection/CustomerContactModel.html', context)