import random

# Data
TENSES = ["present", "past", "future"]
CATEGORIES = ["simple", "continuous", "perfect", "perfect continuous"]
PRONOUNS = ["I", "you", "he", "she", "it", "we", "you", "they"]
AUXILIARIES = [
    "___", "do", "does", "did", "will", "am", "is", "are", "was", "were",
    "will be", "have", "has", "had", "will have", "have been", "has been",
    "had been", "will have been"
]
REGULAR_VERBS = {
    "present": ["wash", "love", "work", "jump", "call"],
    "present 3ps": ["washes", "loves", "works", "jumps", "calls"],
    "past/perfect": ["washed", "loved", "worked", "jumped", "called"],
    "continuous": ["washing", "loving", "working", "jumping", "calling"]
}
SINGULAR_DEMONSTRATIVES = ["this", "that"]
PLURAL_DEMONSTRATIVES = ["these", "those"]
SINGULAR_NOUNS = ["dog", "cat", "boy", "girl", "man", "woman"]
PLURAL_NOUNS = ["dogs", "cats", "boys", "girls", "men", "women"]

def define_grammatical_tense():
    """
    Define a random grammatical tense and category.

    Returns:
        tuple: A tuple containing the tense and category.
    """
    tense = random.choice(TENSES)
    category = random.choice(CATEGORIES)
    return tense, category

def define_subject_type(subject):
    """
    Define the type of subject based on the pronoun.

    Args:
        subject (str): The subject pronoun.

    Returns:
        str: The type of subject ('3ps' or 'not3ps').
    """
    if subject in ["he", "she", "it"]:
        subject_type = "3ps"
    else:
        subject_type = "not3ps"
    return subject_type

def define_auxiliary(tense, category, subject, subject_type):
    """
    Define the auxiliary verb based on tense, category, subject, and subject type.

    Args:
        tense (str): The grammatical tense.
        category (str): The grammatical category.
        subject (str): The subject pronoun.
        subject_type (str): The type of subject.

    Returns:
        str: The auxiliary verb.
    """
    if tense in ["present", "past"] and category in ["simple"]:
        aux = AUXILIARIES[0]
    elif tense in ["future"] and category in ["simple"]:
        aux = AUXILIARIES[4]
    elif tense in ["present"] and category in ["continuous"] and subject == "I":
        aux = AUXILIARIES[5]
    elif tense in ["present"] and category in ["continuous"] and subject_type == "3ps":
        aux = AUXILIARIES[6]
    elif tense in ["present"] and category in ["continuous"] and subject_type == "not3ps":
        aux = AUXILIARIES[7]
    elif tense in ["past"] and category in ["continuous"] and subject in ["I", "he", "she", "it"]:
        aux = AUXILIARIES[8]
    elif tense in ["past"] and category in ["continuous"] and subject in ["you", "we", "they"]:
        aux = AUXILIARIES[9]
    elif tense in ["future"] and category in ["continuous"]:
        aux = AUXILIARIES[10]
    elif tense in ["present"] and category in ["perfect"] and subject_type == "not3ps":
        aux = AUXILIARIES[11]
    elif tense in ["present"] and category in ["perfect"] and subject_type == "3ps":
        aux = AUXILIARIES[12]
    elif tense in ["past"] and category in ["perfect"]:
        aux = AUXILIARIES[13]
    elif tense in ["future"] and category in ["perfect"]:
        aux = AUXILIARIES[14]
    elif tense in ["present"] and category in ["perfect continuous"] and subject_type == "not3ps":
        aux = AUXILIARIES[15]
    elif tense in ["present"] and category in ["perfect continuous"] and subject_type == "3ps":
        aux = AUXILIARIES[16]
    elif tense in ["past"] and category in ["perfect continuous"]:
        aux = AUXILIARIES[17]
    elif tense in ["future"] and category in ["perfect continuous"]:
        aux = AUXILIARIES[18]
    return aux

def choose_regular_verb(tense, category, subject_type):
    """
    Choose a regular verb based on tense, category, and subject type.

    Args:
        tense (str): The grammatical tense.
        category (str): The grammatical category.
        subject_type (str): The type of subject.

    Returns:
        str: The chosen verb.
    """
    if tense in ["present", "future"] and category in ["simple"] and subject_type == "not3ps":
        verb = random.choice(REGULAR_VERBS["present"])
    elif tense in ["present"] and category in ["simple"] and subject_type == "3ps":
        verb = random.choice(REGULAR_VERBS["present 3ps"])
    elif tense in ["future"] and category in ["simple"] and subject_type == "3ps":
        verb = random.choice(REGULAR_VERBS["present"])
    elif tense in ["past"] and category in ["simple"]:
        verb = random.choice(REGULAR_VERBS["past/perfect"])
    elif category in ["perfect"]:
        verb = random.choice(REGULAR_VERBS["past/perfect"])
    elif category in ["continuous", "perfect continuous"]:
        verb = random.choice(REGULAR_VERBS["continuous"])
    return verb

def define_demonstrative():
    """
    Define a random demonstrative.

    Returns:
        str: The chosen demonstrative.
    """
    plural_or_singular = random.choice([1, 2])
    if plural_or_singular == 1:
        demonstrative = random.choice(SINGULAR_DEMONSTRATIVES)
    else:
        demonstrative = random.choice(PLURAL_DEMONSTRATIVES)
    return demonstrative

def define_noun(demonstrative):
    """
    Define a noun based on the demonstrative.

    Args:
        demonstrative (str): The demonstrative.

    Returns:
        str: The chosen noun.
    """
    if demonstrative in ["this", "that"]:
        noun = random.choice(SINGULAR_NOUNS)
    elif demonstrative in ["these", "those"]:
        noun = random.choice(PLURAL_NOUNS)
    return noun

def main():
    """
    Main function to generate and print a random phrase.
    """
    tense, category = define_grammatical_tense()
    subject = random.choice(PRONOUNS)
    subject_type = define_subject_type(subject)
    auxiliary = define_auxiliary(tense, category, subject, subject_type)
    verb = choose_regular_verb(tense, category, subject_type)
    demonstrative = define_demonstrative()
    noun = define_noun(demonstrative)

    sentence = f"{subject} {auxiliary} {verb} {demonstrative} {noun}"
    print(f"Sentence: {sentence}")
    print(f"Metadata: Subject: {subject}, Subject Type: {subject_type}, Tense: {tense}, Category: {category}, Auxiliary: {auxiliary}, Verb: {verb}, Demonstrative: {demonstrative}, Noun: {noun}")

if __name__ == "__main__":
    main()
