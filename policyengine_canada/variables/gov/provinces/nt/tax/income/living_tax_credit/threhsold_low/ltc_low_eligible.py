from policyengine_canada.model_api import *


class ntcb_older_eligible_child(Variable):
    value_type = bool
    entity = Household
    label = "Base income level for all middle income"
    definition_period = YEAR
    defined_for = ProvinceCode.NT

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.nt.tax.income.living_tax_credit.threshold_low.low
        income = Household("income", period)
        
        return p.low_threshold >= income