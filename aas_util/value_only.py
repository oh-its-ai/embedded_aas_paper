import aas_core3.types as aas_types


def property_type_switch(option: aas_types.DataTypeDefXSD, value):
    switch = {
        aas_types.DataTypeDefXSD.STRING: str(value),
        aas_types.DataTypeDefXSD.LONG: int(value)
    }

    return switch.get(option, str)()


def value_only(value):
    if isinstance(value, aas_types.Property):
        return_value = {
            value.id_short: property_type_switch(value.value_type, value=value.value)
        }
        print(return_value)

        return return_value
