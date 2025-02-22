import random
from data_loader import PartsOfSpeech

# Examples of sentences per tense denomination
# Simple present: I eat pizza
# Simple past: I ate pizza
# Simple future: I will eat pizza
# Present progressive: I am eating pizza
# Past progressive: I was eating pizza
# Future progressive: I will be eating pizza
# Present perfect: I have eaten pizza
# Past perfect: I had eaten pizza
# Future perfect: I will have eaten pizza
TENSE_DENOMINATIONS = ["simple_present", "simple_past", "simple_future",
                       "present_progressive", "past_progressive", "future_progressive",
                       "present_perfect", "past_perfect", "future_perfect",
                       "present_perfect_progressive", "past_perfect_progressive", "future_perfect_progressive"]

PERSONS = ["first", "second", "third"]

NUMBER = ["singular", "plural"]


def select_personal_pronoun_by_person_and_number(pronouns, person, number):
    return [p for p in pronouns if p.person == person and p.number == number]


def select_non_auxiliary_verbs(verbs):
    return [verb for verb in verbs if verb.type != "auxiliary"]


def needs_auxiliary_verbs(tense):
    return "simple" not in tense


def get_demonstrative_pronoun_by_number_and_random_distance(demonstrative_pronouns, number):
    return random.choice([d for d in demonstrative_pronouns if d.number == number])


def select_correct_verb_form(verb, tense, person, number):
    if "progressive" in tense:
        return verb.progressive
    if "perfect" in tense:
        return verb.past_participle
    if "future" in tense:
        return verb.get_future_tense_form()
    if tense == "simple_present":
        if number == "singular":
            return verb.present_first_person if person == "first" else verb.present_second_person if person == "second" else verb.present_third_person
        else:
            return verb.present_first_person if person == "first" else verb.present_second_person if person == "second" else verb.present_third_person
    if tense == "simple_past":
        return verb.past

    return verb.base_form


def get_auxiliary_verbs(tense, person, number):
    if tense == "simple_present":
        if person == "first" or person == "second":
            return "do"
        elif person == "third":
            return "does"
    elif tense == "simple_past":
        return "did"
    elif tense == "simple_future":
        return "will"
    elif tense == "present_progressive":
        if number == "singular":
            return "am" if person == "first" else "is" if person == "third" else "are"
        else:
            return "are"
    elif tense == "past_progressive":
        if number == "singular":
            return "was" if person == "first" or person == "third" else "were"
        else:
            return "were"
    elif tense == "future_progressive":
        return "will be"
    elif tense == "present_perfect":
        return "have" if person == "first" or person == "second" else "has"
    elif tense == "past_perfect":
        return "had"
    elif tense == "future_perfect":
        return "will have"
    elif tense == "present_perfect_progressive":
        return "have been" if person == "first" or person == "second" else "has been"
    elif tense == "past_perfect_progressive":
        return "had been"
    elif tense == "future_perfect_progressive":
        return "will have been"
    else:
        return ""


class Sentence:
    def __init__(self, tense, person):
        self.tense = tense
        self.subject_type = person


class SimpleSentence(Sentence):
    def __init__(self, tense, person, subject, verb, sentence_object, object_number, demonstrative_pronouns):
        super().__init__(tense, person)
        self.subject = subject
        self.verb = verb
        self.object = sentence_object
        self.object_number = object_number
        self.demonstrative_pronouns = demonstrative_pronouns

        self.is_progressive = "progressive" in tense

    def __str__(self):
        demostrative_pronouns = get_demonstrative_pronoun_by_number_and_random_distance(self.demonstrative_pronouns,
                                                                                        self.object_number)
        obj = self.object.noun_singular if self.object_number == "singular" else self.object.noun_plural

        verb = select_correct_verb_form(self.verb, self.tense, self.subject_type, self.object_number)

        if needs_auxiliary_verbs(self.tense):
            return f"{self.subject.pronoun} {get_auxiliary_verbs(self.tense, self.subject_type, self.object_number)} {verb} {demostrative_pronouns.pronoun} {obj}"

        return f"{self.subject.pronoun} {verb} {demostrative_pronouns.pronoun} {obj}"

    def print_metadata(self):
        metadata = {
            "TENSE": self.tense,
            "PERSON": self.subject_type,
            "SUBJECT": self.subject.pronoun,
            "VERB": self.verb.base_form,
            "OBJECT": self.object.noun_singular if self.object_number == "singular" else self.object.noun_plural,
            "NUMBER": self.object_number
        }

        print(f"Metadata: {metadata}")


def main():
    parts_of_speech = PartsOfSpeech.load_data()

    if not parts_of_speech.personal_pronouns:
        print("Error: No personal pronouns loaded.")
        return
    if not parts_of_speech.verbs:
        print("Error: No verbs loaded.")
        return
    if not parts_of_speech.nouns:
        print("Error: No nouns loaded.")
        return
    if not parts_of_speech.demonstrative_pronouns:
        print("Error: No demonstrative pronouns loaded.")
        return

    tense = random.choice(TENSE_DENOMINATIONS)
    person = random.choice(PERSONS)
    object_number = random.choice(NUMBER)

    subject = random.choice(
        select_personal_pronoun_by_person_and_number(parts_of_speech.personal_pronouns, person, object_number))
    verb = random.choice(select_non_auxiliary_verbs(parts_of_speech.verbs))
    noun = random.choice(parts_of_speech.nouns)

    sentence = SimpleSentence(tense, person, subject, verb, noun, object_number, parts_of_speech.demonstrative_pronouns)

    print(f"Sentence: {sentence}")
    sentence.print_metadata()


if __name__ == "__main__":
    main()
