from policyengine_canada.model_api import *


class qc_cost_of_living_credit(Variable):
    value_type = float
    entity = Person
    label = "Quebec cost of living credit"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.cost_of_living
        income = person("individual_net_income", period)

        # determine eligibility:
        # You were 18 or over or, if you were under 18, you:
        # (a) were the father or mother of a child who lived with you; or
        # (b) were recognized as an emancipated minor by a competent authority (such as a court)
        is_adult = person("is_adult", period)

        # (a)
        is_parent = person("own_children_in_household", period) > 0
        # (b)
        is_emancipated = person("is_emancipated", period)

        eligible = is_adult | is_parent | is_emancipated
        amount_if_eligible = max_(0, p.base - p.reduction.calc(income))
        return eligible * amount_if_eligible
