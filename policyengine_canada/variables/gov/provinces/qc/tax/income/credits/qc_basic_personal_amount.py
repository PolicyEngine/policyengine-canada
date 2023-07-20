from policyengine_canada.model_api import *


class qc_basic_personal_amount(Variable):
    value_type = float
    entity = Person
    label = "Quebec basic personal amount"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.QC
    reference = "https://www.revenuquebec.ca/documents/en/formulaires/tp/2022-12/TP-1.D-V%282022-12%29.pdf"

    def formula(household, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits

        return p.basic_personal_amount
