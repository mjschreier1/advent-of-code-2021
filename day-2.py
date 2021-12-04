import utils as u


def main():
    # Part 1
    coordinates = calculate_coordinates('day-2-movements.txt')
    depth = coordinates['y'] * -1
    horizontal_distance = coordinates['x']
    u.pretty_print('Depth:', depth)
    u.pretty_print('Horizontal Distance:', horizontal_distance)
    u.pretty_print('Depth x Horizontal Distance:', depth * horizontal_distance)
    # Part 2
    refined_coordinates = calculate_refined_coordinates('day-2-movements.txt')
    refined_depth = refined_coordinates['y'] * -1
    refined_horizontal_distance = refined_coordinates['x']
    u.pretty_print('Refined Depth:', refined_depth)
    u.pretty_print('Refined Horizontal Distance:', refined_horizontal_distance)
    u.pretty_print('Refined Depth x Refined Horizontal Distance:', refined_depth * refined_horizontal_distance)


def calculate_coordinates(movements_file: str) -> dict:
    coordinates = {
        'x': 0,
        'y': 0
    }
    with open(movements_file) as f:
        for raw_line in f:
            if raw_line.startswith('forward'):
                coordinates['x'] += int(raw_line[8:])
            elif raw_line.startswith('up'):
                coordinates['y'] += int(raw_line[3:])
            elif raw_line.startswith('down'):
                coordinates['y'] -= int(raw_line[5:])
            else:
                raise ValueError('Movement type not recognized')
    return coordinates


def calculate_refined_coordinates(movements_file: str) -> dict:
    coordinates = {
        'x': 0,
        'y': 0,
        'aim': 0
    }
    with open(movements_file) as f:
        for raw_line in f:
            if raw_line.startswith('forward'):
                val = int(raw_line[8:])
                coordinates['x'] += val
                coordinates['y'] -= (coordinates['aim'] * val)
            elif raw_line.startswith('up'):
                coordinates['aim'] -= int(raw_line[3:])
            elif raw_line.startswith('down'):
                coordinates['aim'] += int(raw_line[5:])
            else:
                raise ValueError('Movement type not recognized')
    return coordinates


if __name__ == '__main__':
    main()
