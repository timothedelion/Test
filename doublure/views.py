from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.db.models.functions import Concat
from django.db.models import Value
from django.utils import timezone
import stage.settings
from django.views import generic
from django.contrib.auth.decorators import user_passes_test, login_required
from  django.contrib.auth.mixins import UserPassesTestMixin, AccessMixin
from django.core.mail import send_mail
from .models import ResponseDoublure, Doublure, SousTheme, ThemeDoublure, ObjectifDoublure, AnswerRadioDoublure, DescriptionDoublure
from .forms import ResponseDoublureForm
from modulesimulation.models import Stagiaire, Rubrique, Notification
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

def is_formateur(user): # vérifie si l'utilisateur identifié est un formateur, utilisé pour authoriser l'accés à certaine page à l'utilisateur
    return user.groups.filter(name='Formateur').exists()


def is_stagiaire(user):
    return user.groups.filter(name='Stagiaire').exists()


def is_doubleur(user):
    return user.groups.filter(name='Doubleur').exists()


@login_required # il faut être identiié pour accèder à cette page
@user_passes_test(is_formateur) # il faut être un formateur pour accèder à cette page
def DoublureDetail(request,pk, id):
    doublure = Doublure.objects.get(id=1)
    stagiaire = Stagiaire.objects.get(pk=pk)
    numero_doublure = DescriptionDoublure.objects.get(id=id)
    liste_obj = doublure.objectifs_non_val(stagiaire)
    soustheme_items = [o.soustheme for o in liste_obj]
    sousthemes = list(set([c for c in soustheme_items]))
    themes = list(set([c.theme for c in soustheme_items]))

    if request.method == 'POST':
        form = ResponseDoublureForm(request.POST, doublure=doublure, stagiaire=stagiaire)
        if form.is_valid():
            response = form.save()
            response.numero_doublure = numero_doublure
            response.stagiaire = stagiaire
            response.save()

            #Permet de compléter le journal des notifications
            rubrique=Rubrique.objects.get(name="passage_doublure")
            comments = str(response.numero_doublure) + " (" + str(response.get_zone_display()) + ")"
            notif = Notification(date=timezone.now(), rubrique=rubrique, stagiaire=stagiaire, user_notif=request.user, uuid_etranger=response.doublure_uuid, comments = comments)
            notif.save()
            return HttpResponseRedirect("/doublure/confirm/%s" % response.doublure_uuid)
    else:
        form = ResponseDoublureForm(doublure=doublure, stagiaire=stagiaire)

    return render(request, 'doublure/doubluredetail.html', {'response_form': form, 'doublure': numero_doublure,
                                                            'sousthemes':sousthemes, 'themes': themes, 'stagiaire':stagiaire})


@login_required
def ConfirmDoublure(request, uuid):
    email = stage.settings.support_email
    rep = ResponseDoublure.objects.filter(doublure_uuid=uuid).order_by('-created')[0]
    stagiaire = rep.stagiaire
    objectifs = []
    answers = []
    sousthemes = []
    themes = []
    '''On ne garde que la dernière version de la doublure'''
    numero = list(set(
        [r.numero_doublure for r in ResponseDoublure.objects.filter(stagiaire=stagiaire).order_by('numero_doublure')]))
    try:
        for i in numero:
            reps = ResponseDoublure.objects.filter(stagiaire=stagiaire, numero_doublure=i).order_by('updated', 'created')
            while len(reps) > 1:
                reps[0].delete()
    except AssertionError:
        print('erreur')

    ''' On construit le contexte '''

    ans= [a for a in AnswerRadioDoublure.objects.filter(response=rep)]
    for a in ans:
        if a.body != '' or a.comments != '':
            answers.append(a)
            objectifs.append(a.objectif)
            themes.append(a.objectif.soustheme.theme)
    objectifs = list(set(objectifs))
    sousthemes = list(set([o.soustheme for o in objectifs]))
    themes = list(set(themes))



    ''' On contrôle que l'utilisateur à le droit d'accèder à la page'''
    if (request.user.groups.filter(name='Formateur').exists() or request.user.groups.filter(name='Doubleur').exists()  or (request.user.first_name + ' ' + request.user.last_name == stagiaire.name)):
        return render(request, 'doublure/confirmdoublure.html', {'uuid': uuid, "email": email, 'rep': rep,'stagiaire':stagiaire,
                                                                 'sousthemes': sousthemes, 'objectifs': objectifs,
                                                                 'answers': answers, 'themes': themes})


    else:
        return render(request, 'registration/accueil.html')


class IndexView(UserPassesTestMixin, AccessMixin, generic.ListView):# affiche la liste des stagiaires
    def get_login_url(self): # redirige le stagiaire
        if self.request.user.groups.filter(name='Stagiaire').exists():
            stag = Stagiaire.objects.filter(name=self.request.user.first_name + ' ' + self.request.user.last_name)
            url = '/doublure/index/'+str(stag[0].id)+'/'
        else:
            url = '/accounts/login/accueil/'
        return url

    ''' contrôle l'accès à la page '''
    def test_func(self):
        return self.request.user.groups.filter(name='Doubleur') or self.request.user.groups.filter(name='Formateur')


    template_name = 'doublure/indexstagiaire.html'

    context_object_name = 'stagiaire_list'
    def get_queryset(self):
        return Stagiaire.objects.all()


def DoublureIndexView(request, id): # Affiche la liste des doublures, en vert celles effectuées en gris celles non effectuées
    stagiaire = Stagiaire.objects.get(id=id)
    ''' On ne garde que la dernière version de la doublure'''
    numero = list(set([r.numero_doublure for r in ResponseDoublure.objects.filter(stagiaire=stagiaire).order_by('numero_doublure')]))
    try:
        for i in numero:
            rep = ResponseDoublure.objects.filter(stagiaire=stagiaire, numero_doublure=i).order_by('updated', 'created')
            while len(rep)>1:

                rep[0].delete()
    except AssertionError:
         print('erreur')

    doublure_l = [ d for d in DescriptionDoublure.objects.all()]
    doublure_list = []
    rep_list = ResponseDoublure.objects.filter(stagiaire=stagiaire).order_by('numero_doublure')

    for d in doublure_l:
        if not ResponseDoublure.objects.filter(stagiaire=stagiaire, numero_doublure=d).exists():
            doublure_list.append(d)


    return render(request, 'doublure/indexdoublure.html',{'rep_list':rep_list, 'doublure_list': doublure_list, 'stagiaire': stagiaire})

@login_required
@user_passes_test(is_formateur or is_doubleur)
def DoublureModification(request, pk, id): # permet de modifier le résultat d'une doublure
    response = get_object_or_404(ResponseDoublure, id=pk)
    stagiaire = Stagiaire.objects.get(id=id)
    numero = response.numero_doublure
    numero_doublure = response.numero_doublure
    doublure = response.doublure
    soustheme_items = SousTheme.objects.filter(doublure=doublure)
    sousthemes = [c for c in soustheme_items]
    themes = list(set([c.theme for c in soustheme_items]))
    cle = 1
    if request.method == 'POST':
        form = ResponseDoublureForm(request.POST, instance=response, doublure=numero_doublure, stagiaire=stagiaire)

        if form.is_valid():
            resp = form.save()
            cle = resp.id
            resp.save()





            return HttpResponseRedirect("/doublure/confirm/%s" % response.doublure_uuid)
    else:
        form = ResponseDoublureForm(instance=response, doublure=doublure, stagiaire=stagiaire)



    return render(request, 'doublure/doubluredetail.html',{'response_form': form, 'doublure': numero_doublure,
                   'sousthemes': sousthemes, 'themes': themes,'stagiaire':stagiaire})



def VisionGlobale(request, id): #affiche une vision globale de toutes les doublures du stagiaire, id = identifiant du stagiaire
    stagiaire = Stagiaire.objects.get(id=id)
    doublures = [d for d in ResponseDoublure.objects.filter(stagiaire=stagiaire).order_by('numero_doublure')]
    return render(request, 'doublure/global.html', {'stagiaire':stagiaire, 'doublures':doublures})