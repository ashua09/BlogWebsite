from pyexpat import model
from unicodedata import category
from xml.etree.ElementTree import Comment
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy,reverse
from django.views.generic import ListView,DetailView,UpdateView,CreateView,DeleteView
from blog.models import Post,Category,Comment
from blog.forms import PostForm,EditForm,CommentForm
from django.http import HttpResponseRedirect


# Create your views here.
class HomeView(ListView):
    model=Post 
    template_name='blog/home.html'
    ordering=['-published_date']

    def get_context_data(self,*args, **kwargs):
        cat_menu=Category.objects.all()
        context= super(HomeView,self).get_context_data(*args,**kwargs)
        # stuff=get_object_or_404(Post,id=self.kwargs['pk'])
        # total_likes=stuff.total_likes()
        # liked=False
        # if self.likes.filter(id=self.request.user.id).exist():
        #     liked=True
        context['cat_menu']=cat_menu
        # context['total_likes']=total_likes
        # context['liked']=liked
        return context

class PostDetail(DetailView):
    model=Post
    template_name="blog/post_detail.html"

class AddComment(CreateView):
    model=Comment
    form_class=CommentForm
    #fields="__all__"
    template_name='blog/add_comment.html'

    def form_valid(self,form):   #making the user id available for our profile so that when we save the form it save under right user
        form.instance.post_id=self.kwargs['pk']
        return super().form_valid(form)

    success_url=reverse_lazy('blog:home')
    

class AddPost(CreateView):
    model=Post 
    form_class=PostForm
    template_name='blog/add_post.html'
    # fields=('title','body')
    # fields="__all__"
    # success_url=reverse_lazy('blog:home')
class CategoryPost(CreateView):
    model=Category 
    fields='__all__'
    template_name='blog/add_category.html'

class UpdatePost(UpdateView):
    model=Post
    form_class=EditForm
    template_name='blog/update_post.html'

class DeletePost(DeleteView):
    model=Post
    template_name='blog/delete_post.html'
    success_url=reverse_lazy('blog:home')

def CategoryView(request,cats):
    category_post=Post.objects.filter(category=cats)
    return render(request,'blog/category.html',{'cats':cats, 'category_post':category_post})

def CategoryListView(request):
    cat_menu_list=Category.objects.all()    
    context={
        'cat_menu_list':cat_menu_list,
        }
    return render(request,'blog/category_list.html',context=context)

# def LikeView(request,pk):
#     post=get_object_or_404(Post,id=request.POST.get('post_id'))
#     liked=False
#     if post.likes.filter(id=request.user.id).exist():
#         post.likes.remove(request.user)
#         liked=False
#     else:
#         post.likes.add(request.user)
#         liked=True
#     return HttpResponseRedirect(reverse('blog/post_detail',args=[str(pk)]))