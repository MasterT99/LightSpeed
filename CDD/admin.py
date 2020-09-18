
from django.contrib import admin
from CDD.models import User,Claims,Chat,Circular,PartCost

# Register your models here.
admin.site.register(User)
admin.site.register(Claims)
admin.site.register(Chat)
admin.site.register(Circular)
admin.site.register(PartCost)
