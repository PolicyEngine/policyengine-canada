from policyengine_canada.model_api import *


class ns_chargeable_earned_income(Variable):
    value_type = float
    entity = Person
    label = "Nova Scotia Income Assistance chargeable earned income"
    unit = CAD
    definition_period = YEAR
    reference = (
        "https://novascotia.ca/just/regulations/regs/esiaregs.htm#TOC2_4"
    )
    defined_for = ProvinceCode.NS

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.ns.tax.income.income_assistance.eligibility.income
        is_disabled = person("is_disabled", period)
        earned_income = p.earned_income
        chargeable_earned_income = p.earned_income_exemption_rates.calc(
            earned_income
        )
        # chargeable earned income for general employment
        chargeable_earned_income_supported = (
            p.earned_income_exemption_rates_supported.calc(earned_income)
        )
        # chargeable earned income for supported employment
        return (
            is_disabled,
            chargeable_earned_income_supported,
            chargeable_earned_income,
        )
