import math
import operator
from itertools import accumulate

import utils as u


def main():
    u.pretty_print('Least amount of fuel to align the crabs at a constant fuel rate', calculate_optimized_fuel('day-7-start-positions.txt', False))
    u.pretty_print('Least amount of fuel to align the crabs at a variable fuel rate', calculate_optimized_fuel('day-7-start-positions.txt', True))


def calculate_optimized_fuel(positions_data_path: str, variable_rate: bool) -> int:
    positions = []
    with open(positions_data_path) as f:
        for position in f.readline().split(','):
            positions.append(int(position))
    # Populate the variable rate reference only if needed
    variable_rate_by_steps = (list(accumulate(range(max(positions) + 1), operator.add)) if variable_rate else None)
    optimized_fuel = math.inf
    for i in range(max(positions) + 1):
        fuel_to_position_i = 0
        for position in positions:
            fuel_to_position_i += (variable_rate_by_steps[abs(position - i)] if variable_rate else abs(position - i))
        if fuel_to_position_i < optimized_fuel:
            optimized_fuel = fuel_to_position_i
    return optimized_fuel


if __name__ == '__main__':
    main()
