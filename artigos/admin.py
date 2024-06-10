from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import User, Post, PostImage, Comment, Rating

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('user','image_profile_preview')
    ordering = ('user',)
    search_fields = ('user',)

    def image_profile_preview(self, obj):
        if obj.image_profile and hasattr(obj.image_profile, 'url'):
            return mark_safe('<img src="{url}" width="100" height="100" />'.format(url=obj.image_profile.url))
        else:
            return "-"

class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo','texto','user')
    ordering = ('user',)
    search_fields = ('user',)

class PostImageAdmin(admin.ModelAdmin):
    list_display = ('post','image_preview')
    ordering = ('post',)
    search_fields = ('post',)

    def image_preview(self, obj):
        return mark_safe('<img src="{url}" width="100" height="100" />'.format(url=obj.image_post.url))
    image_preview.short_description = 'Imagem Preview'

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','texto','post')
    ordering = ('user','post')
    search_fields = ('user',)

    class RatingInline(admin.TabularInline):
        model = Rating
        extra = 0

    inlines = [RatingInline]


admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostImage, PostImageAdmin)
admin.site.register(Comment, CommentAdmin)