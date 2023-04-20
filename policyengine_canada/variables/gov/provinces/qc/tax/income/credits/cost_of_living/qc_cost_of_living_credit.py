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
        is_child = person("is_child", period)
        # (a)
        is_father = person("is_father", period)
        is_mother = person("is_mother", period)
        # (b)
        is_emancipated = person("is_emancipated", period)

        eligible = (
            is_adult
            | (is_child & is_father)
            | (is_child & is_mother)
            | (is_child & is_emancipated)
        )

        return max_(0, eligible * (p.base - p.reduction.calc(income)))
