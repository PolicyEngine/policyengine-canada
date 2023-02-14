from policyengine_canada.model_api import *


class bc_tax_reduction_credit(Variable):
    value_type = float
    entity = Person
    label = "British Columbia tax reduction credit"
    unit = CAD
    definition_period = YEAR

    def formula(person, period, parameters):
        income = person("bc_taxable_income", period)
        province = person.household("province", period)
        p = parameters(
            period
        ).gov.provinces.bc.tax.income.credits.bc_tax_reduction_credit
        in_bc = province == province.possible_values.BRITISH_COLUMBIA
        return in_bc * max_(p.base - p.reduction.calc(income), 0)
