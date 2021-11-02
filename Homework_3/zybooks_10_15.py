#  Helmut Brenner  #
#  2037275  #

class Team:
    def __init__(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def get_win_percentage(self):
        win_percentage = float(self.team_wins) / (self.team_wins + self.team_losses)
        return win_percentage


if __name__ == '__main__':
    team = Team()

    team.team_name = str(input())
    team.team_wins = float(input())
    team.team_losses = float(input())

    win_percent = team.get_win_percentage()

    if win_percent >= 0.5:
        print('Congratulations, Team {} has a winning average!'.format(team.team_name))
    else:
        print('Team {} has a losing average.'.format(team.team_name))
