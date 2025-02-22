import csv
import os
from parts_of_speech import Noun, Verb, PersonalPronoun, DemonstrativePronoun


def read_csv(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} does not exist.")
        return []
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            return [row for row in reader]
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return []


class PartsOfSpeech:
    def __init__(self, personal_pronouns, demonstrative_pronouns, verbs, nouns):
        self.personal_pronouns = personal_pronouns
        self.demonstrative_pronouns = demonstrative_pronouns
        self.verbs = verbs
        self.nouns = nouns

    @staticmethod
    def load_data():
        base_path = os.path.dirname(__file__)

        try:
            pronouns_data = read_csv(os.path.join(base_path, 'data/pronouns.csv'))
            personal_pronouns = [
                PersonalPronoun(p["pronoun"], p["number"], p["pronoun_type"], p["person"], p["case"])
                for p in pronouns_data if p['pronoun_type'] == 'personal'
            ]
            demonstrative_pronouns = [
                DemonstrativePronoun(p["pronoun"], p["number"], p["pronoun_type"], p["distance"])
                for p in pronouns_data if p['pronoun_type'] == 'demonstrative'
            ]
        except KeyError as e:
            print(f"Error processing pronouns data: Missing key {e}")
            personal_pronouns = []
            demonstrative_pronouns = []

        try:
            verbs = [Verb(**v) for v in read_csv(os.path.join(base_path, 'data/verbs.csv'))]
        except KeyError as e:
            print(f"Error processing verbs data: Missing key {e}")
            verbs = []

        try:
            nouns = [Noun(**n) for n in read_csv(os.path.join(base_path, 'data/nouns.csv'))]
        except KeyError as e:
            print(f"Error processing nouns data: Missing key {e}")
            nouns = []

        return PartsOfSpeech(personal_pronouns, demonstrative_pronouns, verbs, nouns)
