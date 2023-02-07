from django import forms
from .models import Acciones,PlanAcciones

class AccionesForms(forms.ModelForm):
    class Meta:
        model = Acciones
        fields = ('titulo' ,'recomendacion','respoejecucion','actividadrealizar','fechaejecucion','observacion','estadoacciones',
        'plan')
        labels = { 
            'titulo':"TITULO ",
            'recomendacion':"RECOMENDACIÓN",
            'respoejecucion':"RESPONSABLE DE EJECUCIÓN DE LA RECOMENDACIÓN",
            'actividadrealizar':"ACTIVIDADES A REALIZAR PARA LA EJECUCIÓN DE LA RECOMENDACIÓN",
            'fechaejecucion':"FECHA DE EJECUCIÓN",
            'firmaresponsable':"",
            'observacion':"OBSERVACIÓN",
            'estadoacciones':"ESTADO",
            'plan':"PLAN",
        }
        widgets = {
            'titulo':forms.Textarea(attrs={'class':'form-control','rows':"2"}),
            'recomendacion':forms.Textarea(attrs={'class':'form-control','rows':"2"}),
            'respoejecucion':forms.Textarea(attrs={'class':'form-control','rows':"2"}),
            'actividadrealizar':forms.Textarea(attrs={'class':'form-control','rows':"2"}),
            'fechaejecucion':forms.DateInput(format='%Y-%m-%d',attrs={'class':'form-control','type':'date'}),
            'firmaresponsable':forms.Textarea(attrs={'class':'form-control','rows':"2"}),
            'observacion':forms.Textarea(attrs={'class':'form-control','rows':"2"}),
            'estadoacciones':forms.Select(attrs={'class':'form-control'}),
            'plan':forms.Select(attrs={'class':'form-control'}),
        }
        
class PlanAccionesForms(forms.ModelForm):
    class Meta:
        model = PlanAcciones
        fields = ('titulo' ,'ninforme','periodo','fecha')
        labels = { 
            'titulo':"TITULO ",
            'ninforme':"N. INFORME",
            'periodo':"PERIODO",
            'fecha':"FECHA",
        }
        widgets = {
            'titulo':forms.Textarea(attrs={'class':'form-control','rows':"2"}),
            'ninforme':forms.Textarea(attrs={'class':'form-control','rows':"2"}),
            'periodo':forms.Textarea(attrs={'class':'form-control','rows':"2"}),
            'fecha':forms.DateInput(format='%Y-%m-%d',attrs={'class':'form-control','type':'date'}),
        }