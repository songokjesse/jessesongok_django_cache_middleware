from django.urls import path
from django.conf.urls import url


from . import views
from .views import view_cached_product


urlpatterns =[
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    url(r'^cache/', view_cached_product),
]