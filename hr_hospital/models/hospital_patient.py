from odoo import fields, models


class HospitalDoctor(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital patient'

    name = fields.Char(required=True)
