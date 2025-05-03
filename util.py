def convert_f_to_c(f):
    """
    Convert Fahrenheit to Celsius.
    :param f: Temperature in Fahrenheit
    :return: Temperature in Celsius
    """
    return (f - 32) * 5 / 9

#  create a function more flexable to convert between all units of temperature
def convert_temperature(value, from_unit, to_unit):
    """
    Convert temperature between different units.
    :param value: Temperature value to convert
    :param from_unit: Unit of the input temperature (C, F, K)
    :param to_unit: Unit of the output temperature (C, F, K)
    :return: Converted temperature value
    """
    # Convert input to Celsius
    if from_unit == 'F':
        celsius = convert_f_to_c(value)
    elif from_unit == 'K':
        celsius = value - 273.15
    else:
        celsius = value

    # Convert Celsius to output unit
    if to_unit == 'F':
        return celsius * 9 / 5 + 32
    elif to_unit == 'K':
        return celsius + 273.15
    else:
        return celsius