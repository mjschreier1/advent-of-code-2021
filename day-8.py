import utils as u


def main():
    u.pretty_print('Number of 1s, 4s, 7s, 8s in outputs', number_of_easy_digits_in_outputs('day-8-signal-patterns.txt'))
    u.pretty_print('Sum of outputs', sum_outputs('day-8-signal-patterns.txt'))


def number_of_easy_digits_in_outputs(signal_patterns_data_path: str) -> int:
    count = 0
    with open(signal_patterns_data_path) as f:
        for raw_line in f:
            count += number_of_easy_digits_in_output(parse_signal_pattern(raw_line)['outputs'])
    return count


def sum_outputs(signal_patterns_data_path: str) -> int:
    count = 0
    with open(signal_patterns_data_path) as f:
        for raw_line in f:
            line_data = parse_signal_pattern(raw_line)
            count += calculate_output_value(get_digit_panel_configuration(line_data['inputs']), line_data['outputs'])
    return count


def parse_signal_pattern(pattern_data: str) -> dict:
    ins_and_outs = pattern_data.split(' | ')
    return {'inputs': ins_and_outs[0].split(), 'outputs': ins_and_outs[1].split()}


def number_of_easy_digits_in_output(outputs: list) -> int:
    easy_digits_lengths = [2, 4, 3, 7]
    count = 0
    for digit in outputs:
        if len(digit) in easy_digits_lengths:
            count += 1
    return count


def get_digit_panel_configuration(inputs: list) -> dict:
    digit_panels = {}
    # Start by identifying the panels in the digits that require a unique number of panels
    for digit in inputs:
        if len(digit) == 2:
            digit_panels[1] = [panel for panel in digit]
        elif len(digit) == 4:
            digit_panels[4] = [panel for panel in digit]
        elif len(digit) == 3:
            digit_panels[7] = [panel for panel in digit]
        elif len(digit) == 7:
            digit_panels[8] = [panel for panel in digit]
    # Then use those digits as a reference to identify the panels in the digits with a non-unique number of panels
    for digit in inputs:
        if len(digit) == 5:
            if all(panel in digit for panel in digit_panels[7]):
                digit_panels[3] = [panel for panel in digit]
            else:
                count_of_panels_of_4 = 0
                for panel in digit_panels[4]:
                    if panel in digit:
                        count_of_panels_of_4 += 1
                if count_of_panels_of_4 == 3:
                    digit_panels[5] = [panel for panel in digit]
                else:
                    digit_panels[2] = [panel for panel in digit]
        elif len(digit) == 6:
            if all(panel in digit for panel in digit_panels[4]):
                digit_panels[9] = [panel for panel in digit]
            elif all(panel in digit for panel in digit_panels[7]):
                digit_panels[0] = [panel for panel in digit]
            else:
                digit_panels[6] = [panel for panel in digit]
    return digit_panels


def calculate_output_value(digit_panel_configuration: dict, outputs: list) -> int:
    output_value = 0
    for i, digit in enumerate(reversed(outputs)):
        output_value += get_digit_value(digit_panel_configuration, digit) * pow(10, i)
    return output_value


def get_digit_value(digit_panel_configuration: dict, digit: str) -> int:
    if len(digit) == 2:
        return 1
    elif len(digit) == 4:
        return 4
    elif len(digit) == 3:
        return 7
    elif len(digit) == 7:
        return 8
    elif len(digit) == 5:
        if all(panel in digit for panel in digit_panel_configuration[2]):
            return 2
        elif all(panel in digit for panel in digit_panel_configuration[3]):
            return 3
        else:
            return 5
    # At this point, there must be 6 panels in the digit, so evaluate sub-conditions for 6 panels
    elif all(panel in digit for panel in digit_panel_configuration[0]):
        return 0
    elif all(panel in digit for panel in digit_panel_configuration[6]):
        return 6
    else:
        return 9


if __name__ == "__main__":
    main()
