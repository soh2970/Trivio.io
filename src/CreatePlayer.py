import json

def update_player_bank(self, game_state):
        # Load the current player bank
        with open('playerBank.json', 'w') as file:
            player_bank = json.load(file)
            player_id = self.player.playerId

            # Update game history and current saved game
            if player_id in player_bank:
                player_bank[player_id]['gameHistory'].append(game_state)
                player_bank[player_id]['currentSavedGame'] = game_state
            else:
                # If the player is new, initialize their data structure
                player_bank[player_id] = {
                    'password': 'default_password',  # Set a default or new password
                    'gameHistory': [game_state],
                    'currentSavedGame': game_state
                }
            
            # Save back to file
            file.seek(0)  # Go to the beginning of the file
            json.dump(player_bank, file, indent=4)
            file.truncate()  # Remove any excess data from the file

#update currentSavedGame (overrides)
#update gameHistory (append)