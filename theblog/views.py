from django.http.response import HttpResponseRedirect
from .models import Category, Post,Comment
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import PostForm,EditForm,CommentForm
from django.urls import reverse_lazy,reverse

# Create your views here.


# def home(request):
#     return render(request,'home.html',{})
def CategoryView(request,cats):
    catergory_post= Post.objects.filter(category=cats.replace('-',' '))
    return render(request,'categories.html',{'cats':cats.title().replace('-',' '),'category_post':catergory_post})

def LikeView(request,pk):
    post = get_object_or_404(Post,id=request.POST.get('post-id'))
    liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked=True
        
    return HttpResponseRedirect(reverse('article-detail',args=[str(pk)]))


def CategoryListView(request):
    cat_menu_list= Category.objects.all()
    return render(request,'category_list.html',{'cat_menu_list':cat_menu_list})

class HomeView(ListView):
    model=Post
    template_name='home.html'
    # ordering=['-id']
    ordering=['-post_date']

    def get_context_data(self, *args,**kwargs):
        category_menu= Category.objects.all()
        context= super(HomeView,self).get_context_data(*args,**kwargs)
        context['category_menu']=category_menu
        return context

class ArticleDetailView(DetailView):
    model=Post
    template_name='article_detail.html'
    def get_context_data(self, *args,**kwargs):
        category_menu= Category.objects.all()
        post_likes= get_object_or_404(Post,id=self.kwargs['pk'])

        liked=False
        if post_likes.likes.filter(id=self.request.user.id).exists():
            liked=True
        total_likes= post_likes.total_likes()
        context= super(ArticleDetailView,self).get_context_data(*args,**kwargs)
        context['category_menu']=category_menu
        context['total_likes']=total_likes
        context['liked']=liked
        return context

class AddPostView(CreateView):
    model=Post
    form_class=PostForm
    template_name='add_post.html'
    # fields='__all__'
class AddCommentView(CreateView):
    model=Comment
    form_class=CommentForm
    template_name='add_comment.html'
    ordering=['-date_added']
    success_url=reverse_lazy('home')
    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


class AddCategoryView(CreateView):
    model=Category
    template_name='add_category.html'
    fields="__all__"

class UpdatePostView(UpdateView):
    model=Post
    form_class=EditForm
    template_name='update_post.html'
    # fields='__all__'
class DeletePostView(DeleteView):
    model=Post
    template_name='delete_post.html'
    success_url=reverse_lazy('home')
    # fields='__all__'