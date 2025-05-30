from odoo import models, fields, api

class Gestion_Ventes(models.Model):
    _name = "gestion.vente"
    _description = "Gestion des ventes de produits et articles"

    name = fields.Many2one("gestion.reception",required=True)
    quantite = fields.Integer("Quantité", required=True)
    prix_unitaire = fields.Float("Prix unitaire",related='name.prix_unitaire')
    prix_ht = fields.Float("Prix unitaire HT", required=True, compute="calcul_total")
    tva = fields.Float("Montant TVA", default=True, compute="calcul_tva")
    prix_ttc = fields.Float("Prix total TTC",defalut=True, compute="calcul_ttc")
    
    date_vente = fields.Datetime("Date de vente", default=fields.Datetime.now)
    
    unity = fields.Selection([
        ("pieces", "Pièce"),
        ("cartons", "Carton"),
        ("poids", "Poids"),
        ("metre", "Mètre"),
    ], string="Unité de mesure")

    bon_commande = fields.Char("Bon de commande")
    bon_livraison = fields.Char("Bon de livraison")
    numero_facture = fields.Char("Numéro de facture")
    bon_retour = fields.Text("Bon de retour")
    image = fields.Binary("Image")
    observation = fields.Text("Observation")

    @api.depends("quantite","prix_unitaire")
    def calcul_total(self):
        for calcul in self:
            calcul.prix_ht = calcul.quantite * calcul.prix_unitaire

    @api.depends("prix_ht")
    def calcul_tva(self):
        for calcul in self:
            calcul.tva = calcul.prix_ht * (20/100)
    
    @api.depends("prix_ht","tva")
    def calcul_ttc(self):
        for calcul in self:
            calcul.prix_ttc = calcul.prix_ht + calcul.tva

    def enregistrer (self) : 
        pass

