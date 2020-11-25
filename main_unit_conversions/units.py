import logging
from enum import Enum
from Indian_state_analyzer.my_csv_analyzer.csv_reader_exception import UnitError, ExceptionType

class Length(Enum):
    M = 1
    KM = 1000
    CM = 0.01
    YD = 0.9144
    FT = 0.3048
    IN = 0.0254
    MI = 1609.34
    NanoM = 1e-9
    MilliM =0.001
    MicroM = 1e-6

class Mass(Enum):
    GM = 1
    KG = 1000
    LB = 453.592
    OZ = 28.3495
    TON = 1e+6
    MilliG = 0.001
    MicroG = 1e-6

class Volume(Enum):
    L = 1
    CU_M = 1000
    GAL = 3.78541
    MilliL = 0.001
    FLOZ = 0.0284131
    QT = 0.946353
    CUP = 0.24

logging.basicConfig(filename='./UnitsHandlling.log', level=logging.DEBUG,
                    format='%(asctime)s | %(levelname)s | %(message)s')

class UnitHandler:

    def add_units(amount1: (int, float), unit1, amount2: (int, float), unit2):
        '''
            To add two values of unit Length or Mass or  Volume.

            :raises UnitError if units are of different type.
            :param unit1: Unit to add
            :type unit1:Enum
            :param amount1: Value to add
            :type amount1: Number
            :param unit2: Enum
            :type unit2: Value to add
            :param amount2: Value to add.
            :type amount2: Number
            :return: Value
            :rtype: Number
        '''
        try:
            if (amount1 < 0 or amount2 < 0):
                raise UnitError(UnitError, ExceptionType.InvalidQuantityException)
            sum = amount1 + UnitHandler.convert(unit2, unit1, amount2)
            logging.debug("{}{} + {}{} = {}{}".format(amount1, unit1.name, amount2, unit2.name, sum, unit1.name))
            return sum
        except UnitError as my_error:
            raise UnitError(UnitError, my_error.message)
        except TypeError as invalid_amount_type:
            raise UnitError(invalid_amount_type, ExceptionType.InvalidQuantityException)
        except AttributeError as unknown_unit:
            raise UnitError(unknown_unit, ExceptionType.UnrecognizedUnitException)
        except Exception:
            raise UnitError(Exception, ExceptionType.MiscException)

    def convert(convert_from, convert_to, amount=1 or 1.0):
        '''
            Converts between units of same type. Returns value of  first argument's unit value in form of second argument's unit.

            :raises UnitError if argument are not of type Length and Mass and Volume
            :raises UnitError if arguments are not of same type.
            :param convert_from: Unit to convert from
            :type convert_from: Enum
            :param convert_to: Unit to convert to
            :type convert_to: Enum
            :return: converted value
            :rtype: float
        '''
        if type(convert_from) != type(convert_to):
            raise UnitError(UnitError, ExceptionType.UnitMismatchException)
        try:
            if (amount < 0):
                raise UnitError(UnitError, ExceptionType.InvalidQuantityException)
            converted_value = amount * (convert_from.value/convert_to.value)
            logging.debug("{} {} ---> {} {}".format(amount, convert_from.name, converted_value, convert_to.name))
            return converted_value
        except TypeError as invalid_quantifier:
            raise UnitError(invalid_quantifier, ExceptionType.InvalidQuantityException)
        except AttributeError as unknown_unit:
            raise UnitError(unknown_unit, ExceptionType.UnrecognizedUnitException)


UnitHandler.convert(Mass.KG, Mass.LB, 75)
UnitHandler.convert(Mass.KG, Mass.LB, 85)
UnitHandler.convert(Length.CM, Length.FT, 168)

UnitHandler.add_units(100, Length.FT, 0.5, Length.KM)
UnitHandler.add_units(50, Length.IN, 1/3, Length.YD)
UnitHandler.add_units(1/5, Length.KM, 199, Length.FT)

UnitHandler.convert(Length.KM, Length.NanoM, 10**10)