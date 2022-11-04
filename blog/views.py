from django.shortcuts import render,get_object_or_404
from django.views.generic import (ListView,
DetailView,
UpdateView,
CreateView,
DeleteView)
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
import tkinter
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def drawchart():
        root = tkinter.Tk() 
        canvas = root.Canvas(root, width=400, height=500)
        canvas.pack()
        blackline = canvas.create_line (0, 0, 200, 0)
        root.mainloop()
        return blackline



def Home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)

class PostListView(ListView):
    model = Post
    template_name='blog/home.html'
    context_object_name='posts'
    ordering= ['-date_posted']
    paginate_by= 3

class UserPostListView(ListView):
    model = Post
    template_name='blog/user_posts.html'
    context_object_name='posts'
    paginate_by= 3

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')



class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields=['title','content']

    def form_valid(self,form):
        form.instance.author= self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields=['title','content']

    def form_valid(self,form):
        form.instance.author= self.request.user
        return super().form_valid(form)
    
    def test_func(self) :
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url='/'

    def test_func(self) :
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False


def About(request):
    return render(request,'blog/about.html',{'title':'About'})

