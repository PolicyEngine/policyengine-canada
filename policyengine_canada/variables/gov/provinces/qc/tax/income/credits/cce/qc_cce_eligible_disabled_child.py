from policyengine_canada.model_api import *


class qc_cce_eligible_disabled_child(Variable):
    value_type = bool
    entity = Person
    label = "Quebec children care expenses tax credits eligible disabled child"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits.cce

        income = person("individual_net_income", period)

        own_child = person("is_child_of_filer", period)
        dependant = person("is_dependant", period)
        disabled = person("is_disabled", period)

        qualifying_non_own_child_dependant = dependant & (income <= p.child_income_limit)
        return disabled & (own_child | qualifying_non_own_child_dependant)
