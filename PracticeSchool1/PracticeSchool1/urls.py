from django.urls import include, re_path
import MyApp1.views
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Uncomment the next line to enable the admin:
   path('admin/', admin.site.urls),
   re_path(r'^home$', MyApp1.views.home, name='home'),
   re_path(r'^$', MyApp1.views.home, name='index'),
   re_path(r'^$', MyApp1.views.index, name='test'),
   re_path(r'input', MyApp1.views.input_view, name='input'),
   path('delete/<int:teacher_id>/', MyApp1.views.delete_teacher, name='delete_teacher'), # delete teachers
   path('signup/', MyApp1.views.signup_view, name='signup'), #Signup Page
   path('login/', auth_views.LoginView.as_view(template_name='MyApp1/login.html'), name='login'),
   path("logout/", auth_views.LogoutView.as_view(), name="logout"),
   path('home/', MyApp1.views.home, name='home'),
   path('report/', MyApp1.views.report, name='report'),
   path('test/', MyApp1.views.index, name='test'),
   path('outline/', MyApp1.views.outline, name='outline'),
   


]

admin.site.site_header = "BSSS administration"
admin.site.index_title = "Welcome to BSSS"
admin.site.site_title = "BSSS Admin"
