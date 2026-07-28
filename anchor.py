from brain import classify_emotion
import json
import random

def main():
    feeling = input("What are you feeling today?\n> ")

    with open("proofs.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    with open("responses.json", "r", encoding="utf-8") as file:
        responses = json.load(file)

    feeling = feeling.lower()
    category = classify_emotion(feeling)

    if category not in data["proofs"]:
        category = None

    if category is None:
        print("\nI'm here whenever you need a reality check.")
        return

    selected = random.sample(
        data["proofs"][category],
        min(3, len(data["proofs"][category]))
    )

    print()

    print(responses.get(category, data["intro"]))
    print(data["bridge"])
    print()

    for proof in selected:
        print("• " + proof)

    print("\n" + data["ending"])


if __name__ == "__main__":
    main()