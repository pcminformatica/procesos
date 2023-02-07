from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from proyectos.models import Acciones,EstadoSistemas,PlanAcciones
from datetime import datetime,time,date,timedelta
from proyectos.forms import AccionesForms,PlanAccionesForms
# Create your views here.
#@login_required(login_url='/iniciar/')

def HomePlanes(request):
        planes = PlanAcciones.objects.all()
        today = date.today()
        riesgo = today + timedelta(days=8)
        ctx = {'planes':planes,
                'today':today,
                'riesgo':riesgo}
        return render(request,"proyectos/HomePlanes.html",ctx)

def ViewPlanAccionesForms(request):
        if request.method == 'POST':
                form = PlanAccionesForms(request.POST, request.FILES or None)
                if form.is_valid():
                        author = form.save(commit=False)
                        author.save()
                        messages.success(request, 'Plan acción creada con éxito.')
                        return redirect('HomePlanes')
        else:
                form = PlanAccionesForms()
                contex = {'form':form}
        return render(request,"proyectos/forms.html",contex)

def ViewEditarPlanAccionesForms(request,pk):
	accion = get_object_or_404(PlanAcciones,pk=pk)
	if request.method == 'POST':
		form = PlanAccionesForms(request.POST, request.FILES or None,instance=accion)
		if form.is_valid:
			author = form.save(commit=False)
			author.save()
			messages.success(request, 'Plan acción actualizada con éxito.')
			return redirect('HomePlanes')
	else:
		form = PlanAccionesForms(instance=accion)
	contex = {'form':form}
	return render(request,"proyectos/forms.html",contex)

def ViewEliminarPlanAccionesForms(request,pk):
        empresa = get_object_or_404(Acciones,pk=pk)
        empresa.estadosistema = EstadoSistemas.objects.get(codigo=2)
        empresa.save()
        messages.success(request, 'Plan acción eliminada con exito.')
        return redirect('HomePlanes')

from django.db.models import Q
def HomeProyectos(request,pk):
        plan = get_object_or_404(PlanAcciones,pk=pk)
        acciones = Acciones.objects.filter(plan=plan).filter(~Q(estadosistema__codigo = 2))
        today = date.today()
        riesgo = today + timedelta(days=8)
        ctx = {'acciones':acciones,
                'today':today,
                'riesgo':riesgo,
                'plan':plan}
        return render(request,"proyectos/HomeProyectos.html",ctx)

def ViewAccionesForms(request):
        if request.method == 'POST':
                form = AccionesForms(request.POST, request.FILES or None)
                if form.is_valid():
                        author = form.save(commit=False)
                        author.save()
                        messages.success(request, 'Acción creada con éxito.')
                        return redirect('HomeProyectos' ,author.plan.pk)
        else:
                form = AccionesForms()
                contex = {'form':form}
        return render(request,"proyectos/forms.html",contex)

def ViewEditarAccionesForms(request,pk):
	accion = get_object_or_404(Acciones,pk=pk)
	if request.method == 'POST':
		form = AccionesForms(request.POST, request.FILES or None,instance=accion)
		if form.is_valid:
			author = form.save(commit=False)
			author.save()
			messages.success(request, 'Acción actualizada con éxito.')
			return redirect('HomeProyectos',author.plan.pk)
	else:
		form = AccionesForms(instance=accion)
	contex = {'form':form}
	return render(request,"proyectos/forms.html",contex)

def ViewEliminarAccionesForms(request,pk):
        empresa = get_object_or_404(Acciones,pk=pk)
        empresa.estadosistema = EstadoSistemas.objects.get(codigo=2)
        empresa.save()
        messages.success(request, 'Acción eliminada con exito.')
        return redirect('HomeProyectos',empresa.plan.pk)