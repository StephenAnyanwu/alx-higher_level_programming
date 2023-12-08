#!/usr/bin/python3

def roman_to_int(roman_string):
    """
    converts a Roman numeral to an integer (between 1 - 3999)

    Paramter
    --------
    roman_string : str
        roman numeral to be converted (uppercase)

    Returns
    -------
    int
        integer value of roman_string, or 0 if roman_string
        is not a string or None
    """

    if roman_string is None:
        return (0)
    roman_dict = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100,
            'D': 500, 'M': 1000
    }
    int_val = 0
    for i in range(len(roman_string)):
        if roman_string[i] not in roman_dict:
            return (0)
        if i > 0 and roman_dict[roman_string[i]] >\
                roman_dict[roman_string[i - 1]]:
            int_val = int_val + roman_dict[roman_string[i]] -\
                    2 * roman_dict[roman_string[i - 1]]
        else:
            int_val += roman_dict[roman_string[i]]
    return (int_val)
