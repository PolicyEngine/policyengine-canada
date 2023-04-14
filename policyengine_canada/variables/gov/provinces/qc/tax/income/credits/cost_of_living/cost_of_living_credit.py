from policyengine_canada.model_api import *


class cost_of_living_credit(Variable):
    value_type = float
    entity = Person
    label = "Quebec csot of living credit"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.cost_of_living
        income = person("individual_net_income", period)
        base = person("base", period)
        
        return max_(0, base - p.reduction.calc(income))
