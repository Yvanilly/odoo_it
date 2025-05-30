from odoo import models, fields, api

class Gestion_Sortie(models.Model):
    _name = "gestion.sortie"
    _description = "Modèle pour gérer les sorties de stock"

    # Informations sur l'article
    name = fields.Char("Nom article", required=True)
    code_bare = fields.Char("Code barre")

    # Quantité et unité
    quantite = fields.Integer("Quantité sortie", required=True)
    unity = fields.Selection([
        ("pieces", "Pièce"),
        ("carton", "Carton"),
        ("poids", "Poids"),
        ("metre", "Mètre"),
    ], string="Unité de mesure")

    # Tarification
    prix_unitaire = fields.Float("Prix unitaire", required=True)
    prix_total = fields.Float("Total",readonly=True, compute="calcule_total")

    # Dates et utilisateur
    date_sortie = fields.Datetime("Date de sortie", default=fields.Datetime.now)
    nom_sortie = fields.Char("Nom du responsable de sortie")
    magasin = fields.Char("Magasin")

    # Documents
    bon_commande = fields.Char("Bon de commande")
    bon_livraison = fields.Char("Bon de livraison")
    numero_facture = fields.Char("Numéro de facture")
    bon_retour = fields.Text("Bon de retour")

    # État
    etat = fields.Selection([
        ("bon", "Bon"),
        ("mauvais", "Mauvais"),
    ], string="État de la sortie")

    @api.depends("quantite","prix_unitaire")
    def calcule_total(self):
        for calcul in self:
            calcul.prix_total = calcul.quantite * calcul.prix_unitaire
