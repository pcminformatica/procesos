"""sppa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include,path
from proyectos import views as proyectos


urlpatterns = [

    path('', proyectos.HomePlanes, name='HomePlanes'),
    path('plan/formulario', proyectos.ViewPlanAccionesForms, name='ViewPlanAccionesForms'),
    path('plan/formularios/<pk>/edit/', proyectos.ViewEditarPlanAccionesForms, name='ViewEditarPlanAccionesForms'),
    path('plan/formulario/<pk>/eliminar', proyectos.ViewEliminarAccionesForms, name='ViewEliminarAccionesForms'),  
#   
    path('plan/<pk>/1/', proyectos.HomeProyectos, name='HomeProyectos'),
    path('formulario', proyectos.ViewAccionesForms, name='ViewAccionesForms'),
    path('formularios/<pk>/edit/', proyectos.ViewEditarAccionesForms, name='ViewEditarAccionesForms'),
    path('formulario/<pk>/eliminar', proyectos.ViewEliminarAccionesForms, name='ViewEliminarAccionesForms'),  


]
