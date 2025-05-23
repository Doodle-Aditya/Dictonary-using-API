import requests

def get_definition(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Word not found. Try another word.")
        return

    data = response.json()[0]
    print(f"\n Word: {data['word']}")

    meaning = data['meanings'][0]
    print(f" Part of Speech: {meaning['partOfSpeech']}")
    print(f" Definition: {meaning['definitions'][0]['definition']}")

    if 'example' in meaning['definitions'][0]:
        print(f" Example: {meaning['definitions'][0]['example']}")


# --- Run it ---
word = input("Enter a word: ")
get_definition(word)
