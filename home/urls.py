from django.contrib import admin
from django.urls import path,include
from home import views


# django admin header customisation
admin.site.site_header= "Developer Aaditya_Mohit"
# ye heading ko change krega
admin.site.site_title="Welcome to Aaditya's Home"
# ye andr ke jo title head hota h usko change krega
admin.site.index_title=" Welcome to this portal"
# ye index ko is name se dikhaaega waha

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', views.home, name='home'),
      path('about/', views.about, name='about'),
       path('contact/', views.contact, name='contact'),
        path('projects/', views.projects, name='projects')
]
 
