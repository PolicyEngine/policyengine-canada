from policyengine_canada.model_api import *


class sk_caregiver_amount(Variable):
    value_type = float
    entity = Person
    label = "Saskatchewan Caregiver Amount"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk/td1sk-23e.pdf"
    defined_for = ProvinceCode.SK

    def formula(person, period, parameters):
        relative_live_eligibility = person("is_live_together", period)
        is_elderly_dependant = person("is_elderly_dependant", period)
        is_infirm_dependant = person("is_infirm_dependant", period)
        dependants_income = person("dependants_income", period)
        infirm_relative_age = person("infirm_relative_age", period)
        elderly_age = person("elderly_age", period)
        p = parameters(period).gov.provinces.sk.tax.income.credits.sk_caregiver_amount

        age_threshold = select([is_elderly_dependant == 1 & is_infirm_dependant == 0,
        is_elderly_dependant == 0 & is_infirm_dependant == 1,], 
        [p.elderly_age_threshold, p.infirm_age_threshold])
        age_eligibility = where(dependant_age >= age_threshold, 1, 0)
        dependants_income_eligibility = where(dependants_income <= p.lower_income_threshold, 1, 0)

        eligibility = relative_live_eligibility & age_eligibility & dependants_income_eligibility

        return where(eligibility == 1, p.amount, 0)