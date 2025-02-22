class Noun:
    def __init__(self, noun_singular, noun_plural, gender):
        self.noun_singular = noun_singular
        self.noun_plural = noun_plural
        self.gender = gender


class Pronoun:
    def __init__(self, pronoun, number, pronoun_type):
        self.pronoun = pronoun
        self.number = number
        self.pronoun_type = pronoun_type


class PersonalPronoun(Pronoun):
    def __init__(self, pronoun, number, pronoun_type, person, case):
        super().__init__(pronoun, number, pronoun_type)
        self.person = person
        self.case = case


class DemonstrativePronoun(Pronoun):
    def __init__(self, pronoun, number, pronoun_type, distance):
        super().__init__(pronoun, number, pronoun_type)
        self.distance = distance


class Verb:
    def __init__(self, base_form, present_first_person, present_second_person, present_third_person, past,
                 past_participle, progressive, type, category):
        self.base_form = base_form
        self.present_first_person = present_first_person
        self.present_second_person = present_second_person
        self.present_third_person = present_third_person
        self.past = past
        self.past_participle = past_participle
        self.progressive = progressive
        self.type = type
        self.category = category

    def get_future_tense_form(self):
        return f"will {self.base_form}"
