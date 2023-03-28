from policyengine_canada.model_api import *


class nb_litr_base(Variable):
    value_type = float
    entity = Household
    label = "New Brunswick low income tax reduction base"
    definition_period = YEAR
    defined_for = ProvinceCode.NB

    def formula(household, period, parameters):
        person = household.members
        p = parameters(
            period
        ).gov.province.nb.tax.income.credits.low_income_tax_reduction
        married = household("is_married", period)
        dependant = person("is_dependent", period)
        return min_(
            p.base.max_amount,
            p.base.main
            + married * p.base.spouse
            + dependant * p.base.dependant,
        )
