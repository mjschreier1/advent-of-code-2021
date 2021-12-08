from typing import Dict

import utils as u


def main():
    u.pretty_print('Number of vent overlaps w/o diagonals', get_number_of_vent_overlaps('day-5-coordinates.txt', False))
    u.pretty_print('Number of vent overlaps w/ diagonals', get_number_of_vent_overlaps('day-5-coordinates.txt', True))


def get_number_of_vent_overlaps(vent_readings_file_path: str, include_diagonals: bool) -> int:
    vent_counts = {}
    with open(vent_readings_file_path) as f:
        for raw_line in f:
            line = parse_line(raw_line)
            if is_horizontal_line(line['y1'], line['y2']):
                increment_vents_horizontally(vent_counts, line['x1'], line['x2'], line['y1'])
            elif is_vertical_line(line['x1'], line['x2']):
                increment_vents_vertically(vent_counts, line['y1'], line['y2'], line['x1'])
            elif include_diagonals and is_diagonal_line(line['x1'], line['y1'], line['x2'], line['y2']):
                increment_vents_diagonally(vent_counts, line['x1'], line['x2'], line['y1'], line['y2'])
    return count_vent_overlaps(vent_counts)


def parse_line(raw_line: str) -> Dict[str, int]:
    coordinates = raw_line.split(' -> ')
    start_coordinate = coordinates[0].split(',')
    end_coordinate = coordinates[1].split(',')
    return {'x1': int(start_coordinate[0]), 'y1': int(start_coordinate[1]),
            'x2': int(end_coordinate[0]), 'y2': int(end_coordinate[1])}


def is_horizontal_line(y1: int, y2: int) -> bool:
    return y1 == y2


def is_vertical_line(x1: int, x2: int) -> bool:
    return x1 == x2


def is_diagonal_line(x1: int, y1: int, x2: int, y2: int) -> bool:
    return abs(x2 - x1) == abs(y2 - y1)


def increment_vents_horizontally(vent_counts: Dict[int, Dict[int, int]], x1: int, x2: int, y: int) -> None:
    low_x = (x1 if x1 < x2 else x2)
    high_x = (x1 if x1 > x2 else x2)
    for x in range(low_x, high_x + 1):
        safe_increment_dict_value(vent_counts, x, y)


def increment_vents_vertically(vent_counts: Dict[int, Dict[int, int]], y1: int, y2: int, x: int) -> None:
    low_y = (y1 if y1 < y2 else y2)
    high_y = (y1 if y1 > y2 else y2)
    for y in range(low_y, high_y + 1):
        safe_increment_dict_value(vent_counts, x, y)


def increment_vents_diagonally(vent_counts: Dict[int, Dict[int, int]], x1: int, x2: int, y1: int, y2: int) -> None:
    low_x = (x1 if x1 < x2 else x2)
    high_x = (x1 if x1 > x2 else x2)
    start_y = (y1 if low_x == x1 else y2)
    end_y = (y2 if start_y == y1 else y1)
    increment_y = end_y > start_y
    for i, x in enumerate(range(low_x, high_x + 1)):
        safe_increment_dict_value(vent_counts, x, (start_y + i if increment_y else start_y - i))


def count_vent_overlaps(vent_counts: Dict[int, Dict[int, int]]) -> int:
    count = 0
    for x in vent_counts:
        for y in vent_counts[x]:
            if vent_counts[x][y] > 1:
                count += 1
    return count


def safe_increment_dict_value(dictionary: Dict[int, Dict[int, int]], x: int, y: int) -> None:
    if x not in dictionary:
        dictionary[x] = {}
    if y not in dictionary[x]:
        dictionary[x][y] = 1
    else:
        dictionary[x][y] += 1


if __name__ == "__main__":
    main()
