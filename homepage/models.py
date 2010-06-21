from django.db import models 

class ShowStyle(models.Model):
    name = models.CharField(max_length=100)

# Administrator adds these when he sets up the system 
class Place(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name    
    # Define visible styles here instead of at the specific style
    #visible = models.ManyToManyField(TextImage)

# This could be used for: Contact, History, ...
class TextImage(ShowStyle):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to="images/")
    # This in wrong    
    showAt = models.ManyToManyField(Place,through='ShowAt') # This has to be restricted

class ShowAt(models.Model):
    show_style = models.ForeignKey(TextImage)  # ShowStyle
    place = models.ForeignKey(Place)
    order_no = models.IntegerField()
    #language = 
    
