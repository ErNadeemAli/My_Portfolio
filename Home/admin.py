from django.contrib import admin
from .models import OurUser

# Register your models here.

@admin.register(OurUser)
class OurUserAdmin(admin.ModelAdmin):   
    list_display=['first_name','last_name','email','number','option','message']
     
 
