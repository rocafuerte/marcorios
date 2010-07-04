from django.db import models

# One should open a page and then se which Placews that should be visible
# Should have som XML-file that defines availables Styles

# Administrator adds these when he sets up the system 
# Is not more the a name. e.g TopBar , LeftMenu , ...
class Place(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name
    

# Its is the WHOLE page that is a showStyle, not just the ""
class ShowStyle(models.Model):
    SHOW_STYLES = (
        ('TI', 'Text and Image'),
        ('TE', 'Only Text'),
        )
    title = models.CharField(max_length=100)
    #style_name = models.CharField(max_length=2,choices=SHOW_STYLES) #e.g TextImage
    order_no = models.IntegerField() # For the menu
    is_published = models.BooleanField()
    pub_date = models.DateTimeField('date published')
    mod_date = models.DateTimeField('date modified')
    visible_places = models.ManyToManyField(Place,related_name='vp') # This has to be restricted. It is set by admin.
    show_in_places = models.ManyToManyField(Place,related_name='sip') # This has to be restricted.
    def __unicode__(self):
        return self.title
    def style_name(self):
        return "no style name yet"

# May not be neded
#class VisiblePlaces(models.Model):
#    show_style = models.ForeignKey(ShowStyle)  # TODO, show all possible syles
#    place = models.ForeignKey(Place)
#    order_no = models.IntegerField()


# GOTTA LIMIT THE PLACES - maybe not so important
# This could be used for: Contact, History, ...
# This is a One-level style
class TextImage(ShowStyle):
    #VISIBLE_PLACES = ()
    #SHOW_IN_PLACES = ()
    title = "hej"
    text = models.TextField()
    #image = models.ForeignKey(MyImage)
    help_text = "This show style concists of a image and a text"
    def style_name(self):
        return "TextImage"

class MyImage(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to="images/")
    ti = models.ForeignKey(TextImage)

 
class OnlyText(ShowStyle):
    #VISIBLE_PLACES = ()
    #SHOW_IN_PLACES = ()    
    text = models.TextField()
    help_text = "This show style concists of a text"
    def style_name(self):
        return "Text"
