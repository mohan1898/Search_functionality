from django.urls import path
from searchbar import views
urlpatterns = [
    path('',views.index,name='index'),
    path('search',views.search,name='search'),
]
