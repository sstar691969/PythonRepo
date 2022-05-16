from django.shortcuts import get_object_or_404, render
from .models import Meeting 
def index(request):
    return render(request, 'club/index.html')

def meeting(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'club/meeting.html', {'meeting_list': meeting_list})  

