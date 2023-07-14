from policyengine_canada.model_api import *


class qc_basic_personal_amount(Variable):
    value_type = float
    entity = Person
    label = "Quebec basic personal amount"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.QC
    reference = "https://www.revenuquebec.ca/documents/en/formulaires/tp/2022-12/TP-1.D-V%282022-12%29.pdf"

    adds = "gov.provinces.qc.tax.income.credits.basic_personal_amount"
