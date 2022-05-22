from django.shortcuts import get_object_or_404, render
from .models import Meeting, Meeting Minutes, Resource, Event
from django.urls import reverse_lazy


def index(request):
    return render(request, 'club/index.html')

def meeting(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'club/meeting.html', {'meeting_list': meeting_list})  

def meetingDetail(request, id):
    meeting=get_object_or_404(Product, pk=id)
    return render(request, 'club/meetingdetail.html', {'meeting': Meeting})  
