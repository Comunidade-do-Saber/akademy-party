# This file is part of SAGE Education.   The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
from trytond.model import fields, Unique
from trytond.pool import PoolMeta
from trytond.pyson import Eval, Not, Bool

_GENDER = [
    (None, ''),
    ('masculine', 'Masculine'), ('female', 'Female'),
    ('non_binary', 'Non-Binary'), ('gender_fluid', 'Gender Fluid'),
    ('agender', 'Agender'), ('transgender', 'Transgender'),
    ('bigenero', 'Bigenero'), ('genderqueer', 'Genderqueer'),
    ('two_spirit', 'Two-Spirit'), ('pangender', 'Pangender')
]

_MARITALSTATUS =  [
    (None, ''),
    ('single', 'Single'), ('married', 'Married'),
    ('divorced', 'Divorced'), ('widow(er)', 'Widow(er)'),
    ('separated', 'Separated'), ('common_law_marriage', 'Common-law Marriage'),
    ('open_relationship', 'Open Relationship'), ('registered_domestic_relationship', 'Registered Domestic Relationship'),
    ('civil_marriage', 'Civil Marriage'), ('religious_marriage', 'Religious Marriage')
]


class Party(metaclass=PoolMeta):
    'Party'
    __name__= 'party.party'    

    is_person = fields.Boolean(
        "Person", 
        states={
            'invisible': Bool(Eval('is_institution')), 
            'required': Not(Bool(Eval('is_institution')))
        }, depends=['is_institution'], 
        help="The entity is a person.")
    is_institution = fields.Boolean(
        "Institution", 
        states={
            'invisible':  Bool(Eval('is_person')), 
            'required': Not(Bool(Eval('is_person')))
        }, depends=['is_person'], 
        help="The entity is an organization.")
    date_birth = fields.Date(
        'Date birth', 
        states={
            'invisible': Not(Bool(Eval('is_person'))), 
            'required': Bool(Eval('is_person'))            
        }, help="The date of birth.")    
    gender = fields.Selection(_GENDER, string=u'Gender',         
        states={
            'invisible': Not(Bool(Eval('is_person'))), 
            'required': Bool(Eval('is_person'))
        })
    marital_status = fields.Selection(_MARITALSTATUS, string=u'Marital status', 
        states={
            'invisible': Not(Bool(Eval('is_person'))), 
            'required': Bool(Eval('is_person'))
        })
    bi_number = fields.Char(
        'ID nº', size=15,
        states={
            'invisible': Not(Bool(Eval('is_person')))
        }, help="The unique number identifier of a person.")
    father = fields.Many2One(
        'party.party', 'Father',
        states={
            'invisible': Not(Bool(Eval('is_person')))
        }, ondelete="RESTRICT", help="Father's name")
    mother = fields.Many2One(
        'party.party', 'Mother',
        states={
            'invisible': Not(Bool(Eval('is_person')))
        }, ondelete="RESTRICT", help="Mother's name.")    
