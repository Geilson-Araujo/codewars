# Consider an array of sheep where some sheep may be missing
# from their place.
# We need a function that counts the number of sheep present
# in the array (true means present).
# Hint: Don't forget to check for bad values like null/undefined.


def count_sheeps(array_of_sheeps: list) -> int:
    return array_of_sheeps.count(True)
