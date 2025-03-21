from django.contrib import admin
from .models import ChatGroup, GroupMessage
# Register your models here.
# quản lý data các bảng này trong admin
admin.site.register(ChatGroup)
admin.site.register(GroupMessage)