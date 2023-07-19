from policyengine_canada.model_api import *


class ns_chargeable_income(Variable):
    value_type = float
    entity = Person
    label = "Nova Scotia Income Assistance chargeable income"
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
        earned_income = person("ns_chargeable_earned_income", period)
        rent_received = person("ns_chargeable_rent_income", period)
        training_allowance = person("ns_training_allowance", period)
        net_training_allowance = max_(
            0, (training_allowance - p.training_allowance_exempt)
        )
        harvest_connection_program_wages = person(
            "ns_harvest_connection_program_wages", period
        )
        net_harvest_connection_program_wages = max_(
            0,
            (
                harvest_connection_program_wages
                - p.harvest_connection_program_wages_exempt
            ),
        )

        return (
            p.unearned_income
            + earned_income
            + rent_received
            + net_training_allowance
            + net_harvest_connection_program_wages
        )
