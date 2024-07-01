from policyengine_canada.model_api import *


class ab_caregiver_amount_eligible(Variable):
    value_type = float
    entity = Person
    label = "Alberta caregiver amount income eligibility"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1ab/td1ab-23e.pdf"
    defined_for = ProvinceCode.AB

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.ab.tax.income.credits.credits_return

        dependant_net_income = person("ab_dependant_net_income", period) * eligible_dependant

        income_eligibility = (
            dependant_net_income <= p.upper_dependant_income_threshold
        )

        return income_eligibility
