from policyengine_canada.model_api import *


class cpp_retirement_pension(Variable):
    value_type = float
    entity = Person
    label = "CPP retirement pension"
    definition_period = YEAR
    unit = CAD
    documentation = "Annual CPP retirement pension amount"
    reference = "https://www.canada.ca/en/services/benefits/publicpensions/cpp/cpp-benefit/amount.html"

    def formula(person, period, parameters):
        p = parameters(period).gov.cra.benefits.cpp.retirement
        eligible = person("cpp_retirement_eligible", period)
        years_contributed = person("cpp_years_of_contribution", period)

        # Contribution factor: ratio of years contributed to maximum contributory period
        max_years = p.max_contributory_years
        contribution_factor = min_(years_contributed / max_years, 1)

        # Scale average monthly by contribution factor, cap at maximum monthly
        monthly_amount = min_(
            p.average_monthly * contribution_factor,
            p.maximum_monthly,
        )
        annual_amount = monthly_amount * 12

        return where(eligible, annual_amount, 0)
