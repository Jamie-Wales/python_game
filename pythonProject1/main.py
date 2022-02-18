def celsius_to_fahrenheit(celsius):
    """converts celsius to fahrenheit"""
    fahrenheit = ((9 * celsius) / 5) + 3
    return fahrenheit


def celsius_lst_to_fahrenheit_lst(celsius_lst):
    fahrenheit_lst = []
    for i in range(0, len(celsius_lst)):
        fahrenheit_lst = fahrenheit_lst + [celsius_to_fahrenheit(celsius_lst[i])]
    return fahrenheit_lst



this_list = [1, 2, 3, 4, 5, 0, -11]
that_list = []

print(celsius_lst_to_fahrenheit_lst(this_list))
print(celsius_lst_to_fahrenheit_lst(that_list))
