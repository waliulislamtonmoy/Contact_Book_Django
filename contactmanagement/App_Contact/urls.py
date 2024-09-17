

from django.urls import path
from .views import HomeView,ContactDetailView,ContactAddView,EditContact,DeleteContact,ContactSearchView

urlpatterns = [
   path("",HomeView.as_view(),name="home"),
   path("/details/<int:pk>/",ContactDetailView.as_view(),name='details'),
   path("/create",ContactAddView.as_view(),name='create'),
   path("/updata/<int:pk>/",EditContact.as_view(),name='update'),
   path("/delete/<int:pk>/",DeleteContact.as_view(),name='delete'),
   path('search/', ContactSearchView.as_view(), name='search'),
]
