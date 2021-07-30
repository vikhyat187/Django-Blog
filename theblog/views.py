from .models import Category, Post
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import PostForm,EditForm
from django.urls import reverse_lazy
# Create your views here.


# def home(request):
#     return render(request,'home.html',{})
def CategoryView(request,cats):
    catergory_post= Post.objects.filter(category=cats.replace('-',' '))
    return render(request,'categories.html',{'cats':cats.title().replace('-',' '),'category_post':catergory_post})

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
        context= super(ArticleDetailView,self).get_context_data(*args,**kwargs)
        context['category_menu']=category_menu
        return context

class AddPostView(CreateView):
    model=Post
    form_class=PostForm
    template_name='add_post.html'
    # fields='__all__'
    # fields=['title','body','title_tag']

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