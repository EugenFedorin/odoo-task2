from odoo import fields, models


class HospitalDoctor(models.Model):
    _name = 'hospital.visit'
    _description = 'Hospital visit'

    name = fields.Char(required=True)
