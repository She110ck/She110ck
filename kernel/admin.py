from django.contrib import admin


# Register your models here.
from kernel.models import PostData, Hashtag, Dictonary, Lang, PostType


class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'image', 'content', 'date', 'author', 'post_type', 'post_lang']
    list_display = ['title', 'date', 'post_type']
    list_display_links = ['title']
    list_filter = ['date']
    search_fields = ['title', 'content']


class HashtagAdmin(admin.ModelAdmin):
    fields = ['tag', 'connects']
    list_display = ['tag']
    list_display_links = ['tag']
    search_fields = ['tag']


class DictonaryAdmin(admin.ModelAdmin):
    fields = ['word', 'mean', 'photo', 'lang']
    list_display = ['word', 'mean', 'lang']
    list_display_links = ['word']
    list_filter = ['lang']
    search_fields = ['word', 'mean']


class LangAdmin(admin.ModelAdmin):
    fields = ['short_name', 'full_name']
    list_display = ['short_name', 'full_name']
    list_display_links = ['short_name']


class PostTypeAdmin(admin.ModelAdmin):
    fields = ['name', 'description']
    list_display = ['name']
    list_display_links = ['name']


admin.site.register(PostData, PostAdmin)
admin.site.register(Hashtag, HashtagAdmin)
admin.site.register(Dictonary, DictonaryAdmin)
admin.site.register(Lang, LangAdmin)
admin.site.register(PostType, PostTypeAdmin)
