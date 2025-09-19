class Games:
    def __init__(self, name, no_of_teams, no_in_team):
        self.name = name
        self.no_of_teams = no_of_teams
        self.no_in_team = no_in_team

    def display_info(self):
        print(f"Sport: {self.name}")
        print(f"Number of teams: {self.no_of_teams}")
        print(f"Players per team: {self.no_in_team}")
        print()  



football = Games("Football", 2, 11)
basketball = Games("Basketball", 2, 5)
rugby = Games("Rugby", 2, 15)
table_tennis = Games("Table Tennis", 2, 1)

football.display_info()
basketball.display_info()
rugby.display_info()
table_tennis.display_info()


