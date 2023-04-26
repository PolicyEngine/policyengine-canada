from policyengine_canada.model_api import *


class cce_eligible_disabled_child(Variable):
    value_type = bool
    entity = Person
    label = "Quebec children care expenses tax credits eligible disabled child"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(person, period, parameters):
        dependent = person("is_dependent", period)
        disabled = person("is_disabled", period)

        return dependent & disabled

        # todo: a child who was your or your spouse's dependant and whose income for the year was not more than $11,081.-> make parameter
