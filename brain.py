import ollama


def classify_emotion(feeling):
    prompt = f"""
You are the emotion classifier for an AI assistant called Anchor.

Your job is to identify the SINGLE PRIMARY emotional struggle.

Categories:

- not_enough
  The user feels inadequate, not good enough, not worthy, incapable, insecure about themselves, or lacks confidence.

- communication
  The user is struggling with speaking, writing, English, expressing thoughts, or communicating.

- learning
  The user doubts their ability to learn, improve, study, or understand something.

- failure
  The user is upset because of a mistake, failure, rejection, or poor performance.

- comparison
  The user believes others are ahead of them or is comparing themselves to other people.

- others_doubt_me
  The user feels discouraged because other people don't believe in them, their dreams, or their abilities.

Reply with ONLY the category name.

User:
"{feeling}"
"""

    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    print("Category:", response["message"]["content"].strip())

    return response["message"]["content"].strip()