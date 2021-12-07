from typing.io import TextIO

import utils as u


def main():
    u.pretty_print('Score of best bingo card', calculate_score_of_best_bingo_card('day-4-bingo.txt'))
    u.pretty_print('Score of worst bingo card', calculate_score_of_worst_bingo_card('day-4-bingo.txt'))


def calculate_score_of_best_bingo_card(bingo_data_file: str) -> int:
    with open(bingo_data_file) as f:
        bingo_numbers = f.readline().split(',')
        bingo_cards = parse_bingo_cards(f)
    for i, number in enumerate(bingo_numbers):
        # No need to evaluate the cards until 5 numbers are called (when i == 4)
        winning_card_numbers = mark_number(bingo_cards, number, i > 3)
        if len(winning_card_numbers) > 0:
            return score_card(bingo_cards[winning_card_numbers[0]], int(number))
    raise ValueError('No winning card found!')


def calculate_score_of_worst_bingo_card(bingo_data_file: str) -> int:
    with open(bingo_data_file) as f:
        bingo_numbers = f.readline().split(',')
        bingo_cards = parse_bingo_cards(f)
    for i, number in enumerate(bingo_numbers):
        # No need to evaluate the cards until 5 numbers are called (when i == 4)
        winning_card_numbers = mark_number(bingo_cards, number, i > 3)
        for winning_card_number in reversed(winning_card_numbers):
            if len(bingo_cards) == 1:
                return score_card(bingo_cards[0], int(number))
            bingo_cards.pop(winning_card_number)


# Active bingo file should have a whitespace line above every bingo card
def parse_bingo_cards(active_bingo_file: TextIO) -> list:
    bingo_cards = []
    for _ in active_bingo_file:
        # Skip the current line of whitespace and read the next 5 instead
        current_card = []
        for _ in range(5):
            current_card.append(active_bingo_file.readline().split())
        bingo_cards.append(current_card)
    return bingo_cards


# Returns a list of any winning card numbers
def mark_number(cards: list, number: str, evaluate_cards: bool) -> list:
    winning_cards = []
    # 'i' represents card number, 'j' represents row number on that card, 'k' represents column within that row
    for i in range(len(cards)):
        number_found = False
        for j in range(5):
            for k in range(5):
                if cards[i][j][k] == number:
                    cards[i][j][k] = 'X'
                    number_found = True
                    if evaluate_cards and is_winning_card(cards[i], j, k):
                        winning_cards.append(i)
                    break
            if number_found:
                break
    return winning_cards


def is_winning_card(card: list, recent_number_row: int, recent_number_column: int) -> bool:
    return all(val == 'X' for val in card[recent_number_row]) or all(row[recent_number_column] == 'X' for row in card)


def score_card(card: list, recent_number: int) -> int:
    score = 0
    for row in card:
        for val in row:
            if val != 'X':
                score += int(val)
    return score * recent_number


if __name__ == "__main__":
    main()
