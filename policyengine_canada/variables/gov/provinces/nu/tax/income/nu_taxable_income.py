from policyengine_canada.model_api import *


class nu_taxable_income(Variable):
    value_type = float
    entity = Person
    label = "Nunavut total taxable income"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.revenue.pa.gov/FormsandPublications/FormsforIndividuals/PIT/Documents/2021/2021_pa-40in.pdf#page=8"

    def formula(person, period, parameters):
        province = person.household("province", period)
        in_nunavut = province == province.possible_values.NUNAVUT
        province = person.household("province", period)
        in_nunavut = province == province.possible_values.NUNAVUT
        return in_nunavut * add(
            person, period, ["total_individual_pre_tax_income"]
        )
