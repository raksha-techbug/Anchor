import json
import random

# Ask the user how they are feeling
feeling = input("What are you feeling today?\n> ")

# Load the proofs
with open("proofs.json", "r") as file:
    data = json.load(file)

    # Decide which category to use
if "enough" in feeling.lower():
    category = "not_enough"

elif "english" in feeling.lower() or "communicat" in feeling.lower():
    category = "communication"

elif "learn" in feeling.lower() or "study" in feeling.lower():
    category = "learning"

else:
    category = None

# Pick 3 random proofs
# Temporary: always use the "not_enough" category
if category is None:
    print("\nI'm here whenever you need a reality check.")
else:
    selected = random.sample(
        data["proofs"][category],
        min(3, len(data["proofs"][category]))
    )

    print("\n")
    print(data["intro"])
    print(data["bridge"] + "\n")

    for proof in selected:
        print("• " + proof)

    print("\n" + data["ending"])
