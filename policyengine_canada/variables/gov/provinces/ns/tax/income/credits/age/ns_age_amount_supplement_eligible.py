from policyengine_canada.model_api import *


class ns_age_amount_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Eligible for the Nova Scotia age amount and age amount supplement"
    definition_period = YEAR
    defined_for = ProvinceCode.NS
    reference = (
        "https://hr.acadiau.ca/files/sites/hr/Payroll/Pensions%20&%20Benefits/NS_TD1_2022.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1ns-ws/td1ns-ws-23e.pdf#page=1",
        "https://nslegislature.ca/sites/default/files/legc/statutes/income%20tax.pdf#page=28",
    )

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.ns.tax.income.credits.age
        age = person("age", period)

        # is eligible for age amount supplement
        return age >= p.age_eligibility
