from django.contrib import admin
from .models import PictureFolder, AllPictures, PictureComment
# Register your models here.


admin.site.register(PictureFolder)
admin.site.register(AllPictures)
admin.site.register(PictureComment)
