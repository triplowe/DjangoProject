from django.shortcuts import render, redirect
from .forms import TopicForm, EntryForm
from .models import Topic

# Create your views here.
def index(request):
    return render(request, 'MainApp/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request, 'MainApp/topics.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.all()
    context = {'topic':topic, 'entries':entries}
    return render(request, 'MainApp/topic.html', context)

def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)

        if form.is_valid():
            form.save()

            return redirect('MainApp:topics')

    context =  {'form':form} #context passes a dict to give the template data
    return render(request, 'MainApp/new_topic.html', context)

def new_entry(request):
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)

        if form.is_valid():
            form.save()

            return redirect('MainApp:topic')

    context =  {'form':form}
    return render(request, 'MainApp/new_entry.html', context)