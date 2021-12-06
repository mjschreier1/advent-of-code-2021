import utils as u


def main():
    u.pretty_print('Power Consumption', get_power_readings('day-3-power-readings.txt'))
    u.pretty_print('Life Support Ratings', get_life_support_ratings('day-3-power-readings.txt'))


def get_power_readings(power_readings_file: str) -> dict:
    bit_cardinality = []
    with open(power_readings_file) as f:
        for raw_line in f:
            # Initialize the cardinality tracker on the first iteration (when the length of the list is 0),
            # then track using the existing cardinalities
            if len(bit_cardinality) == 0:
                for power_reading in raw_line:
                    if power_reading != '\n':
                        bit_cardinality.append(1 if power_reading == '1' else -1)
            else:
                for i, power_reading in enumerate(raw_line):
                    if power_reading != '\n':
                        bit_cardinality[i] += 1 if power_reading == '1' else -1
    return calculate_power(bit_cardinality)


# Convert cardinalities to actual bits (and invert each bit for the epsilon rate)
def calculate_power(reading_cardinalities: list) -> dict:
    gamma_rate = 0
    epsilon_rate = 0
    for cardinality in reading_cardinalities:
        gamma_rate = (gamma_rate << 1) | (1 if cardinality > 0 else 0)
        epsilon_rate = (epsilon_rate << 1) | (0 if cardinality > 0 else 1)
    return {
        'gamma_rate': gamma_rate,
        'epsilon_rate': epsilon_rate,
        'total_power': gamma_rate * epsilon_rate
    }


def get_life_support_ratings(power_readings_file: str) -> dict:
    # Simply kick off the recursive 'calculate' function using blank strings and return the result
    return calculate_life_support_ratings(power_readings_file, {'o2': '', 'co2': ''})


def calculate_life_support_ratings(power_readings_file: str, current_calculation: dict) -> dict:
    bit_to_calculate = len(current_calculation['o2'])
    o2_bit_cardinality = 0
    co2_bit_cardinality = 0
    # Need to track whether both a 0 and 1 have been found for co2 because the bit to return must be found at least once
    # If the least common bit was found 0 times, it should not be returned!
    co2_both_digits_found = False
    with open(power_readings_file) as f:
        for raw_line in f:
            # Once the new-line character is reached, there are no more digits to consider, so prepare the final output
            # Otherwise, drill-down to the next digit and make a recursive call back to this function
            if raw_line[bit_to_calculate:bit_to_calculate + 1] == '\n':
                o2_rating = int(current_calculation['o2'], 2)
                co2_rating = int(current_calculation['co2'], 2)
                return {
                    'o2': o2_rating,
                    'co2': co2_rating,
                    'total_life_support': o2_rating * co2_rating,
                    'asBinary': current_calculation
                }
            else:
                # Only consider lines that start with the current starting patterns for o2 and co2
                if raw_line.startswith(current_calculation['o2']):
                    o2_bit_cardinality += 1 if raw_line[bit_to_calculate:bit_to_calculate + 1] == '1' else -1
                if raw_line.startswith(current_calculation['co2']):
                    digit_to_add = 1 if raw_line[bit_to_calculate:bit_to_calculate + 1] == '1' else -1
                    if not co2_both_digits_found and ((co2_bit_cardinality > 0 and digit_to_add < 0) or (co2_bit_cardinality < 0 and digit_to_add > 0)):
                        co2_both_digits_found = True
                    co2_bit_cardinality += digit_to_add
    next_co2_bit_is_one = ((co2_bit_cardinality < 0) if co2_both_digits_found else (co2_bit_cardinality > 0))
    return calculate_life_support_ratings(
        power_readings_file,
        {
            'o2': current_calculation['o2'] + ('1' if o2_bit_cardinality > -1 else '0'),
            'co2': current_calculation['co2'] + ('1' if next_co2_bit_is_one else '0')
        }
    )


if __name__ == '__main__':
    main()
