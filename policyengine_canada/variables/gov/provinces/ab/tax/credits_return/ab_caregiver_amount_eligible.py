from policyengine_canada.model_api import *


class ab_caregiver_amount_eligible_person(Variable):
    value_type = bool
    entity = Person
    label = "Eligible person for the Alberta caregiver amount"
    definition_period = YEAR
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1ab/td1ab-23e.pdf"
    defined_for = ProvinceCode.AB

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.ab.tax.income.credits.credits_return

        dependant_net_income = person("ab_dependant_net_income", period)

        return dependant_net_income <= p.upper_dependant_income_threshold
