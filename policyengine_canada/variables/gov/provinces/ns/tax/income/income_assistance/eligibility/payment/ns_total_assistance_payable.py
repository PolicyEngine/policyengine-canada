from policyengine_canada.model_api import *


class ns_total_assistance_payable(Variable):
    value_type = float
    entity = Person
    label = "Nova Scotia Income Assistance total payable"
    unit = CAD
    definition_period = YEAR
    reference = "https://novascotia.ca/just/regulations/regs/esiaregs.htm#TOC2_4"
    defined_for = ProvinceCode.NS

    def formula(person, period, parameters):
        income = person("ns_taxable_income", period)
        chargeble_income = peroson("chargeble_income",period)
        ns_applicable_asset_amount = person ("ns_applicable_asset_amount", period)
        p = parameters(
            period
        ).gov.provinces.ns.tax.income.income_assistance.eligibility.payment
        return p.eligible_amount - chargeble_income - ns_applicable_asset_amount
