from django.db.models.aggregates import Avg
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CreateUserForm,CompteForm,CreateCommentaire,UpdateMed,ContactForm
from .filters import SearchFilter
from .decorators import unauthenticated_user
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def home(request):
    myFilter=SearchFilter(request.GET)
    medecins=myFilter.qs
    if request.user.is_authenticated:
     compte=Compte.objects.get(user=request.user)   
     context={'medecins':medecins,'myFilter':myFilter,'compte':compte}
    else:
     context={'medecins':medecins,'myFilter':myFilter}  
    return render(request,'base/acceuil.html',context)
    
def search(request):
    medecins=Medecin.objects.all().order_by('-note')
    myFilter=SearchFilter(request.GET, queryset=medecins)
    medecins=myFilter.qs  
    if request.user.is_authenticated:
     compte=Compte.objects.get(user=request.user)   
     context={'medecins':medecins,'myFilter':myFilter,'compte':compte}
    else:
     context={'medecins':medecins,'myFilter':myFilter }       
    return render(request,'base/liste_med.html',context)


def profile(request,pk):
    medecins=Medecin.objects.filter(id=pk)
    commentaires=Commentaire.objects.filter(medecin=pk)
    if request.user.is_authenticated:
     compte=Compte.objects.get(user=request.user)
     context={'medecins':medecins,'commentaires':commentaires,'compte':compte}
    else:
     context={'medecins':medecins,'commentaires':commentaires}
    return render(request,'base/profile.html',context)



@unauthenticated_user    
def conxPage(request):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()  
            login(request, user)
            user=Compte.objects.get(user=user)
            if user.roles == 'P':
                return redirect('acceuil')
            if user.roles == 'M' :
                return redirect('pro_med')
            
            
    else:
        form=AuthenticationForm()
    context={'form':form}    
    return render(request,'compte/connecter.html',context)
@unauthenticated_user
def inscritPage(request):
    if  request.method=='POST':
        User_form=CreateUserForm(request.POST)
        Util_form = CompteForm(request.POST)
        if User_form.is_valid() and Util_form.is_valid(): 
            user=User_form.save() 
            user.save()
            Compte= Util_form.save(commit=False)
            Compte.user=user
            Compte.save()        
            if Compte.roles=='P':
                patient=Patient.objects.create(compte=Compte)
                patient.save()
            if Compte.roles=='M':
                medecin=Medecin.objects.create(compte=Compte)
                medecin.save()    
        else:
            HttpResponse("<h1>Something wrong with form </h1>")  
        return redirect('connecter')     
    else:
        User_form=CreateUserForm(request.POST)
        Util_form = CompteForm(request.POST)
    context={'User_form':User_form,'Util_form':Util_form}
    return render(request,'compte/inscription.html',context)
def logoutUser(request):
    logout(request)
    return redirect('connecter')  
@login_required (login_url="/connecter/")         
def createcomnt(request,pk):    
    user=request.user
    compte=Compte.objects.get(user=user)
    medecin=Medecin.objects.get(id=pk)
    if compte.roles=='P':
     patient=Patient.objects.get(compte=compte)
     commentaire=Commentaire.objects.filter(patient=patient,medecin=medecin).exists() 
     
     if  commentaire==False: 
        if  request.method=='POST':
         form=CreateCommentaire(request.user,request.POST)
         if form.is_valid():
            instance=form.save(commit=False) 
            instance.patient=patient
            instance.medecin=medecin
            instance.save()
            save_note(instance.pk)
            save_note_med(medecin.pk)
            return redirect('profile',pk=pk)
     else:
         return redirect('profile',pk)
     form=CreateCommentaire(request.user)       
     context={'form':form,'medecin':medecin,'patient':patient}   
     return render(request,'base/createcomnt.html',context)  
    else:
        return redirect('profile',pk)
@login_required (login_url="/connecter/")
def pro_med(request):
    compte=Compte.objects.get(user=request.user)
    medecins=Medecin.objects.get(compte=compte)
    context={'medecins':medecins,'compte':compte}
    return render(request,'base/pro_med.html',context)        
def modifier(request):
    if  request.method=='POST':
        form=UpdateMed(request.user ,request.POST, request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)
            compte=Compte.objects.get(user=request.user)
            profile.pk= Medecin.objects.get(compte=compte).pk
            profile.compte= Medecin.objects.get(compte=compte).compte
           
            profile.save()
            return redirect('pro_med')    
    else:
        form=UpdateMed(request.user)        
    context={'form':form}            
    return render(request,'base/modifier.html',context)    
def contact(request):
    form = ContactForm()
    if  request.method=='POST':       
        form=ContactForm(request.POST)
        if form.is_valid() : 
           form.save()
        return redirect('acceuil') 
    if request.user.is_authenticated:
     compte=Compte.objects.get(user=request.user)          
     contexte={'form':form,'compte':compte}  
    else:
     contexte={'form':form}            
    return render(request,'base/contact.html',contexte)
def propos(request):    
   if request.user.is_authenticated:
     compte=Compte.objects.get(user=request.user)   
     context={'compte':compte}
   else:
     context={} 
   return render(request,'base/propos.html',context)
def note_commentaire(commentaire):
    dict={'bien':7,'trés bien':10,'parfait':10,'m3allem':9,'cv':6,'moyen':5,'excellent':9,'catastrophe':1,'5ayeb':2,'mal':2}

    list=commentaire.split(" ")

    aide=False

    i=0

    while aide==False and i<len(list):

        if list[i] in dict:

            aide=True

        else:

            i=i+1

    if aide==True:

        return dict[list[i]]

    else:

        return 0
def save_note(id):
    commentaire=Commentaire.objects.get(pk=id)
    commentaire.note=note_commentaire(commentaire.body)
    commentaire.save()

def save_note_med(id):
    medecin=Medecin.objects.get(pk=id)
    commentaires=Commentaire.objects.filter(medecin=medecin)
    medecin.note=commentaires.aggregate(moy=Avg('note'))['moy']
    medecin.save()
