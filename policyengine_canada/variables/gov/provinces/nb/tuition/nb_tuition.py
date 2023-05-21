from policyengine_canada.model_api import *

# 1 2 3 4 5 6 7 8 9 10
# 1 unused_amont
# 2 amount from line 9 of federal s 11
# 3 1+2
# 4 if value<=44887 line 26000
#   else (line8 in From NB428)/0.094
# 5 line 31 from form NB428
# 6 max(0, 4-5)
# 7 min((1),(6))
# 8 (6-7)
# 9 min(2,8)
# 10 (7+9)
# 11 (3)
# 12 (10)
# 13 (11-12)
# if transfer:
#   14 min(5000,(2))
#   15 (9)
#   16 max(0,(14)-(15))
#   17 input the provincial amount
#   18 (13)-(17)
# else:
#   18 (13)

class nb_tuition(Variable):
    value_type = float
    entity = Tution
    label = "New Brunswick tuition amounts"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/canadian-income-tax-rates-individuals-current-previous-years.html"
    defined_for = ProvinceCode.NB

    def formula(person, period, parameters):
        income = person("nb_taxable_income", period)
        p = parameters(period).gov.provinces.nb.tax.income.rate
        return p.calc(income)
