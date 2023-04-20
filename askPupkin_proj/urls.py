from django.contrib import admin
from django.urls import path
from askPupkin_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hot/', views.hot, name='hot'),
    path('tag/<str:tag_name>/', views.tag_question, name="tag"),
    path('question/<int:question_id>/', views.question, name='question'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('ask/', views.ask, name='ask'),
    path('settings/<int:user_id>/', views.settings, name='settings'),
    path('admin/', admin.site.urls),
]
