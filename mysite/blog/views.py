from django.shortcuts import render
from django.utils import timezone
from .models import Post

"""
A view is a place where we put the "logic" of our application.
It will request information from the model you created before
and pass it to a template. 
We'll create a template in the next chapter. 
Views are just Python functions that are a 
little bit more complicated
"""

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request,'blog/post_list.html',{'posts':posts})
	#last parameter,add some things for the tmemplate to use .
	#

# Create your views here.
