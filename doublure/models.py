from django.db import models
from django.core.exceptions import ValidationError
import datetime
from modulesimulation.models import Stagiaire
# Create your models here.



class Doublure(models.Model): # ressemble à la classe Simulation mais ici on ne définira qu'une seule doublure,
    # pour différenciez les différentes doublures on utilisera la classe DescritptionDoublure dans la classe Responsedoublure
    name = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return (self.name)

    def objectifs(self):
        if self.pk:
            return ObjectifDoublure.objects.filter(doublure=self.pk)
        else:
            return None

    def objectifs_non_val(self, stagiaire): # retourne la liste des objectifs non validés par un stagiaire, prend un stagiaire comme argument
        if self.pk:
            liste = ObjectifDoublure.objects.filter(doublure=self.pk)
            l=[]
            for o in liste:
                if not o.objectif_valide(stagiaire):
                    l.append(o)
            return l
        else:
            return None

    def themeDoublure(self):
        if self.pk:
            return ThemeDoublure.objects.filter(doublure=self.pk)
        else:
            return None

class ThemeDoublure(models.Model):
    name = models.CharField(max_length=300)
    doublure = models.ForeignKey(Doublure)
    def __str__(self):
        return self.name

class SousTheme(models.Model):
    name = models.CharField(max_length=300)
    theme = models.ForeignKey(ThemeDoublure)
    doublure = models.ForeignKey(Doublure, null=True, blank=True )

    def __str__(self):
        return self.name

def validate_list(value):
    '''takes a text value and verifies that there is at least one comma '''
    values = value.split(',')
    if len(values) < 2:
        raise ValidationError("The selected field requires an associated list of choices. Choices must contain more than one item.")


class ObjectifDoublure(models.Model):
    TEXT = 'text'
    RADIO = 'radio'
    SELECT = 'select'
    SELECT_MULTIPLE = 'select-multiple'
    INTEGER = 'integer'
    QUESTION_TYPES = (
     	(TEXT, 'text'),
        (RADIO, 'radio'),
        (SELECT, 'select'),
        (SELECT_MULTIPLE, 'Select Multiple'),
        (INTEGER, 'integer'),
         	)

    seuil_validation = models.IntegerField(default=3) # seuil pr valider un objectif => par défault à 3 mais peut être changé
    text = models.TextField()
    required = models.BooleanField()
    soustheme = models.ForeignKey(SousTheme)
    doublure = models.ForeignKey(Doublure)
    comments = models.TextField('Commentaire', blank=True, null=True)
    objectif_type = models.CharField(max_length=200, choices=QUESTION_TYPES, default=RADIO)
    choices = models.TextField(blank=True, null=True,
                               help_text='if the question type is "radio," "select," or "select multiple" provide a comma-separated list of options for this',
                               default="Validé, En cours, Difficultés")

    def save(self, *args, **kwargs):
        if (
                    self.objectif_type == ObjectifDoublure.RADIO or self.objectif_type == ObjectifDoublure.SELECT or self.objectif_type == ObjectifDoublure.SELECT_MULTIPLE):
            validate_list(self.choices)
        super(ObjectifDoublure, self).save(*args, **kwargs)


    def objectif_valide(self, stagiaire): # vérifie si un stagiaire à valider un objectif, prend un stagiaire en argument, retourn True ou False
        rep = ResponseDoublure.objects.filter(stagiaire=stagiaire)
        answers = []
        for response in rep:
            answer = AnswerRadioDoublure.objects.filter(response=response, objectif=self)
            answers.append([a for a in answer])

        som = 0
        for ans in answers:
            for a in ans:
                if a.body == 'Validé':
                    som += 1
        return som >= self.seuil_validation


    def get_choices(self):
        choices = self.choices.split(',')
        choices_list = []
        for c in choices:
            c = c.strip()
            choices_list.append((c, c))
        choices_tuple = tuple(choices_list)
        return choices_tuple

    def __str__(self):
        return self.text


class DescriptionDoublure(models.Model): # défini le numéro de la doublure, utilisé dans la classe ResponseDoublure
    numero_doublure = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.numero_doublure


class ResponseDoublure (models.Model): # définit le résultat du stagiaire à une doublure
    CHOICES = (('O','Ouest'),('S','Sud'),('E','Est'))
    zone = models.CharField(max_length=200, default = 'O',choices=CHOICES)
    numero_doublure = models.ForeignKey(DescriptionDoublure, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    doublure = models.ForeignKey(Doublure)
    doubleur = models.CharField(max_length=200)
    mce = models.CharField(max_length=3, default='MCE')
    stagiaire = models.ForeignKey(Stagiaire)
    comments = models.TextField('Thèmes abordés, situation particulières rencontrées', blank=True, null=True)
    positif = models.TextField('Points positifs', blank=True, null=True)
    amelioration = models.TextField('Axe d"amélioration', blank=True, null=True)
    doublure_uuid = models.CharField("Identifiant unique de la doublure du stagiaire ", max_length=12)

    def __unicode__(self):
        return "response %s" % self.doublure_uuid


class AnswerBaseDoublure(models.Model):
    objectif = models.ForeignKey(ObjectifDoublure)
    response = models.ForeignKey(ResponseDoublure, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class AnswerTextDoublure(AnswerBaseDoublure):
    body = models.TextField(blank=True, null=True)


class AnswerRadioDoublure(AnswerBaseDoublure):
    body = models.TextField(blank=True, null=True)
    comments = models.TextField('Commentaire', blank=True, null=True)


class AnswerSelectDoublure(AnswerBaseDoublure):
    body = models.TextField(blank=True, null=True)


class AnswerSelectMultipleDoublure(AnswerBaseDoublure):
    body = models.TextField(blank=True, null=True)


class AnswerIntegerDoublure(AnswerBaseDoublure):
    body = models.IntegerField(blank=True, null=True)
