from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import SareeModel, CollectionModel, CustomerContactModel
from .forms import SareeModelForm, CollectionForm, CustomerContactForm, SecSareeModelForm
from django.contrib.auth.decorators import login_required

def home(request):
    """default home page view"""
    return render(request, 'saree_collection/index.html')

@login_required(login_url="/admin")
def add_new_collection(request):
    """creat a new collection and add new sarees to it."""
    if request.method == 'POST':
        images_form = SareeModelForm(request.POST, request.FILES)
        # making a list of all uploaded images
        images_list_from_form = request.FILES.getlist('saree_img')
        if images_form.is_valid():
            collection_name = datetime.now().strftime("%B")
            # crete new collection entry based on current month
            if collection_name not in [i.collection_name for i in CollectionModel.objects.all()]:
                collection = CollectionModel(collection_name = collection_name)
                collection.save()
            collection_instance = CollectionModel.objects.get(collection_name = collection_name)
            # save all the uploaded file to the new collection created
            for f in images_list_from_form:
                file = SareeModel(saree_img=f, collection_name = collection_instance)
                file.save()
        return HttpResponse('Done')
    else:
        form =  SareeModelForm()
    context = {
        'form': form,
    }
    return render(request, 'saree_collection/add_new_collection.html', context)

@login_required(login_url="/admin")
def add_to_collection(request):
    """Add new sarees to existing collection"""
    if request.method == 'POST':
        images_form = SecSareeModelForm(request.POST, request.FILES)
        # making a list of all uploaded images
        images_list_from_form = request.FILES.getlist('saree_img')
        if images_form.is_valid():
            # getting the collection to which the images are being uploaded to 
            collection_instance = images_form.instance.collection_name
            for f in images_list_from_form:
                file = SareeModel(saree_img=f, collection_name = collection_instance)
                file.save()
        return HttpResponse('Done')
    else:
        form =  SecSareeModelForm()
    context = {
        'form': form,
    }
    return render(request, 'saree_collection/add_to_collection.html', context)

def collections(request):
    """A default homepage view."""
    return render(request, 'saree_collection/home.html')

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
    return render(request, 'saree_collection/coll_sarees.html', context)

def customer_contact_form_view(request):
    if request.method == 'POST':
        form = CustomerContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Thanks for showing interest. We will get back to you.")
        else:
            return HttpResponse("invalid details")
    form = CustomerContactForm()
    context = {'form': form}
    return render(request, 'saree_collection/CustomerContactModel.html', context)

def all_sarees(request):
    sarees = SareeModel.objects.all()
    context = {
        'sarees': sarees
    }
    return render(request, 'saree_collection/all_sarees.html', context)