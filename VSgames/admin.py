from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from VSgames.models import Post, User, Tag, Comment, Vote

# Register your models here.

admin.site.register(Post)
admin.site.register(User, UserAdmin)

UserAdmin.fieldsets += (("Custom fields", {"fields": ("nickname",)}),)


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Tag, TagAdmin)
admin.site.register(Comment)
admin.site.register(Vote)
