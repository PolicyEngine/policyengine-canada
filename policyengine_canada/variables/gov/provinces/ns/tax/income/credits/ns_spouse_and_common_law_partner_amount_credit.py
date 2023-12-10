from policyengine_canada.model_api import *


class ns_spouse_and_common_law_partner_amount_credit(Variable):
    value_type = float
    entity = Household
    label = "Nova Scotia spouse and commonlaw partner amount credit"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.NS
    reference = (
        "https://hr.acadiau.ca/files/sites/hr/Payroll/Pensions%20&%20Benefits/NS_TD1_2022.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5003-c/5003-c-22e.pdf#page=1",
        "https://nslegislature.ca/sites/default/files/legc/statutes/income%20tax.pdf#page=24",
    )

    def formula(household, period, parameters):
        person = household.members
        spouse_income = person("spouse_income", period)
        total_spouse_income = household.sum(spouse_income)
        p = parameters(
            period
        ).gov.provinces.ns.tax.income.credits.spouse_and_common_law_partner_amount

        reduced_base_amount = max_(0, (p.base - total_spouse_income))
        # Adding married condition to avoid amount for single filers
        is_married = household("is_married", period)
        return min_(p.cap, reduced_base_amount) * is_married
