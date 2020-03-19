from django.contrib import admin
from .models import CollectionModel, SareeModel, CustomerContactModel

# Registering my models
admin.site.register(CollectionModel)
admin.site.register(SareeModel)
admin.site.register(CustomerContactModel)