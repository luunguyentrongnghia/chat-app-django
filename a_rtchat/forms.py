from django.forms import ModelForm
from django import forms
from .models import *

class ChatmessageCreateForm(ModelForm):
    class Meta:
        #  Đây là mô hình mà biểu mẫu này được liên kết với. Trong trường hợp này, mô hình là GroupMessage.
        model = GroupMessage
        # Đây là danh sách các trường (field) của mô hình mà biểu mẫu này sẽ hiển thị. Trong trường hợp này, chỉ có trường body được hiển thị.
        fields = ['body']
        # forms.Textarea được sử dụng để tạo một textarea (khu vực nhập văn bản) cho trường body
        widgets = {
            'body': forms.TextInput(attrs={'placeholder': 'Add message...', 'class': 'p-4 text-black', 'maxlength': '300','autofocus': True}),
        }
        