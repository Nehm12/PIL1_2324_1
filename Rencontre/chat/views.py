from django.shortcuts import get_object_or_404, render
from .models import Message, list_user
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@login_required
def Liste_users(request):
    users = User.objects.exclude(username=request.user)
    return render(request, 'chat/Liste.html', {'users': users})

@login_required
def room(request, username):
    user2 = get_object_or_404(User, username=username)
    user1 = request.user
    newroom = list_user.objects.filter(list=user1).filter(list=user2).first()

    if not newroom:
        newroom = list_user.objects.create()
        newroom.list.add(user1, user2)
        newroom.save()
    
    messages = Message.objects.filter(newroom=newroom).order_by('timestamp')

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(newroom=newroom, user1=user1, user2=user2, content=content)
            return JsonResponse({'status': 'ok'})  # Réponse JSON pour la requête AJAX
    
    context = {
        'newroom': newroom,
        'user2': user2,
        'messages': messages,
    }
    return render(request, 'chat/room.html', context)

@login_required
@csrf_exempt
def load_messages(request):
    if request.method == 'GET':
        room_name = request.GET.get('room_name')
        newroom = get_object_or_404(list_user, id=room_name)
        messages = Message.objects.filter(newroom=newroom).order_by('timestamp').values('content', 'user1__username', 'timestamp')
        return JsonResponse({'messages': list(messages)})

@login_required
@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        room_name = request.POST.get('room_name')

        newroom = get_object_or_404(list_user, id=room_name)
        user1 = request.user
        user2 = newroom.list.exclude(id=user1.id).first()
        
        if content:
            Message.objects.create(newroom=newroom, user1=user1, user2=user2, content=content)
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid data'})