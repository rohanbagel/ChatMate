from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import * 
from .forms import * 

# Create your views here.

@login_required
def chat_view(request):
    chat_group = get_object_or_404(ChatGroup, group_name='public-chat')
    chat_messages = chat_group.chat_messages.all()[:30]
    form = ChatmessageCreateForm()
    
    if request.method == 'POST':
        form = ChatmessageCreateForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.group = chat_group
            message.save()
            
            if request.headers.get('HX-Request'):
                return render(request, 'a_realtimechat/partials/chat_message_p.html', {'message': message})
            return redirect('home')
            
    return render(request, 'a_realtimechat/chat.html', {'chat_messages': chat_messages, 'form': form})

