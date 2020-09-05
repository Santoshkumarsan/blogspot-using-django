from django.contrib import admin
from .models import Post,Comment,Contactus
# Register your models here.
# for main post admin interface
class PostAdmin(admin.ModelAdmin):
    list_display=['title','author','created','status']
    prepopulated_fields={'slug':('title',)}
    list_filter=('status','author','created')
    search_fields=('title','body')
    raw_id_fields=('author',)
    ordering=['status','publish']
    date_hierarchy='publish'

# for  comments admin interface.

class CommentAdmin(admin.ModelAdmin):
    list_display=('name','email','post','body','created','updated','active')
    list_filter=('active','created','name')
    search_fields=('name','email','body')



class ContactusAdmin(admin.ModelAdmin):
    list_display=('Name','Email','Mobile','Feedback','Time')


admin.site.register(Contactus,ContactusAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Post,PostAdmin)






