import os
import uuid
import rarfile
import fotoksu.settings
from datetime import datetime
from django.contrib import admin
from django.core.files.base import ContentFile
from .models import About, Album, Lightbox, Priceofwork, Specialoffers
from .forms import AlbumForm
# Register your models here.
from PIL import Image

@admin.register(About)
class AboutModelAdmin(admin.ModelAdmin):
    list_display = ('id', )

@admin.register(Album)
class AlbumModelAdmin(admin.ModelAdmin):
    form = AlbumForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'thumb')
    list_filter = ('created',)

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            album = form.save(commit=False)
            album.modified = datetime.now()
            album.save()

            if form.cleaned_data['zip']:

                zip = rarfile.RarFile(form.cleaned_data['zip'])
                for filename in sorted(zip.namelist()):

                    file_name = os.path.basename(filename)
                    if not file_name:
                        continue

                    data = zip.read(filename)
                    contentfile = ContentFile(data)

                    img = Lightbox()
                    img.album = album
                    img.alt = filename
                    filename = '{0}{1}.jpg'.format(album.slug, str(uuid.uuid4())[-13:])
                    img.image.save(filename, contentfile)
                
                    filepath = '{0}/albums/{1}'.format(fotoksu.settings.MEDIA_ROOT, filename)
                    with Image.open(filepath) as i:
                        img.width, img.height = i.size

                    img.thumb.save('thumb-{0}'.format(filename), contentfile)
                    img.save()
                zip.close() 
            super(AlbumModelAdmin, self).save_model(request, obj, form, change)

# In case image should be removed from album.
@admin.register(Lightbox)
class LightboxModelAdmin(admin.ModelAdmin):
    list_display = ('alt', 'album')
    list_filter = ('album', 'created')
    
@admin.register(Priceofwork)
class PriceofworkModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    
@admin.register(Specialoffers)
class SpecialoffersModelAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_filter = ('created', )