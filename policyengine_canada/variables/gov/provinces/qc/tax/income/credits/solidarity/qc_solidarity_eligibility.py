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

        person = household.members
        # Tax filer eligibility
        # You were 18 or older
        adult = person("is_adult", period)
        # You were younger than 18 and met all following requirements
        has_spouse = household("is_married", period)
        children = household("count_children", period)
        has_child = children > 0
        emancipated = person("is_emancipated", period)

        eligible = adult | (has_spouse & has_child & emancipated)

        # family income eligibility
        addtional_income = children * p.dependent_child

        maximum_income_limit = select(
            [has_spouse == True, has_spouse == False],
            [
                p.individual_with_spouse_basic_income + addtional_income,
                p.individual_without_spouse_basic_income + addtional_income,
            ],
        )

        return eligible & (income < maximum_income_limit)
