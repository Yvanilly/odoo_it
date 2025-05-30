# -*- coding: utf-8 -*-

from odoo import models, fields, api


class gestion_achats(models.Model):
    _name = "gestion.achats"
    #name est le seul élément où il ne faut pas mettre d'espace
    _description = "gestion achat des produits et articles"

    name = fields.Char("Nom article",required=True)
    quantite = fields.Integer("Quantité", required=True)
    prix_unitaire = fields.Float("Prix unitaire", required=True)
    prix_total = fields.Float("Total",readonly=True, compute="calcule_total")
    date_achats = fields.Datetime("Date Achats",default=fields.Datetime.now)
    unity = fields.Selection([
        ("pieces", "Piece"),
        ("cartons","Carton"),
        ("poids","Poids"),
        ("metre","Metre"),
    ],string="unité")
    bon_commande = fields.Char("bon de commande")
    bon_livraison = fields.Char("bon de livraison")
    numero_facture = fields.Char("Numéro de facture")
    bon_retour = fields.Text("Bon retour")
    image = fields.Binary("Image")
    observation = fields.Text ("Observation")

    @api.depends("quantite","prix_unitaire")
    def calcule_total(self):
        for calcul in self:
            calcul.prix_total = calcul.quantite * calcul.prix_unitaire