from policyengine_canada.model_api import *


class nb_tuition_credit_amount(Variable):
    value_type = float
    entity = Person
    label = "New Brunswick tuition credit amount"
    definition_period = YEAR
    defined_for: "nb_tuition_eligible"
    reference = (
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5004-s11/5004-s11-22e.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5004-c/5004-c-22e.pdf#page=1",
    )

    def formula(person, period, parameters):
        age = person("age", period)
        tuition = person("tuition_expenses", period)  # line 2
        taxable_income = person("nb_taxable_income", period)  # line 4
        tuition_income = person(
            "nb_tuition_credit_amount_income", period
        )  # line 5
        p = parameters(
            period
        ).gov.provinces.nb.tax.income.credits.tuition_amount
        return select(
            [
                taxable_income
                <= p.nb_tax_on_taxable_income_threshold.thresholds[1],
                taxable_income
                > p.nb_tax_on_taxable_income_threshold.thresholds[1],
            ],
            [
                min_(max_(taxable_income - tuition_income, 0), tuition),
                min_(
                    max_(
                        (
                            p.nb_tax_on_taxable_income_threshold.calc(
                                taxable_income
                            )
                            / p.nb_tax_on_taxable_income_rate
                        )
                        - tuition_income,
                        0,
                    ),
                    tuition,
                ),
            ],
        )
