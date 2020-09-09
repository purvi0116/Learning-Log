from django import forms

from .models import Topic,Entry

class TopicForm(forms.ModelForm):  #https://stackoverflow.com/questions/2303268/djangos-forms-form-vs-forms-modelform
	class Meta:
		model = Topic
		fields = ['text']
		labels = {'text': ''}

class EntryForm(forms.ModelForm): 
	class Meta:
		model = Entry
		fields = ['text']
		labels = {'text': ''}		
		widgets = {'text': forms.Textarea(attrs={'cols' : 80})}