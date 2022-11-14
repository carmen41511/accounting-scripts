"""Print out all the melons in our inventory."""


from melons import melon

# for m, char in melon:
#     print(m.upper())
#     for k, v in char:
#         print(f"{k}: {v}")
#     print('\n')

# for i in melon:
#     print(i.upper())
#     for k in melon[i]:
#         print(f"{k}: {melon[i][k]}")
#     print("\n")


def print_all_melons(melons):
    """Print each melon with corresponding attribute information."""

    for melon_name, attributes in melons.items():
        print(melon_name.upper())

        for attribute, value in attributes.items():
            print(f'{attribute}: {value}')

        print('===================================')


print_all_melons(melons)