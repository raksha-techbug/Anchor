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
  The user is upset because something already went wrong: they failed, made a mistake, were rejected, or feel bad about a past outcome.

- consistency
  The user is struggling to keep going, stay disciplined, stay consistent, or feels like giving up. The focus is persistence, not a past failure.

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