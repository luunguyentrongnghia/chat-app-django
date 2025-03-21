from django.shortcuts import render
from django.shortcuts import get_object_or_404,redirect
from .models import *
from .forms import ChatmessageCreateForm

# Create your views here.
def chat_view(request):
    # get_object_or_404 sử dụng để lấy một đối tượng từ cơ sở dữ liệu. Nếu đối tượng không tồn tại, hàm sẽ trả về một trang lỗi 404.
    chat_groups = get_object_or_404(ChatGroup,group_name='public-chat')
    # [:30]: Sử dụng slicing để lấy 30 tin nhắn gần nhất từ kết quả trên
    chat_messages = chat_groups.chat_messages.all()
    form = ChatmessageCreateForm()
    if request.method == 'POST':
        # Đây là một cách để tạo một biểu mẫu (form) từ yêu cầu POST.
        form = ChatmessageCreateForm(request.POST)
        if form.is_valid():
            print(form.is_valid())
            #  Đây là một cách để lưu trữ dữ liệu nhập vào vào cơ sở dữ liệu. Tuy nhiên, commit=False có nghĩa là dữ liệu sẽ không được lưu trữ ngay lập tức, mà sẽ được lưu trữ sau khi thực hiện một số hành động khác.
            message = form.save(commit=False)
            message.author = request.user
            message.group = chat_groups
            message.save()
            #  Đây là một cách để chuyển hướng người dùng đến trang chủ
            # return redirect('home')
    #  sử dụng hàm render để trả về một trang HTML với dữ liệu từ biến chat_messages.
    return render(request, 'a_rtchat/chat.html',{'chat_messages':chat_messages,'form':form})
