from policyengine_canada.model_api import *


class basic_personal_amount_supplement(Variable):
    value_type = float
    entity = Person
    label = "Basic Personal Amount"
    unit = CAD
    definition_period = YEAR

    def formula(person, period, parameters):
        income = person("individual_net_income", period)
        p = parameters(period).gov.cra.tax.income.credits.basic_personal_amount
        max_amount = p.max_amount
        base = p.base
        phase_out_rate = where(
            income > p.phase_out.threshold.start,
            min_(
                (income - p.phase_out.threshold.start)
                / (p.phase_out.threshold.end - p.phase_out.threshold.start),
                1,
            ),
            0,
        )
        return (max_amount - base) - ((max_amount - base) * phase_out_rate)
