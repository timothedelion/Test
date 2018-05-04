from .models import ResponseDoublure, ObjectifDoublure, AnswerBaseDoublure, AnswerIntegerDoublure, AnswerRadioDoublure, AnswerSelectDoublure, AnswerSelectMultipleDoublure, AnswerTextDoublure
from django import forms
from django.contrib.auth.models import User
from django.forms import models
import uuid
import django.core.exceptions
from modulesimulation.forms import HorizontalRadioRenderer

class ResponseDoublureForm(models.ModelForm): # créer le formulaire de résultat d'une doublure
    class Meta:
        model = ResponseDoublure
        fields = ('doubleur', 'stagiaire','zone', 'comments','positif', 'amelioration','mce')
        widgets= {'comments' : forms.Textarea(attrs={'rows':3,'cols':105}),'positif' : forms.Textarea(attrs={'rows':3,'cols':105}),
                  'amelioration' : forms.Textarea(attrs={'rows':3,'cols':105})}

    def __init__(self, *args, **kwargs): # initialise le formulaire, définit les champs du formulaire et les valeurs initiales éventuelles
        doublure = kwargs.pop('doublure')
        stagiaire = kwargs.pop('stagiaire')
        try:
            respd = kwargs.get('instance')
            self.uuid = respd.doublure_uuid
            print(self.uuid)
        except AttributeError:
            self.uuid = uuid.uuid4().hex
        self.doublure = doublure
        self.stagiaire = stagiaire
        super(ResponseDoublureForm, self).__init__(*args, **kwargs)

        data = kwargs.get('data')
        self.fields["stagiaire"].initial = stagiaire # donne la valeur par défault du bon stagiaire




        for q in doublure.objectifs_non_val(self.stagiaire):


            if q.objectif_type == ObjectifDoublure.TEXT:
                self.fields["objectif_%d" % q.pk] = forms.CharField(label=q.text, widget=forms.Textarea)
            elif q.objectif_type == ObjectifDoublure.RADIO:
                objectif_choices=q.get_choices()
                self.fields["objectif_%d" % q.pk]= forms.ChoiceField(label=q.text, widget=HorizontalRadioRenderer, choices= objectif_choices)
            elif q.objectif_type == ObjectifDoublure.SELECT:
                objectif_choices=q.get_choices()
                objectif_choices = tuple([('', '-------------')]) + objectif_choices
                self.fields["objectif_%d" % q.pk]=forms.ChoiceField(label=q.text, widget=forms.Select, choices=objectif_choices)
            elif q.objectif_type==ObjectifDoublure.SELECT_MULTIPLE:
                objectif_choices=q.get_choices()
                self.fields["objectif_%d" %q.pk]=forms.MultipleChoiceField(label=q.text, widget=forms.CheckboxSelectMultiple, choices=objectif_choices)
            elif q.objectif_type== ObjectifDoublure.INTEGER:
                self.fields["objectif_%d" % q.pk]= forms.IntegerField(label=q.text)
            if q.required:
                self.fields["objectif_%d" % q.pk].required= True
                self.fields["objectif_%d" % q.pk].widget.attrs["class"]="required"
            else:
                self.fields["objectif_%d" % q.pk].required= False

            self.fields["zcomments_%d" % q.pk] = forms.CharField(label='Commentaire',
                                                                 widget=forms.Textarea(attrs={'rows': 1, 'cols': 40}),
                                                                 required=False)

            if q.soustheme:
                classes = self.fields["objectif_%d" % q.pk].widget.attrs.get("class")
                if classes:
                    self.fields["objectif_%d" % q.pk].widget.attrs["class"]= classes + ("cat_%s" % q.soustheme.name)
                else:
                    self.fields["objectif_%d" % q.pk].widget.attrs["class"] = ("cat_%s" % q.soustheme.name)

                classesc = self.fields["zcomments_%d" % q.pk].widget.attrs.get("class")
                if classesc:
                    self.fields["zcomments_%d" % q.pk].widget.attrs["class"] = classes + ("cat_%s" % q.soustheme.name)
                else:
                    self.fields["zcomments_%d" % q.pk].widget.attrs["class"] = ("cat_%s" % q.soustheme.name)
                self.fields["objectif_%d" % q.pk].widget.attrs["soustheme"] = q.soustheme.name
                self.fields["zcomments_%d" % q.pk].widget.attrs["soustheme"] = q.soustheme.name

            try:
                a = AnswerRadioDoublure.objects.get(response=ResponseDoublure.objects.get(doublure_uuid=self.uuid), objectif=q)
                self.fields["objectif_%d" % q.pk].initial = a.body # permet de recupérer les valeurs déjà rentrées dans le cas d'une modification de la doublure
                self.fields["zcomments_%d" % q.pk].initial = a.comments # permet de recupérer les valeurs déjà rentrées dans le cas d'une modification de la doublure
            except django.core.exceptions.ObjectDoesNotExist:
                print('fail')



            if data:
                self.fields["objectif_%d" % q.pk].initial = data.get("objectif_%d" % q.pk)
                self.fields["zcomments_%d" % q.pk].initial = data.get("zcomments_%d" % q.pk)



    def save(self, commit=True): # permet de sauvegarder le résultat d'une doublure
        response = super(ResponseDoublureForm, self).save(commit=False)
        response.doublure = self.doublure
        response.doublure_uuid = self.uuid
        response.save()
        for field_name, field_value in self.cleaned_data.items():
            if field_name.startswith("objectif_"):
                q_id = int(field_name.split("_")[1])
                q = ObjectifDoublure.objects.get(pk=q_id)
                if q.objectif_type == ObjectifDoublure.TEXT:
                    a = AnswerTextDoublure(objectif=q)
                    a.body = field_value
                elif q.objectif_type == ObjectifDoublure.RADIO:
                    a = AnswerRadioDoublure(objectif=q)
                    a.body = field_value
                    for field_name_c, field_value_c in self.cleaned_data.items():
                        if field_name_c.startswith("zcomments_"):
                            c_id = int(field_name_c.split("_")[1])
                            if c_id == q_id:
                                a.comments = field_value_c


                elif q.objectif_type == ObjectifDoublure.SELECT:
                    a = AnswerSelectDoublure(objectif=q)
                    a.body = field_value
                elif q.objectif_type == ObjectifDoublure.SELECT_MULTIPLE:
                    a = AnswerSelectMultipleDoublure(question=q)
                    a.body = field_value
                elif q.objectif_type == ObjectifDoublure.INTEGER:
                    a = AnswerIntegerDoublure(objectif=q)
                    a.body = field_value

                a.response = response
                a.save()



        return response