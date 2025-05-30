from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Gestion_Reception(models.Model):
    _name = "gestion.reception"
    _description = "Models pour gérer la réception des produits"

    name = fields.Char("Nom article", required=True)
    code_bare = fields.Char("Code bare")

    quantite = fields.Integer("Quantité reçue", required=True)
    unity = fields.Selection([
        ("pieces", "Pièce"),
        ("carton", "Carton"),
        ("poids", "Poids"),
        ("metre", "Mètre"),
    ], string="Unité de mesure")

    prix_unitaire = fields.Float("Prix unitaire", required=True)
    prix_total = fields.Float("Total")

    date_reception = fields.Datetime("Date de réception", default=fields.Datetime.now)
    nom_reception = fields.Char("Nom du réceptionniste")
    magasin = fields.Char("Magasin")
    bon_commande = fields.Char("Bon de commande")
    bon_livraison = fields.Char("Bon de livraison")
    numero_facture = fields.Char("Numéro de facture")
    bon_retour = fields.Text("Bon de retour")
    etat = fields.Selection([
        ("bon", "Bon"),
        ("mauvais", "Mauvais"),
    ], string="État de la réception")
    
    def _check_quantity_stock(self):
        for record in self:
            if record.quantite < 5:
                raise ValidationError("en rupture de stock")

    

