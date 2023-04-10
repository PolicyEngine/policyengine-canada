from policyengine_canada.model_api import *


class ntcb_older_eligible_child(Variable):
    value_type = bool
    entity = Person
    label = "Base income level for all higher income"
    definition_period = YEAR
    defined_for = ProvinceCode.NT

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.nt.tax.income.threshold_high
        income = person("income", period)
        
        return p.base <= income