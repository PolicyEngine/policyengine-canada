from policyengine_canada.model_api import *


class ntltc_over_base(Variable):
    value_type = bool
    entity = Person
    label = "Eligible child for the NTCB in the older bracket"
    definition_period = YEAR
    defined_for = ProvinceCode.NT

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.nt.tax.income.living_tax_credit.income_threshold
        income = person("income", period)
        return 942