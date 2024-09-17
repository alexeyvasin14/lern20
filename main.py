calls = 0


def count_calls():
    global calls
    calls = calls + 1


def string_info(str1):
    count_calls()
    strlen = len(str1)
    strup = str1.upper()
    strlow = str1.lower()
    return strlen, strup, strlow


def is_contains(string, list_to_search):
    count_calls()
    list_to_search_low = []
    for x in list_to_search:
        list_to_search_low.append(x.lower())

    if string.lower() in list_to_search_low:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(string_info('University'))
print(is_contains('tram', ['ram', 'tRam']))
print(is_contains('bus', ['Avtobus', 'tobus', 'urBAN']))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
