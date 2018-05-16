from django.http import HttpResponse, HttpResponseRedirect,Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from .forms import PostForm
# from urllib import quote_plus
# Create your views here.

def post_create(request):
   form = PostForm
   # context={'form':form}
   # return render(request, "post_form.html",context)
   # if not request.user.is_staff or not request.user.is_superuser:
   #      raise Http404
   # form = PostForm(request.POST or None, request.FILES or None)
   # if form.is_valid():
   #    instance = form.save(commit=False)
   #    instance.user = request.user
   #    print(form.cleaned_data.get("title"))
   #    instance.save()
   #    #message success
   #    messages.success(request,"Successfully created")
   #    return HttpResponseRedirect(instance.get_absolute_url())
   # else:
   #     messages.error(request,"Unsuccessful")
   if request.method =='POST':
      print(request.POST.get("content"))
      print(request.POST.get("title"))
      Post.objects.create(title="title")
   context ={
    "form": form,}
   return render(request, "post_form.html",context)


def post_home(request):
   queryset = Post.objects.all()
   context = {
      "object_list": queryset,
      "title": "list",}

   return render(request, "post_list.html",context)


def post_detail(request,id):
   instance = get_object_or_404(Post, id=id)
   #share_string = quote_plus(instance.content)
   context={
      "instance":instance,
      "title":instance.title}#instance.title,"share_string":share_string
   return render(request, "post_detail.html",context)


def post_update(request, id=None):
   if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
   instance = get_object_or_404(Post, id=id)
   form = PostForm(request.POST or None,request.FILES or None,instance=instance)
   if form.is_valid():
      instance = form.save(commit=False)
      print(form.cleaned_data.get("title"))
      instance.save()
      # messages
      messages.success(request, "created")
      return HttpResponseRedirect(instance.get_absolute_url())
      context ={
      "title":instance.title,
      "instance":instance,
      "form":form,}
   return render(request, "post_form.html",context)


def post_list(request):
   queryset_list = Post.objects.all().order_by("-timestamp")
   paginator = Paginator(queryset_list, 10)
   page_request_var ="page"
   page =request.GET.get('page')#page_request_var
   try:
      queryset = paginator.page(page)
   except PageNotAnInteger:
      queryset = paginator.page(1)
   except EmptyPage:
      queryset = paginator.page(paginator.num_pages)
   context={
      'queryset_list':queryset_list,
      "object_list":queryset,
      "title":"list",
      "page_request_var":page_request_var}
   return render(request, "new1.html", context)
   #return HttpResponse("<h1>List</h1>")#(request, "post_detail.html",context)


def post_delete(request, id=None):
   if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
   instance = get_object_or_404(Post, id=id)
   instance.delete()
   context={
      "title":'delete'
   }
   messages.success(request, "Deleted")
   return redirect("post:list")
   #return HttpResponseRedirect(instance.get_absolute_url())
   #return render(request, "post_detail.html",context)
   #return HttpResponse("<h1>delete</h1>")


