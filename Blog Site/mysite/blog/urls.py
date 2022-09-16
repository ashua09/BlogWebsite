from django.urls import path
from .import views

app_name='blog'

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('detail/<int:pk>',views.PostDetail.as_view(),name='post_detail'),
    path('add_post',views.AddPost.as_view(),name='add_post'),
    path('detail/<int:pk>/add_comment',views.AddComment.as_view(),name='add_comment'),
    path('add_category',views.CategoryPost.as_view(),name='add_category'),
    path('detail/update/<int:pk>',views.UpdatePost.as_view(),name='update_post'),
    path('detail/<int:pk>/delete',views.DeletePost.as_view(),name='delete_post'),
    path('category/<str:cats>/',views.CategoryView,name='category'),
    path('category_list/',views.CategoryListView,name='category_list'),
    
]
