"""
URL configuration for learndjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from demoapp import views
# Step 1
from django.views.generic.base import TemplateView,RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("about/",views.home,name="about"),
    path("",views.index,name="homepage"),
    
    path("comment/",RedirectView.as_view(url="/details"),name="comment"),

    path('subjects',views.subject,name="subject"),
    path("details",views.inputData,name="details"),
    path("books/",views.Book.as_view(),name="book"),
    #step 2
    path("template-based-view",
         TemplateView.as_view(template_name="data.html",
                              extra_context={"name":"Nisha","age":18}),
                              name="template"),
    #step 3 create data.html in templates folder
    path("muneeb/",TemplateView.as_view(template_name="muneeb.html"),name="muneeb"),





]
