from Inheritance_lectures.player import Player


class Guild:

    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == self.name:
            return f'Player {player.name} is already in the guild.'

        if player.guild != Player.default_guild and player.guild != self.name:
            return f'Player {player.name} is in another guild.'

        self.players.append(player)
        player.guild = self.name
        return f'Welcome player {player.name} to the guild {self.name}'


    def kick_player(self, player_name: str):
        for current_player in self.players:
            if current_player.name == player_name:
                self.players.remove(current_player)
                current_player.guild = Player.default_guild
                return f'Player {player_name} has been removed from the guild.'
        return f'Player {player_name} is not in the guild.'


    def guild_info(self):
        final_result = f'Guild: {self.name}'
        for player in self.players:
            final_result += '\n'
            final_result += player.player_info()
        return final_result


