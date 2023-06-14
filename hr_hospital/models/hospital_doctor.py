from odoo import fields, models


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Hospital Doctor'

    name = fields.Char(required=True)
