from django.contrib import admin
from .models import Post, Post_view, Post_comment
# Register your models here.


class Postadmin(admin.ModelAdmin):
    readonly_fields = ('view_count', 'total_comments')


admin.site.register(Post, Postadmin)
admin.site.register(Post_view)
admin.site.register(Post_comment)