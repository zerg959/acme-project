from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views


app_name = 'users_app'

urlpatterns = [
    path('', views.users_list, name='users_list'),
    # path('<slug:username>/', views.user_profile, name='user_profile'),
    path('logout/',
         LogoutView.as_view(template_name="users/logged_out.html"),
         name='logout'
         ),
]
