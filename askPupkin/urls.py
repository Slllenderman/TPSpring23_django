from django.contrib import admin
from django.urls import path, include
from askPupkin_views import views

urlpatterns = [
    path('', views.index, name='index'),
    path('question/<int:question_id>/', views.question_page, name='question_page'),
    path('ask/', views.ask, name='ask'),
    path('settings/<int:user_id>/', views.settings, name='settings'),
    path('auth/login/', views.login, name='login'),
    path('auth/registration/', views.registration, name='registration'),
    path('auth/logout/', views.logout, name='logout'),
    path('admin/', admin.site.urls),
]
