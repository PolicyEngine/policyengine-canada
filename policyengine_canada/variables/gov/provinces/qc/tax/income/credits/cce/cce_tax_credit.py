from policyengine_canada.model_api import *


class cce_tax_credit(Variable):
    value_type = float
    entity = Household
    label = "Quebec childcare expenses tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits.cce

        income = household("adjusted_family_net_income", period)
        eligible = household("cce_eligible_child", period)

        return eligible * (p.rate * income)


# todo: limit credit
