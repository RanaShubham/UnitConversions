import pytest

from unit_converstions.main_unit_conversions.units import *

@pytest.mark.parametrize(
    'amount1, unit1, amount2, unit2, sum', [
        (100, Length.CM, 1, Length.M, 200 ),
        (100, Length.IN, 0, Length.CM, 100),
        (50, Length.YD, 50, Length.FT, 66.666667),
        (5.5, Length.FT, 0.7, Length.CM, 5.522965),
        (22/7, Length.KM, 88/7, Length.YD, 3.15435),
        (8, Length.YD, 4, Length.KM, 4382.45),
        (87/3, Mass.KG, 53/9, Mass.LB, 31.6711),
        (91/7, Mass.LB, 50, Mass.GM, 13.110),
        (345.7, Mass.OZ, 90, Mass.LB, 1785.7),
        (1, Mass.GM, 1, Mass.OZ, 29.349),
        (20, Volume.MilliL, 0.5, Volume.MilliL, 20.5),
        (30, Volume.GAL, 100, Volume.L, 56.417),
        (134, Volume.GAL, 0, Volume.MilliL, 134),
        (6, Volume.CU_M, 778.11, Volume.L, 6.77811)
    ]
)
def test_add_units_adding_two_values_of_same_unit_type_should_return_sum_in_smaller_unit\
                (amount1, unit1, amount2, unit2, sum):
    margin_of_error = abs(UnitHandler.add_units(amount1, unit1, amount2, unit2) - sum)
    assert margin_of_error < 0.1

@pytest.mark.parametrize(
    "amount1, unit1, amount2, unit2",[
        (1, Mass.LB, 1, Length.YD),
        (1, Volume.GAL, 1, Length.KM),
        (1, Mass.OZ, 1 , Volume.CU_M)
        ]
)
def test_add_units_adding_different_units_should_raise_UnitError(amount1, unit1, amount2, unit2):
    with pytest.raises(UnitError) as unit_error:
        UnitHandler.add_units(amount1, unit1, amount2, unit2)
    assert  unit_error.value.message == ExceptionType.UnitMismatchException

@pytest.mark.parametrize(
    "amount1, unit1, amount2, unit2",[
        ("x", Length.IN, 3, Length.FT),
        (3, Length.CM, 12j, Length.KM),
        (5, Volume.GAL, -8 , Volume.CU_M),
        ("t", Mass.LB, -8, Mass.KG)
    ]
)
def test_add_units_adding_units_with_unfit_quantifiers_should_raise_UnitError(amount1, unit1, amount2, unit2):
    with pytest.raises(UnitError) as unit_error:
        UnitHandler.add_units(amount1, unit1, amount2, unit2)
    assert  unit_error.value.message == ExceptionType.InvalidQuantityException

def test_add_units_adding_two_unrecognized_units_raises_UnitError():
    with pytest.raises(AttributeError):
        UnitHandler.add_units(1, Mass.METER, 1, Length.LITER)
