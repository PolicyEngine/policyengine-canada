from policyengine_canada.model_api import *


class qc_solidarity_eligibility(Variable):
    value_type = bool
    entity = Household
    label = "Quebec solidarity tax credit eligibility"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits.solidarity

        income = household("adjusted_family_net_income", period)

        person = household.members
        # Tax filer eligibility
        # You were 18 or older
        age_eligible = person("age", period) >= p.age_eligibility
        # You were younger than 18 and met all following requirements
        has_spouse = household("is_married", period)
        children = household("count_children", period)
        has_child = children > 0
        emancipated = person("is_emancipated", period)

        eligible = age_eligible | (has_spouse & has_child & emancipated)

        # family income eligibility
        additional_income = children * p.maximum_family_income.dependent_child

        income_limit = additional_income + where(
            has_spouse,
            p.maximum_family_income.individual_with_spouse_basic_income,
            p.maximum_family_income.individual_without_spouse_basic_income,
        )

        return eligible & (income < income_limit)
