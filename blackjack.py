import random
import os
import time
class JeremysBlackjack:
    def __init__(self):
        self.reset_game()
    def reset_game(self):
        self.choice = None
        self.round_count = 4
        self.score = 0
        self.dealer = self.create_deck()
        self.p1 = []
        self.p2 = []
        self.game_active = True
    def create_deck(self):
        suits = ['d', 'c', 'h', 's']
        ranks = {
            '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
            '7': 7, '8': 8, '9': 9, '10': 10,
            'J': 10, 'Q': 10, 'K': 10, 'A': 1
        }
        deck = []
        for suit in suits:
            for rank, value in ranks.items():
                card = (rank, suit, value)
                deck.append(card)
        random.shuffle(deck)
        return deck
    def deal_deck(self):
        self.reset_game()
        for _ in range(2):
            self.push(self.p1, "Player 1")
            self.push(self.p2, "Player 2")
        self.cls()
        self.players()
    def players(self):
        self.cls()
        if self.p1:
            self.player_turn(self.p1, "Player 1")
        if self.p2:
            self.player_turn(self.p2, "Player 2")
        self.round_summary()
    def player_turn(self, player, player_name):
        self.cls()
        while self.game_active:
            print(f"\nIt is {player_name}'s turn")
            print("\n1. View deck")
            print("2. Take A Card")
            print("3. Do nothing")
            print("4. Check Score\n")
            self.choice = input(f"Pick An Option via Number for {player_name}: ")
            if self.choice == "1":
                self.view_deck(player)
            elif self.choice == "2":
                self.push(player, player_name)
                break
            elif self.choice == "3":
                break
            elif self.choice == "4":
                print(f"{player_name}'s score: {self.sums(player)}")
            else:
                print("Please select 1-4: ")
    def cls(self):
        os.system('cls')
        time.sleep(0.1)
    def round_summary(self):
        self.cls()
        print(f"\nPlayer 1's Score is {self.sums(self.p1)}.")
        print(f"Player 2's Score is {self.sums(self.p2)}")
        print(f"That was the end of round {self.round_count}")
        self.round_count -= 1
        if self.bust(self.p1) and not self.bust(self.p2):
            print("Player 2 Won, Player 1 Busted")
        elif self.bust(self.p2) and not self.bust(self.p1):
            print("Player 1 Won, Player 2 Busted")
        elif self.bust(self.p1) and self.bust(self.p2):
            print("You both lose!!!! You both busted!!!")
        elif self.win(self.p1) and not self.win(self.p2):
            print("Player 1 Got 21, They Win!")
        elif self.win(self.p2) and not self.win(self.p1):
            print("Player 2 Got 21, They Win!")
        elif self.win(self.p1) and self.win(self.p2):
            print("You both got 21, draw!")
        elif self.no_rounds():
            print("Game Over, No Round Left!")
        else:
            print(f"It is now round {self.round_count}\n")
            input("Press enter to go to next round: ")
            self.players()
        self.game_active = False
    def bust(self, player):
        return self.sums(player) > 21
    def win(self, player):
        return self.sums(player) == 21
    def no_rounds(self):
        if self.round_count == 0:
            scores = [self.sums(self.p1), self.sums(self.p2)]
            valid_scores = []
            for score in scores:
                if score <= 21:
                    valid_scores.append(score)
            if valid_scores:
                winner = sorted(valid_scores)
                print(f"The order from last to first {winner}")
                if winner[1] == winner[0]:
                    print("It is a draw!")
                elif self.sums(self.p1) > self.sums(self.p2):
                    print("Player 1 Won!")
                else:
                    print("Player 2 Won!")
            else:
                print("By the last round everyone busted!")
            return True
        return False
    def view_deck(self, player):
        print(f"\nDealer Deck: {len(self.dealer)} cards")
        for card in player:
            print(f"{card[0]} of {card[1]}. ", end='')
    def sums(self, player):
        self.score = 0
        for card in player:
            self.score += card[2]
        return self.score
    def push(self, player, player_name):
        if len(self.dealer) > 0:
            dealer_card = self.dealer.pop(0)
            player.append(dealer_card)
            print(f"A card is dealt to {player_name}")
        else:
            print("\nAll of the dealer deck cards are gone!!!!")
    def main_menu(self):
        self.cls()
        while True:
            print("\nWelcome to the Main Menu")
            print("1. Start Game")
            print("2. Exit")
            self.choice = input("Pick An Option via Number: ")
            if self.choice == "1":
                self.deal_deck()
            elif self.choice == "2":
                break
            else:
                print("Please Select the Correct Number")
def main():
    run = JeremysBlackjack()
    run.main_menu()
main()