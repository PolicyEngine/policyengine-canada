from policyengine_canada.model_api import *


class is_infirm_dependant(Variable):
    value_type = bool
    entity = Person
    label = "Is an infirm dependant"
    definition_period = YEAR

    # Impute dependant status on age.
    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.ab.tax.income.credits.infirm_dependant
        return person("age", period) >= p.infirm_dependant_age
