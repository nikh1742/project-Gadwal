from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

app_name = 'sar_coll'
urlpatterns = [
    path('', views.collections, name='home'),
    path('add_new_collection/', views.add_new_collection, name='add_coll'),
    path('all_collections/', views.all_collections,name='all_coll'),
    path('collections/', views.collections,name='collections'),
    path('all_collections/<str:collection>/', views.sarees_in_collection, name='saree_coll'),
    path('customer_contact/', views.CustomerContactModel_view, name='cust_cont'),
]



urlpatterns += staticfiles_urlpatterns()



urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
