from policyengine_canada.model_api import *


class bc_comprehensive_tax_credits(Variable):
    value_type = float
    entity = Person
    label = "British Columbia comprehensive tax credits"
    unit = CAD
    definition_period = YEAR
    reference = (
        # C	is the smaller of the value of "B" and the amount that would be the individual's tax payable under
        # this Act for the year if the only amounts deductible were the amounts under the following sections:
        # (a)	section 4.3 [personal credits];
        # (b)	section 4.31 [age credit];
        # (c)	section 4.32 [pension credit];
        # (c.1)	section 4.33 [adoption expense credit];
        # (c.2)	and (c.21) [Repealed 2017-12-30.]
        # (c.3)	[Repealed 2017-12-30.]
        # (c.31)	[Repealed 2017-12-29.]
        # (c.4)	section 4.36 [BC education coaching tax credit];
        # (c.5)	section 4.37 [tax credit for volunteer firefighters and search and rescue volunteers];
        # (d)	section 4.51 [credit for mental or physical impairment];
        # (e)	section 4.64 [credit for EI premium and CPP contribution],
        "https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96215_00_multi#section4.62",  # § 4.62
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5010-c/5010-c-22e.pdf#page=1",  # Line 40
    )
    defined_for = ProvinceCode.BC
