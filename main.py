from igbo import igbo_dict
from yoruba import yoruba_dict
from hausa import hausa_dict
from swahili import swahili_dict
from fulani import fulani_dict

languages = {
    "1": {"name": "igbo", "dict": igbo_dict},
    "2": {"name": "yoruba", "dict": yoruba_dict},
    "3": {"name": "hausa", "dict": hausa_dict},
    "4": {"name": "swahili", "dict": swahili_dict},
    "5": {"name": "fulani", "dict": fulani_dict},
}

def translate_word(language, word):
    if language in languages:
        lang_dict = languages[language]["dict"]
        return lang_dict.get(word, "Word not found")
    return "Language not found"

def main():
    print("Choose a language:")
    for key, value in languages.items():
        print(f"{key}. {value['name']}")
   
    language = input("Enter language number: ")
    word = input("Enter English word: ").lower()
   
    print(translate_word(language, word))

if __name__ == "__main__":
    main()