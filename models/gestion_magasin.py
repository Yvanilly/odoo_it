from odoo import models, fields, api

class Gestion_Magasin(models.Model):
    _name = "gestion.magasin"
    _description = "Modèle pour gérer les mouvements de stock dans le magasin"

    name = fields.Char("Nom de l'article", required=True)
    code_bare = fields.Char("Code-bare")

    quantite_stock = fields.Integer("Quantité en stock", required=True)
    unity = fields.Selection([
        ("pieces", "Pièce"),
        ("carton", "Carton"),
        ("poids", "Poids"),
        ("metre", "Mètre"),
    ], string="Unité de mesure")

    emplacement = fields.Char("Emplacement dans le magasin")
    seuil_alerte = fields.Integer("Seuil d'alerte")
    
    prix_unitaire = fields.Float("Prix unitaire")
    prix_total = fields.Float("Valeur totale", compute="_compute_prix_total", store=True)

    date_mise_a_jour = fields.Datetime("Date de mise à jour", default=fields.Datetime.now)

    etat = fields.Selection([
        ("disponible", "Disponible"),
        ("bas_stock", "Bas stock"),
        ("rupture", "Rupture de stock")
    ], string="État du stock", compute="_compute_etat", store=True)

    @api.depends("quantite_stock", "prix_unitaire")
    def _compute_prix_total(self):
        for record in self:
            record.prix_total = record.quantite_stock * record.prix_unitaire

    @api.depends("quantite_stock", "seuil_alerte")
    def _compute_etat(self):
        for record in self:
            if record.quantite_stock == 0:
                record.etat = "rupture"
            elif record.quantite_stock <= record.seuil_alerte:
                record.etat = "bas_stock"
            else:
                record.etat = "disponible"