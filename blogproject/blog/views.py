from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.shortcuts import render_to_response
from blog.models import *

@csrf_exempt
def create_post(request):
    if request.method == 'POST':
        a = request.POST.get('contact_name')
        t = request.POST.get('title')
        article = request.POST.get('post_message')
        p = post(author=a, title=t, bodytext=article)
        p.save()
        return HttpResponse("Saved successfully")
    else:
        return render_to_response('create_post.html')
    
def show_post(request):
    posts = post.objects.all()
    return render_to_response('show_post.html',{'posts':posts})
