import utils as u


def main():
    u.pretty_print('Number of lantern fish after 80 days', calculate_population('day-6-seed-data.txt', 80))
    u.pretty_print('Number of lantern fish after 256 days', calculate_population('day-6-seed-data.txt', 256))


def calculate_population(seed_data_path: str, num_days: int) -> int:
    seed_data = {}
    for i in range(9):
        seed_data[i] = 0
    with open(seed_data_path) as f:
        for fish_timer in f.readline().split(','):
            seed_data[int(fish_timer)] += 1
    return sum(simulate(seed_data, num_days).values())


def simulate(start_population: dict, days: int) -> dict:
    return start_population if days == 0 else simulate(simulate_day(start_population), days - 1)


def simulate_day(population: dict) -> dict:
    spawn_count = population[0]
    for i in range(8):
        population[i] = population[i + 1]
    population[6] += spawn_count
    population[8] = spawn_count
    return population


if __name__ == "__main__":
    main()
