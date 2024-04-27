# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class EquipeRecherche(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    laboratoire = scrapy.Field()
    directeur_infos = scrapy.Field()
    axes_recherche = scrapy.Field()
    projets_recherche_link = scrapy.Field()
    these_habil_soutenues_link = scrapy.Field()
    prod_scientifique = scrapy.Field()
    membres = scrapy.Field()
class EspaceEntrep(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    qui_sommes_nous = scrapy.Field()
    objectif = scrapy.Field()
    Comment = scrapy.Field()
    activite_service = scrapy.Field()
class EspaceEtuBiblio(scrapy.Item):
    url = scrapy.Field()
    title_biblio = scrapy.Field()
    info_biblio = scrapy.Field()
class EspaceEtuClub(scrapy.Item):
    url = scrapy.Field()
    title_club = scrapy.Field()
    info_club = scrapy.Field()
class FaculteConseilEtab(scrapy.Item):
    url = scrapy.Field()
    Title = scrapy.Field()
    Brief = scrapy.Field()
    Name = scrapy.Field()
    Responsabilite = scrapy.Field()
####################################
class FaculteContact(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    localisation = scrapy.Field()
    numero_telephone = scrapy.Field()
    fax = scrapy.Field()
    email = scrapy.Field()

class FaculteDepartement(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    chef = scrapy.Field()
    email = scrapy.Field()

class FaculteMotDoyen(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()

class FacultePresentation(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()

class FaculteFormationContinue(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    cleaned_content = scrapy.Field()

class FaculteFormationContinueInfo(scrapy.Item):
    url = scrapy.Field()
    Formation = scrapy.Field()
    Filiere = scrapy.Field()
    Responsable = scrapy.Field()
    Objectif = scrapy.Field()
    Public_concerne = scrapy.Field()
    debouche = scrapy.Field()

class FaculteFormationInitial(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    Content = scrapy.Field()

class FaculteFormationInitialInfo(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    Formation = scrapy.Field()
    Objectifs = scrapy.Field()
    Programme = scrapy.Field()
    coordinator_name = scrapy.Field()
    coordinator_email = scrapy.Field()

class FaculteActualite(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()

class FaculteService(scrapy.Item):
    url = scrapy.Field()
    service = scrapy.Field()
    Brief = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()

class FaculteSpider(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    Content = scrapy.Field()

class FaculteRechercheStruct(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    laboratoire = scrapy.Field()
    directeur_infos = scrapy.Field()
    equipes_recherche = scrapy.Field()
    axes_recherche = scrapy.Field()
    projets_recherche_link = scrapy.Field()
    these_habil_soutenues_link = scrapy.Field()


