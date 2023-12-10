from policyengine_canada.model_api import *


class ns_pension_income_amount(Variable):
    value_type = float
    entity = Person
    label = "Nova Scotia pension income amount"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.NS
    reference = (
        "https://hr.acadiau.ca/files/sites/hr/Payroll/Pensions%20&%20Benefits/NS_TD1_2022.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5003-c/5003-c-22e.pdf#page=1",
        "https://nslegislature.ca/sites/default/files/legc/statutes/income%20tax.pdf#page=28",
    )

    def formula(person, period, parameters):
        cap = parameters(
            period
        ).gov.provinces.ns.tax.income.credits.pension_income_amount.cap
        pension_income_amount = person(
            "pension_and_savings_plan_income", period
        )

        return min_(pension_income_amount, cap)
