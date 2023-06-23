from policyengine_canada.model_api import *


class qc_solidarity_eligibility(Variable):
    value_type = bool
    entity = Household
    label = "Quebec solidarity tax credit eligibility"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.solidarity.maximum_family_income

        income = household("adjusted_family_net_income", period)

        # family situation
        has_spouse = household("is_married", period)

        children = household("count_children", period)
        addtional_income = children * p.dependent_child

        if has_spouse == True:
            maximum_income_limit = (
                p.individual_with_spouse_basic_income + addtional_income
            )
        else:
            maximum_income_limit = (
                p.individual_without_spouse_basic_income + addtional_income
            )

        return (
            add(
                household, period, ["qc_solidarity_tax_filer_self_eligibility"]
            )
            > 0
        ) & (income < maximum_income_limit)
