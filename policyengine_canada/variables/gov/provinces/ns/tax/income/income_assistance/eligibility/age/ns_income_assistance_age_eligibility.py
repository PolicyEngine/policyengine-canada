from policyengine_canada.model_api import *


class ns_income_assistance_age_eligibility(Variable):
    value_type = bool
    entity = Person
    label = "Nova Scotia income assistance age eligibility"
    definition_period = YEAR
    defined_for = ProvinceCode.NS

    def formula(person, period, parameters):
        age = person("age", period)
        p = parameters(
            period
        ).gov.provinces.ns.tax.income.income_assistance.eligibility.age
        protective_services = person("in_need_of_protective_services", period)
        # Person is eligible if at or over 19 years of age
        # Person is eligible if between 16 and 19 years of age,
        # and is in need of protective services
        # The person in need of protective services is additionally required to:
        # attend an educational program not designated for student loan purposes;
        # participate in an employment plan;
        # access counselling or mediation services that was identified as necessary;
        # access medical services necessary to preserve their physical health;
        # live in a setting that provides a degree of supervision, accountability,
        # and guidance in accordance with their age and needs.
        # which are not modeled in the program.
        age_threshold = where(protective_services, p.lower, p.main)
        return age >= age_threshold
