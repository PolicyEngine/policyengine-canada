from policyengine_canada.model_api import *


class qc_solidarity_tax_filer_self_eligibility(Variable):
    value_type = bool
    entity = Person
    label = "Quebec solidarity tax credit tax filer self eligibility"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits.solidarity
        # You were 18 or older
        adult = person("is_adult", period)

        # You were younger than 18 and met all following requirements
        has_spouse = person("has_spouse", period)
        has_child = person("own_children_in_household", period) > 0
        emancipated = person("is_emancipated", period)

        return adult | (has_spouse & has_child & emancipated)
