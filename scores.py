class ScoreTracker:
    def __init__(self, username = ''):
        self.streak = 0
        self.correctly_guessed = []
        self.cumulative_attempts = 0
        self.username = username

    # Updates the users streak and accumulated score after the word has been guessed.
    def append_score(self, word, attempts_left):
        self.streak += 1
        self.correctly_guessed.append(word)
        self.cumulative_attempts += attempts_left

    # Prints the users current streak and accumulated score to the screen. 
    def display(self):
        print("\nStreak:", self.streak)
        print("Correctly guessed countries:")
        for country in self.correctly_guessed:
            print(" -", country)
        print("Total accumulated attempts from wins:", self.cumulative_attempts)

    # Reset player streak and accumulated score.
    def reset(self):
        self.streak = 0
        self.correctly_guessed.clear()
        self.cumulative_attempts = 0
        print("\nScore Reset.")

    # Updates the leaderboard with the highest score for that username. 
    def leaderboard(self):
        lines = []
        found = False
        updated = False
        formatted_line = "{:<15}{:^10}{:^20}\n".format(self.username, self.streak, self.cumulative_attempts)

        try:
            with open("leaderboard.txt", "r") as file:
                lines = file.readlines()
        except FileNotFoundError:
            lines = []

        for i, line in enumerate (lines):
            if line.startswith(self.username):
                parts = line.split()
                if len(parts) >= 2:
                    try: 
                        old_streak = int(parts[1])
                        if self.streak > old_streak:
                            lines[i] = formatted_line
                            updated = True
                    except ValueError:
                        lines[i] = formatted_line
                        updated = True 
                found = True 
                break
        
        if not found:
            lines.append(formatted_line)
            updated = True 

        if updated:
            with open("leaderboard.txt", "w") as file:
                file.writelines(lines)