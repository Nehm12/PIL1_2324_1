from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.decorators import login_required

# Create your views here.


# def listU(request):
#     lu= User.objects.all()
    
#     context = {
#         'lu':lu,
#     }
     
#     return render(request, 'list.html',context)
# chat/views.py



@login_required
def user_list(request):
    users = User.objects.exclude(username=request.user.username)
    return render(request, 'chat/user_list.html', {'users': users})


# chat/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message

@login_required
# def private_chat(request, username):
#     other_user = get_object_or_404(User, username=username)
#     messages = Message.objects.filter(
#         (models.Q(sender=request.user) & models.Q(receiver=other_user)) |
#         (models.Q(sender=other_user) & models.Q(receiver=request.user))
#     ).order_by('timestamp')
#     return render(request, 'chat/private_chat.html', {'other_user': other_user, 'messages': messages})
def private_chat(request, username):
    other_user = User.objects.get(username=username)
    messages = Message.objects.filter(sender=request.user, receiver=other_user) | Message.objects.filter(sender=other_user, receiver=request.user)
    messages = messages.order_by('timestamp')
    return render(request, 'chat/private_chat.html', {
        'other_user': other_user,
        'messages': messages
    })