# Take input from the user
scores = input("Enter module scores (space-separated): ")

# Convert the input string to a list of integers
scores_list = list(map(int, scores.split()))

# Filter out modules with scores below 50
modules_to_debug = [score for score in scores_list if score < 50]

# Print the result based on the filtered scores
if modules_to_debug:
    print("Modules to debug:", " ".join(map(str, modules_to_debug)))
else:
    print("All modules are working fine!")
