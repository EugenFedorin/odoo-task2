from odoo import fields, models


class HospitalDisease(models.Model):
    _name = 'hospital.disease'
    _description = 'Hospital disease'

    name = fields.Char(required=True)
