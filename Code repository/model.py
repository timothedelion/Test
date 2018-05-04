class Question(models.Model):
    TYPE_QUESTION_CHOICES = (('OUI/NON', 'OUI/NON'), ('QCM', 'QCM'), ('Ouverte', 'Ouverte'), (
    'Mise en situation', 'Mise en situation'))  # Les choix possibles pour le champ TypeQuestion
    THEME_CHOICES = ()  # TDN : A définir
    TypeQuestion = models.CharField(choices=TYPE_QUESTION_CHOICES, max_length=100)
    Theme = models.CharField(choices=THEME_CHOICES, max_length=100)  # TDN : Dans l'idéal c'est une ForeignKey
    Enonce = models.TextField  # (verbose_name="C'est l'énoncé de la question à proprement parler")

    #    ReponseCorrecte = models.ManyToManyField(ReponseProposee, through = 'ReponseCorrecte')

    def get_list_ReponseProposee(self):
        return [(ReponseProposee.id, ReponseProposee.Enonce) for ReponseProposee in
                ReponseProposee.objects.filter(Question=self)]


class ReponseProposee(models.Model):
    Enonce = models.TextField
    Position = models.IntegerField  # (verbose_name="C'est l'ordre de cette réponse élémentaire parmi les réponses proposées")
    Question = models.ForeignKey(Question)


class ReponseCorrecte(models.Model):  # Cette table de liaison permet de définir la réponse correcte de chaque question
    Reponse = models.ForeignKey(ReponseProposee, null=True)
    Question = models.ForeignKey(Question)


class Questionnaire(models.Model):
    Nom = models.CharField(max_length=100,
                           verbose_name="Intitilé du questionnaire, permettant de le retrouver facilement")
    Duree = models.DurationField  # TDN : apprendre la manière de gérer ce type
    Question = models.ManyToManyField(Question, through='L_Question_Questionnaire')


class L_Question_Questionnaire(models.Model):
    Question = models.ForeignKey(Question)
    Questionnaire = models.ForeignKey(Questionnaire)


class FeuilleReponse(models.Model):
    # Cette table représente la feuille réponse d'un stagiaire à un questionnaire
    ETAT_CHOICES = (('En cours', 'En cours'), ('Termine', 'Termine'))
    Questionnaire = models.ForeignKey(Questionnaire)
    Etat = models.CharField(choices=ETAT_CHOICES, max_length=100)
    TempsRestant = models.IntegerField

    def CalculerNote(self):
        # Procédure qui calcule la note que vaut cette feuille de réponse : note globale et points obtenus à chaque question.

        return 0


class ReponseComplete(models.Model):
    # Stagiaire = models.ForeignKey(Stagiaire) #TDN : ajouter une ForeignKey reliant au user stagiaire
    FeuilleReponse = models.ForeignKey(FeuilleReponse)
    Reponses = models.ManyToManyField(ReponseProposee,
                                      through="L_ReponseComplete_ReponseProposee")  # TDN : Selon qu'il s'agit d'une QCM, OUI/NON, ou ouverte, la réponse renverra à un enregistrement de ReponseProposee, à plusieurs, ou à aucun mais avec une réponse non nulle tout de même... pas facile à gérer !!
    Question = models.ForeignKey(Question)

    def isCorrect(self):
        # Procédure qui vérifie si cette réponse est juste
        o_Query_ReponseComplete = L_ReponseComplete_ReponseProposee.objects.filter(
            ReponseComplete == self.id)  # requête retournant les réponses choisies
        o_Query_ReponseCorrecte = ReponseCorrecte.objects.filter(
            ReponseComplete__Question_id=self.Question.id)  # requête retournant les réponses correctes
        print(o_Query_ReponseComplete)
        print(o_Query_ReponseCorrecte)
        print(o_Query_ReponseComplete = o_Query_ReponseCorrecte)
        # TDN : return à completer




        class L_ReponseComplete_ReponseProposee(
            models.Model):  # TDN : ajouter un paramètre Ouvert/Fermé à la construction de l'instance pour exprimer si c'est une réponse ouverte ou QCM ???
            ReponseComplete = models.ForeignKey(ReponseComplete)
            ReponseProposee = models.ForeignKey(ReponseProposee,
                                                null=True)  # Ce champ sera laissé vide si la réponse est ouverte
            EnonceLibre = models.TextField(
                null=True)  # Ce champ sera laissé vide si la réponse est fermée. #TDN : c'est une solution de contournement. A voir si ça marche

            # class Stagiaire(models.Model):
            #    Questionnaires = models.ManyToManyField(Stagiaire, through = "FeuilleReponse")


            # Ajouter un champ isCorrect dans la table ReponseProposee
            # Ajouter l'attribut isCorrect à la liaison L_Question_ReponseProposee
            # Ajouter une procédure dans Question, qui va chercher la réponse correcte à la question  en filtrant la ReponsePoposee correcte
            # nécessaire d'ajouter des option 'on_delete=models.CASCADE' sur les relations entre tables ??


