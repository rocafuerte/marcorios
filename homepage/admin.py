from marcorios.homepage.models import *
from django.contrib import admin

#class VisiblePlacesInline(admin.StackedInline):
#    model = Place

#class ShowInPlaces(admin.StackedInline):
#    model = Place

#class OnlyTextAdmin(admin.ModelAdmin):
#    inlines = [VisiblePlacesInline]


class MyImageInline(admin.StackedInline):
    model = MyImage
    extra = 2

class TextImageAdmin(admin.ModelAdmin):
    inlines = [MyImageInline]

admin.site.register(TextImage, TextImageAdmin)
admin.site.register(OnlyText)
admin.site.register(Place)
#admin.site.register(MyImage)

