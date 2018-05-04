# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    username = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DoublureAnswerbasedoublure(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    created = models.DateTimeField()
    updated = models.DateTimeField()
    objectif = models.ForeignKey('DoublureObjectifdoublure', models.DO_NOTHING)
    response = models.ForeignKey('DoublureResponsedoublure', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doublure_answerbasedoublure'


class DoublureAnswerintegerdoublure(models.Model):
    answerbasedoublure_ptr = models.ForeignKey(DoublureAnswerbasedoublure, models.DO_NOTHING, primary_key=True)
    body = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doublure_answerintegerdoublure'


class DoublureAnswerradiodoublure(models.Model):
    answerbasedoublure_ptr = models.ForeignKey(DoublureAnswerbasedoublure, models.DO_NOTHING, primary_key=True)
    body = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doublure_answerradiodoublure'


class DoublureAnswerselectdoublure(models.Model):
    answerbasedoublure_ptr = models.ForeignKey(DoublureAnswerbasedoublure, models.DO_NOTHING, primary_key=True)
    body = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doublure_answerselectdoublure'


class DoublureAnswerselectmultipledoublure(models.Model):
    answerbasedoublure_ptr = models.ForeignKey(DoublureAnswerbasedoublure, models.DO_NOTHING, primary_key=True)
    body = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doublure_answerselectmultipledoublure'


class DoublureAnswertextdoublure(models.Model):
    answerbasedoublure_ptr = models.ForeignKey(DoublureAnswerbasedoublure, models.DO_NOTHING, primary_key=True)
    body = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doublure_answertextdoublure'


class DoublureDescriptiondoublure(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    numero_doublure = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doublure_descriptiondoublure'


class DoublureDoublure(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=300)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'doublure_doublure'


class DoublureObjectifdoublure(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    text = models.TextField()
    required = models.BooleanField()
    comments = models.TextField(blank=True, null=True)
    objectif_type = models.CharField(max_length=200)
    choices = models.TextField(blank=True, null=True)
    doublure = models.ForeignKey(DoublureDoublure, models.DO_NOTHING)
    soustheme = models.ForeignKey('DoublureSoustheme', models.DO_NOTHING)
    seuil_validation = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'doublure_objectifdoublure'


class DoublureResponsedoublure(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    created = models.DateTimeField()
    updated = models.DateTimeField()
    doubleur = models.CharField(max_length=200)
    comments = models.TextField(blank=True, null=True)
    doublure_uuid = models.CharField(max_length=12)
    doublure = models.ForeignKey(DoublureDoublure, models.DO_NOTHING)
    stagiaire = models.ForeignKey('ModulesimulationStagiaire', models.DO_NOTHING)
    numero_doublure = models.ForeignKey(DoublureDescriptiondoublure, models.DO_NOTHING, blank=True, null=True)
    amelioration = models.TextField(blank=True, null=True)
    positif = models.TextField(blank=True, null=True)
    zone = models.CharField(max_length=200)
    mce = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'doublure_responsedoublure'


class DoublureSoustheme(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=300)
    theme = models.ForeignKey('DoublureThemedoublure', models.DO_NOTHING)
    doublure = models.ForeignKey(DoublureDoublure, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doublure_soustheme'


class DoublureThemedoublure(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=300)
    doublure = models.ForeignKey(DoublureDoublure, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'doublure_themedoublure'


class ForumPost(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField()
    published_date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'forum_post'


class ModulesimulationAnswerbase(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    created = models.DateTimeField()
    updated = models.DateTimeField()
    objectif = models.ForeignKey('ModulesimulationObjectif', models.DO_NOTHING)
    response = models.ForeignKey('ModulesimulationResponse', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modulesimulation_answerbase'


class ModulesimulationAnswerinteger(models.Model):
    answerbase_ptr = models.ForeignKey(ModulesimulationAnswerbase, models.DO_NOTHING, primary_key=True)
    body = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modulesimulation_answerinteger'


class ModulesimulationAnswerradio(models.Model):
    answerbase_ptr = models.ForeignKey(ModulesimulationAnswerbase, models.DO_NOTHING, primary_key=True)
    body = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modulesimulation_answerradio'


class ModulesimulationAnswerselect(models.Model):
    answerbase_ptr = models.ForeignKey(ModulesimulationAnswerbase, models.DO_NOTHING, primary_key=True)
    body = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modulesimulation_answerselect'


class ModulesimulationAnswerselectmultiple(models.Model):
    answerbase_ptr = models.ForeignKey(ModulesimulationAnswerbase, models.DO_NOTHING, primary_key=True)
    body = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modulesimulation_answerselectmultiple'


class ModulesimulationAnswertext(models.Model):
    answerbase_ptr = models.ForeignKey(ModulesimulationAnswerbase, models.DO_NOTHING, primary_key=True)
    body = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modulesimulation_answertext'


class ModulesimulationBornessimu(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    value_max = models.IntegerField()
    value_min = models.IntegerField()
    simulation = models.ForeignKey('ModulesimulationSimulation', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'modulesimulation_bornessimu'


class ModulesimulationExercice(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=300)
    simulation = models.ForeignKey('ModulesimulationSimulation', models.DO_NOTHING)
    a_noter = models.TextField(blank=True, null=True)
    doc_associe = models.TextField(blank=True, null=True)
    regle = models.TextField(blank=True, null=True)
    contexte = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modulesimulation_exercice'


class ModulesimulationFormateur(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=300)
    profil = models.ForeignKey('ModulesimulationProfil', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'modulesimulation_formateur'


class ModulesimulationNotification(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    date = models.DateField()
    comments = models.TextField(blank=True, null=True)
    user_notif = models.ForeignKey(AuthUser, models.DO_NOTHING)
    rubrique = models.ForeignKey('ModulesimulationRubrique', models.DO_NOTHING)
    stagiaire = models.ForeignKey('ModulesimulationStagiaire', models.DO_NOTHING)
    uuid_etranger = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modulesimulation_notification'


class ModulesimulationObjectif(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    text = models.TextField()
    required = models.BooleanField()
    objectif_type = models.CharField(max_length=200)
    exercice = models.ForeignKey(ModulesimulationExercice, models.DO_NOTHING, blank=True, null=True)
    simulation = models.ForeignKey('ModulesimulationSimulation', models.DO_NOTHING)
    comments = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, null=True)
    choices = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modulesimulation_objectif'


class ModulesimulationObjectifTheme(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    objectif = models.ForeignKey(ModulesimulationObjectif, models.DO_NOTHING)
    theme = models.ForeignKey('ModulesimulationTheme', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'modulesimulation_objectif_theme'
        unique_together = (('objectif', 'theme'),)


class ModulesimulationProfil(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    profil = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'modulesimulation_profil'


class ModulesimulationResponse(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    created = models.DateTimeField()
    updated = models.DateTimeField()
    formateur = models.ForeignKey(ModulesimulationFormateur, models.DO_NOTHING)
    comments = models.TextField(blank=True, null=True)
    simulation_uuid = models.CharField(max_length=12)
    simulation = models.ForeignKey('ModulesimulationSimulation', models.DO_NOTHING)
    stagiaire = models.ForeignKey('ModulesimulationStagiaire', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'modulesimulation_response'


class ModulesimulationRubrique(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'modulesimulation_rubrique'


class ModulesimulationSimulation(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=300)
    description = models.TextField()
    numero = models.IntegerField(blank=True, null=True)
    dossier_simulation = models.TextField(blank=True, null=True)
    bilan = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'modulesimulation_simulation'


class ModulesimulationStagiaire(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=300)
    profil = models.ForeignKey(ModulesimulationProfil, models.DO_NOTHING)
    date_debut = models.DateField()
    formation_finie = models.BooleanField()
    date_fin_prevue = models.DateField()

    class Meta:
        managed = False
        db_table = 'modulesimulation_stagiaire'


class ModulesimulationTheme(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    score_limite = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'modulesimulation_theme'


class ModulesimulationValuethemesimu(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    value_simu = models.IntegerField()
    value_tot = models.IntegerField()
    simulation = models.ForeignKey(ModulesimulationSimulation, models.DO_NOTHING)
    theme = models.ForeignKey(ModulesimulationTheme, models.DO_NOTHING)
    value_tot_no_b = models.IntegerField(db_column='value_tot_no_B')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'modulesimulation_valuethemesimu'


class PratiqueAnswer(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    reponse = models.TextField(blank=True, null=True)
    date_reponse = models.DateField()
    formateur = models.ForeignKey(AuthUser, models.DO_NOTHING)
    question = models.ForeignKey('PratiqueQuestion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pratique_answer'


class PratiqueCategorie(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'pratique_categorie'


class PratiqueQuestion(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    titre = models.CharField(max_length=100)
    question = models.TextField(blank=True, null=True)
    date = models.DateField()
    stagiaire = models.ForeignKey(AuthUser, models.DO_NOTHING)
    answered = models.BooleanField()
    categorie = models.ForeignKey(PratiqueCategorie, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pratique_question'


class QuestionnaireFeuillereponse(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    etat = models.CharField(db_column='Etat', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tempsrestant = models.IntegerField(db_column='TempsRestant', blank=True, null=True)  # Field name made lowercase.
    note = models.IntegerField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    questionnaire = models.ForeignKey('QuestionnaireQuestionnaire', models.DO_NOTHING, db_column='Questionnaire_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'questionnaire_feuillereponse'


class QuestionnaireFeuillereponseReponseouverte(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    feuillereponse = models.ForeignKey(QuestionnaireFeuillereponse, models.DO_NOTHING)
    reponseouverte = models.ForeignKey('QuestionnaireReponseouverte', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'questionnaire_feuillereponse_ReponseOuverte'
        unique_together = (('feuillereponse', 'reponseouverte'),)


class QuestionnaireFeuillereponseReponseproposee(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    feuillereponse = models.ForeignKey(QuestionnaireFeuillereponse, models.DO_NOTHING)
    reponseproposee = models.ForeignKey('QuestionnaireReponseproposee', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'questionnaire_feuillereponse_ReponseProposee'
        unique_together = (('feuillereponse', 'reponseproposee'),)


class QuestionnaireQuestion(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    theme = models.CharField(db_column='Theme', max_length=100)  # Field name made lowercase.
    enonce = models.TextField(db_column='Enonce', blank=True, null=True)  # Field name made lowercase.
    correction = models.TextField(db_column='Correction', blank=True, null=True)  # Field name made lowercase.
    reponsebinairecorrecte = models.NullBooleanField(db_column='ReponseBinaireCorrecte')  # Field name made lowercase.
    typequestion = models.CharField(db_column='TypeQuestion', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'questionnaire_question'


class QuestionnaireQuestionnaire(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nom = models.CharField(db_column='Nom', max_length=100)  # Field name made lowercase.
    duree = models.IntegerField(db_column='Duree', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'questionnaire_questionnaire'


class QuestionnaireQuestionnaireQuestion(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    questionnaire = models.ForeignKey(QuestionnaireQuestionnaire, models.DO_NOTHING)
    question = models.ForeignKey(QuestionnaireQuestion, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'questionnaire_questionnaire_Question'
        unique_together = (('questionnaire', 'question'),)


class QuestionnaireReponsebinaire(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    type = models.CharField(db_column='Type', max_length=100)  # Field name made lowercase.
    label_true = models.CharField(db_column='Label_True', max_length=100)  # Field name made lowercase.
    label_false = models.CharField(db_column='Label_False', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'questionnaire_reponsebinaire'


class QuestionnaireReponseouverte(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    enonce = models.TextField(db_column='Enonce', blank=True, null=True)  # Field name made lowercase.
    question = models.ForeignKey(QuestionnaireQuestion, models.DO_NOTHING, db_column='Question_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'questionnaire_reponseouverte'


class QuestionnaireReponseproposee(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    enonce = models.TextField(db_column='Enonce', blank=True, null=True)  # Field name made lowercase.
    position = models.IntegerField(db_column='Position', blank=True, null=True)  # Field name made lowercase.
    question = models.ForeignKey(QuestionnaireQuestion, models.DO_NOTHING, db_column='Question_id')  # Field name made lowercase.
    iscorrect = models.BooleanField(db_column='isCorrect')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'questionnaire_reponseproposee'


class QuestionnaireTheme(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nomtheme = models.CharField(db_column='NomTheme', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'questionnaire_theme'


class SynthBilansynthese(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    bilan = models.CharField(max_length=1, blank=True, null=True)
    temps = models.IntegerField()
    score = models.IntegerField()
    stagiaire = models.ForeignKey(ModulesimulationStagiaire, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'synth_bilansynthese'


class SynthDoubluresynthese(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    autonomie = models.CharField(max_length=100)
    date_fin_prevue = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'synth_doubluresynthese'


class SynthEvent(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    description = models.TextField()
    date = models.DateField()
    alerte = models.BooleanField()
    formateur = models.ForeignKey(AuthUser, models.DO_NOTHING)
    stagiaire = models.ForeignKey(ModulesimulationStagiaire, models.DO_NOTHING)
    archiver = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'synth_event'


class SynthObjectifStagiaire(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'synth_objectif_stagiaire'


class SynthPalmares(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    date_reussite = models.DateField()
    objectif = models.ForeignKey(SynthObjectifStagiaire, models.DO_NOTHING)
    stagiaire = models.ForeignKey(ModulesimulationStagiaire, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'synth_palmares'


class SynthPrevisionmax(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    score_max = models.IntegerField()
    temps = models.IntegerField()
    stagiaire = models.ForeignKey(ModulesimulationStagiaire, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'synth_previsionmax'


class SynthPrevisionmin(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    score_min = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    temps = models.IntegerField()
    stagiaire = models.ForeignKey(ModulesimulationStagiaire, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'synth_previsionmin'


class SynthSuividoublure(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    autonomie_validee = models.ForeignKey(SynthDoubluresynthese, models.DO_NOTHING)
    stagiaire = models.ForeignKey(ModulesimulationStagiaire, models.DO_NOTHING)
    simulation = models.ForeignKey(ModulesimulationSimulation, models.DO_NOTHING)
    score = models.IntegerField()
    score_max = models.IntegerField()
    test = models.BooleanField()
    date_test = models.DateField()

    class Meta:
        managed = False
        db_table = 'synth_suividoublure'


class SynthSuividoublureideal(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    score = models.IntegerField()
    score_max = models.IntegerField()
    test = models.BooleanField()
    autonomie_validee = models.ForeignKey(SynthDoubluresynthese, models.DO_NOTHING)
    simulation = models.ForeignKey(ModulesimulationSimulation, models.DO_NOTHING)
    stagiaire = models.ForeignKey(ModulesimulationStagiaire, models.DO_NOTHING)
    date_test = models.DateField()

    class Meta:
        managed = False
        db_table = 'synth_suividoublureideal'


class SynthSuividoubluremin(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    score = models.IntegerField()
    score_max = models.IntegerField()
    test = models.BooleanField()
    autonomie_validee = models.ForeignKey(SynthDoubluresynthese, models.DO_NOTHING)
    simulation = models.ForeignKey(ModulesimulationSimulation, models.DO_NOTHING)
    stagiaire = models.ForeignKey(ModulesimulationStagiaire, models.DO_NOTHING)
    date_test = models.DateField()

    class Meta:
        managed = False
        db_table = 'synth_suividoubluremin'


class SynthSuividoublurere(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    score = models.IntegerField()
    score_max = models.IntegerField()
    test = models.BooleanField()
    autonomie_validee = models.ForeignKey(SynthDoubluresynthese, models.DO_NOTHING)
    simulation = models.ForeignKey(ModulesimulationSimulation, models.DO_NOTHING)
    stagiaire = models.ForeignKey(ModulesimulationStagiaire, models.DO_NOTHING)
    date_test = models.DateField()

    class Meta:
        managed = False
        db_table = 'synth_suividoublurere'


class SynthThemesynthese(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    stagiaire = models.ForeignKey(ModulesimulationStagiaire, models.DO_NOTHING)
    theme = models.ForeignKey(ModulesimulationTheme, models.DO_NOTHING)
    score_limite = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'synth_themesynthese'


class SynthTouttheme(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    stagiaire = models.ForeignKey(ModulesimulationStagiaire, models.DO_NOTHING)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'synth_touttheme'


class SynthValidationdoublure(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    autonomie_validee = models.ForeignKey(SynthDoubluresynthese, models.DO_NOTHING)
    stagiaire = models.ForeignKey(ModulesimulationStagiaire, models.DO_NOTHING)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'synth_validationdoublure'


class TheoriqueAcquisitionreferentiel(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    acquisition = models.CharField(max_length=6)
    referentiel = models.ForeignKey('TheoriqueReferentiel', models.DO_NOTHING, blank=True, null=True)
    stagiaire = models.ForeignKey(ModulesimulationStagiaire, models.DO_NOTHING, blank=True, null=True)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'theorique_acquisitionreferentiel'


class TheoriqueFormationtheorique(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    titre = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    semaine_cours = models.IntegerField()
    fichier = models.CharField(max_length=100, blank=True, null=True)
    lien = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'theorique_formationtheorique'


class TheoriqueFormationtheoriqueProfil(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    formationtheorique = models.ForeignKey(TheoriqueFormationtheorique, models.DO_NOTHING)
    profil = models.ForeignKey(ModulesimulationProfil, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'theorique_formationtheorique_profil'
        unique_together = (('formationtheorique', 'profil'),)


class TheoriqueReferentiel(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nom = models.TextField(blank=True, null=True)
    priorite = models.IntegerField()
    module_theorique = models.ForeignKey(TheoriqueFormationtheorique, models.DO_NOTHING)
    classe = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'theorique_referentiel'


class TheoriqueValidationtheorique(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    validation = models.BooleanField()
    module_theorique = models.ForeignKey(TheoriqueFormationtheorique, models.DO_NOTHING, blank=True, null=True)
    stagiaire = models.ForeignKey(ModulesimulationStagiaire, models.DO_NOTHING, blank=True, null=True)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'theorique_validationtheorique'
