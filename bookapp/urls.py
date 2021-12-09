from django.urls import path
from . import views
urlpatterns =[
    path('',views.home,name='home'),
    path('detail/<int:id>/',views.detail,name='detail'),
    path('add/',views.add,name='add'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('search/',views.search,name='search'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
]