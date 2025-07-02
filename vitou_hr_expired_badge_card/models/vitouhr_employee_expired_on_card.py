# -*- coding: utf-8 -*-
###############################################################################
#
#    Copyright (C) 2024-TODAY,
#    Author: REAM Vitou (reamvitou@yahoo.com)
#    Tel: +855 17 82 66 82
#
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class VitouHREmployeeExpiredOnCard(models.Model):
     # _name = 'vitoucms.hr.employee'
     #_inherit = ['mail.thread']
     _inherit = ['hr.employee']
     _description = 'Employee Expired on Card'
     #_rec_name = "provider"
     # _sql_constraints = [
     #      ('name_unique', 'unique(name)', "Currency Code is duplicated!"),
     # ]

     vitouhr_expired_date = fields.Date(string="Expired Date on Card", default=None, store=True)




#
# def unlink(self):
#      for rec in self:
#           domain = [('type_id', '=', rec.id)]
#           found = self.env['ittechnician.type'].sudo().search(domain)
#           if found:
#                raise ValidationError(_("Invalide this provider. \n there are related to this one" % rec.id))
#           return super().unlink()
