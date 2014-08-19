from django.db import models
from django_extensions.db.fields import AutoSlugField

class Snippet(models.Model):

    title = models.CharField(max_length=128)
    text = models.TextField()
    
    slug = AutoSlugField(populate_from="title", unique=True)
    
    created_at = models.DateTimeField(auto_now=True)
    modified_by = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        db_table = "snippet"
