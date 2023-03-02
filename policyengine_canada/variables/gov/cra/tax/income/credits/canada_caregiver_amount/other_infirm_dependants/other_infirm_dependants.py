from policyengine_canada.model_api import *


class other_infirm_dependants(Variable):
    value_type = float
    entity = Person
    label = "Other infirm dependants amount"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s5/5000-s5-22e.pdf - Line 30450"

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.cra.tax.income.credits.canada_caregiver_amount
        dependant_income = person("dependant_income", period)
        eligible = person(
            "eligible_dependent_for_other_infirm_dependants_amount", period
        )
        return eligible * (
            min_(max_(p.base - dependant_income), 0),
            p.max_amount,
        )


# TODO: unit tests
