from django.db import models
from stdimage import StdImageField

class CollectionModel(models.Model):
    """collection model"""
    collection_name = models.CharField(max_length=50)
    collection_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.collection_name


# changing the default upload location
def upload_path(instance, filename):
    """change upload path to a path based on the CollectionModel items."""
    return 'collection_{0}/{1}'.format(instance.collection_name, filename)

class SareeModel(models.Model):
    """model to manage individual sarees."""
    # using stdimage extension to resize the uploaded image before saving.
    saree_img = StdImageField(upload_to=upload_path,
                        variations={'thumbnail': (500, 500)})
    collection_name = models.ForeignKey(to=CollectionModel, on_delete=models.CASCADE)

class CustomerContactModel(models.Model):
    """Model to manage customer queries."""
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    message = models.TextField()
    