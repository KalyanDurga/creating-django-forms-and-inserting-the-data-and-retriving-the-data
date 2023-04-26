from django import forms
from app.models import *

class Topicform(forms.Form):
    topic_name=forms.CharField(max_length=50)


class Webpageform(forms.Form):
    topic_name=forms.CharField(max_length=50)
    name=forms.CharField(max_length=50)
    url=forms.URLField()


class Accessrecordform(forms.Form):
    name=forms.CharField(max_length=50)
    author=forms.CharField(max_length=50)
    date=forms.DateField()