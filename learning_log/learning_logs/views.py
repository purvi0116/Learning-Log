from django.shortcuts import render
from .models import Topic, Entry
from .forms import TopicForm,EntryForm
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
	"""The Home Page for Learning Log"""
	return render(request,'learning_logs/home.html')

@login_required
def topics(request):
	"""Show all topics."""
	topics = Topic.objects.filter(owner=request.user).order_by('date_added')
	context={'topics':topics}
	return render(request,'learning_logs/topics.html',context)	

@login_required
def topic(request, topic_id):
	"""Show a single topic and all its entries"""
	topic = Topic.objects.get(id=topic_id)
	#Make sure theat the topic belongs to the current owner
	check_topic_owner(request, topic)
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic':topic,'entries':entries}
	return render(request,'learning_logs/topic.html',context)	

@login_required
def new_topic(request):
	if request.method=='POST':
		topic=request.POST['topic']
		topic_obj = Topic(text=topic)
		topic_obj.save()
		return HttpResponseRedirect('/topics')

	return render(request,'learning_logs/new_topic.html')	

@login_required
def new_topic2(request):
	"""Add a new topic."""
	if request.method!='POST':
		#No data submitted;create a blank form.
		form = TopicForm()
	else:
		#POST data submitted; process data
		form = TopicForm(request.POST)
		if form.is_valid():
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()
			return HttpResponseRedirect('/topics')	
	context = {'form' : form}
	return render(request,'learning_logs/new_topic2.html',context)		

@login_required
def new_entry(request,topic_id):
	topic = Topic.objects.get(id=topic_id)
	check_topic_owner(request,topic)
	if request.method!='POST':
		form =EntryForm()
	else:
		form = EntryForm(request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)	
			new_entry.topic = topic
			
			new_entry.save()
			return HttpResponseRedirect('/topics/'+topic_id)
	callBack_url = '/new_entry/'+topic_id+'/'		
	context = {'topic': topic, 'form': form, 'callBack_url':callBack_url}
	return render(request, 'learning_logs/new_entry.html',context)		

@login_required
def edit_entry(request,entry_id):
	"""Edit an existing entry"""
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic
	check_topic_owner(request,topic)
	if request.method!='POST':
		# Initial request; pre-fill form with the current entry.
		form = 	EntryForm(instance=entry)
	else:
		# POST data submitted; process data.
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/topics/'+str(topic.id)+'/')	
	context={'form':form, 'topic':topic, 'entry':entry}
	return render(request,'learning_logs/edit_entry.html',context)	

@login_required
def edit_topic(request,topic_id):
	"""Edit an existing entry"""
	topic = Topic.objects.get(id=topic_id)
	check_topic_owner(request,topic)
	if request.method!='POST':
		# Initial request; pre-fill form with the current topic.
		form = 	TopicForm(instance=topic)
	else:
		# POST data submitted; process data.
		form = TopicForm(instance=topic, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/topics/')	
	context={'form':form, 'topic':topic}
	return render(request,'learning_logs/edit_topic.html',context)	

@login_required
def delete_topic(request, topic_id):
	topic = Topic.objects.get(id=topic_id)
	check_topic_owner(request, topic)
	topic.delete()
	return HttpResponseRedirect('/topics/')	

@login_required
def delete_entry(request, entry_id):
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic
	check_topic_owner(request, topic)
	entry.delete()
	topic_id = topic.id
	return HttpResponseRedirect('/topics/'+str(topic_id)+'/')

def check_topic_owner(request,topic):
	if topic.owner!=request.user:
		raise Http404	