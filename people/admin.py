
# coding: utf-8
from django.contrib import admin
from .models import Member


class MemberAdmin(admin.ModelAdmin):
    fields = ['name', 'email', 'description', 'image', 'image_tag']
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        return u'<img src="%s" width="100" />' % obj.image.url

    image_tag.short_description = ''
    image_tag.allow_tags = True


admin.site.register(Member, MemberAdmin)
