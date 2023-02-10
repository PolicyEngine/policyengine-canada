from policyengine_canada.model_api import *


class on_low_income_workers_tax_credit(Variable):
    value_type = float
    entity = Person
    label = "Post reduction of Ontario Low-Income Workers Tax Credit"
    unit = CAD
    definition_period = YEAR

    def formula(person, period, parameters):
        household = person.household
        base = person("on_low_income_workers_tax_credit_base", period)
        afni = household("adjusted_family_net_income", period)
        p = parameters(
            period
        ).gov.provinces.on.tax.income.credits.lift.reduction
        family = household("is_married", period)
        reduction = where(family, p.family.calc(afni), p.single.calc(afni))
        return max_(base - reduction, 0)
