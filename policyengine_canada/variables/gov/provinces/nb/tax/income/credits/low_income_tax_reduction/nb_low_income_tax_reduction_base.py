from policyengine_canada.model_api import *


class nb_low_income_tax_reduction_base(Variable):
    value_type = float
    entity = Household
    label = "New Brunswick low income tax reduction base"
    definition_period = YEAR
    defined_for = ProvinceCode.NB

    def formula(household, period, parameters):
        person = household.members
        p = parameters(
            period
        ).gov.provinces.nb.tax.income.credits.low_income_tax_reduction
        married = household("is_married", period)
        dependant = person("is_dependant", period)
        return min_(
            p.base.max_amount,
            p.base.head
            + married * p.base.spouse
            + dependant * p.base.dependant,
        )
