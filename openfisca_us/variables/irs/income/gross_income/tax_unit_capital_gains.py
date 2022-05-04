from openfisca_us.model_api import *


class tax_unit_capital_gains(Variable):
    value_type = float
    entity = TaxUnit
    label = "Tax unit capital gains"
    unit = USD
    definition_period = YEAR

    formula = sum_of_variables(["capital_gains"])