from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect
from .models import Meeting, Room

MeetingForm = modelform_factory(Meeting, exclude=[])


def details(request, meeting_id):
    meeting = get_object_or_404(Meeting, pk=meeting_id)
    return render(request, 'meetings/details.html',
                  {'meeting': meeting})


def rooms(request):
    return render(request, 'meetings/rooms.html',
                  {'rooms': Room.objects.all()})


def new(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MeetingForm()
    return render(request, 'meetings/new.html', {'form': form})
