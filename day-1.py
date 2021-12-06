import utils as u


def main():
    u.pretty_print('Number of times depth increased', count_increasing_depths())
    u.pretty_print('Number of times normalized depth increased', count_normalized_increasing_depths())


def count_increasing_depths():
    count = 0
    with open('day-1-depths.txt') as f:
        previous_depth = int(f.readline())
        for raw_line in f:
            line = int(raw_line)
            if line > previous_depth:
                count += 1
            # Set up next iteration
            previous_depth = line
    return count


# According to the prompt, normalization is defined as:
# Rather than counting when individual values increase, count each time the sum of the most recent 3 values increase
def count_normalized_increasing_depths():
    count = 0
    with open('day-1-depths.txt') as f:
        values_to_normalize = [int(f.readline()), int(f.readline()), int(f.readline())]
        previous_normalized_depth = sum(values_to_normalize)
        i = 3
        for raw_line in f:
            values_to_normalize[i % 3] = int(raw_line)
            current_normalized_depth = sum(values_to_normalize)
            if current_normalized_depth > previous_normalized_depth:
                count += 1
            # Set up next iteration
            previous_normalized_depth = current_normalized_depth
            i += 1
    return count


if __name__ == '__main__':
    main()
