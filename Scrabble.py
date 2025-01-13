letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
           "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Create a dictionary mapping letters to points
letter_to_points = {letter: point for letter, point in zip(letters, points)}
letter_to_points[" "] = 0  # Add blank tile with 0 points

# Function to score a word
def score_word(word):
    point_total = 0
    for letter in word:
        point_total += letter_to_points.get(letter.upper(), 0)
    return point_total

# Test the function with the word "BROWNIE"
brownie_points = score_word("BROWNIE")
print(f"Brownie Points: {brownie_points}")

# Create a dictionary mapping players to words
player_to_words = {
    "player1": ["BLUE", "TENNIS", "EXIT"],
    "wordNerd": ["EARTH", "EYES", "MACHINE"],
    "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
    "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}

# Calculate points for each player
player_to_points = {}
for player, words in player_to_words.items():
    player_points = sum(score_word(word) for word in words)
    player_to_points[player] = player_points

# Print the standings
print("Player Standings:")
for player, points in player_to_points.items():
    print(f"{player}: {points} points")