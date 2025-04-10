import random
should_continue = True
bank = 1000


def play_game():
    """
    Player can restart game after exhausting money in the bank.
    The bank variable is returned to 1000 on line 116
    """
    global bank

    def process():
        """
        Allows user to keep playing game while there's still money in the bank,
        note that the bank value is adjusted based on win or loss status of player
        """
        stake = int(input("How much are you staking?"))

        def cash(win_or_lose, amount):
            """
            Adjusts bank value based on the player's stake (amount) and win or loss status
            """
            global bank
            if win_or_lose == "win":
                bank += amount
            elif win_or_lose == "lose":
                bank -= amount
            print(f"You have {bank} left")
            return bank

        player_cards = []
        computer_cards = []
        player_cards_sum = 0

        def draw(player_computer_card):
            """
            Draw cards for both computer and player, sums cards value and compare
            """
            cards = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "King", "Queen"]
            special_cards = {
                "Ace": {
                    "Ace_value": 11,
                    "sum greater than 21": 1
                },
                "Jack": 10,
                "King": 10,
                "Queen": 10
            }

            card = random.choice(cards)
            player_computer_card.append(card)
            player_or_user_sum = 0
            for card in player_computer_card:
                if card in special_cards and card != "Ace":
                    player_or_user_sum += special_cards[card]
                elif card != "Ace":
                    player_or_user_sum += card
            for card in player_computer_card:
                # Factoring Ace values based on if sum of cards is greater than 21
                if card == "Ace":
                    player_or_user_sum += special_cards["Ace"]["Ace_value"]
                    if player_or_user_sum > 21:
                        player_or_user_sum -= special_cards["Ace"]["Ace_value"]
                        player_or_user_sum += special_cards["Ace"]["sum greater than 21"]
            return player_or_user_sum

        # Draw only one card for computer and hide second card with X
        computer_card_sum = draw(computer_cards)
        computer_cards.append("X")

        # Draw two cards for player
        for _ in range(2):
            player_cards_sum = draw(player_cards)

        print(f"Computer cards: {computer_cards}")
        computer_cards.pop()
        print(f"Player cards: {player_cards}")
        print(f" Player sum: {player_cards_sum}")

        if player_cards_sum == 21:
            print("BLACKJACK!!! You win")
            status = "win"
            bank = cash(status, stake)
        else:
            user_choice = "hit"
            while player_cards_sum < 21 and user_choice == "hit":
                user_choice = input("Hit or Stand or Double: ").lower()
                if user_choice == "hit":
                    player_cards_sum = draw(player_cards)
                    print(f"Player cards: {player_cards}")
                    print(f" Player sum: {player_cards_sum}")
                elif user_choice == "stand":
                    while computer_card_sum < 17:
                        computer_card_sum = draw(computer_cards)
                    print(f"Computer cards: {computer_cards}")
                    print(f"Computer sum: {computer_card_sum}")
                elif user_choice == "double":
                    stake += stake
                    print(f"You are now staking {stake}")
                    player_cards_sum = draw(player_cards)
                    print(f"Player cards: {player_cards}")
                    print(f" Player sum: {player_cards_sum}")

            def comparison():
                global bank
                if player_cards_sum > 21:
                    print("Busted!! Dealer wins")
                    bank = cash("lose", stake)
                elif computer_card_sum == 21:
                    print(computer_cards)
                    print("BLACKJACK!!!, Dealer wins")
                    bank = cash("lose", stake)
                elif computer_card_sum > 21:
                    print("You win!!!, Dealer Busted")
                    bank = cash("win", stake)
                elif player_cards_sum > computer_card_sum:
                    print("You win!!!")
                    bank = cash("win", stake)
                elif player_cards_sum < computer_card_sum:
                    print("Dealer wins!!!")
                    bank = cash("lose", stake)
                else:
                    print("Draw!!!")

            comparison()

    while bank > 0:
        process()

    play = input("Restart game: 'y' or 'n'").lower
    bank = 1000
    if play == 'n':
        global should_continue
        should_continue = False


while should_continue:
    play_game()
