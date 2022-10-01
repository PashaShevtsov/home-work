import csv


class Candidate:
    def __init__(self, first_name, last_name, email, tech_stack, main_skill, main_skill_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.tech_stack = tech_stack
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def generate_candidates(cls, path_to_file):
        with open(path_to_file) as fp:
            reader = csv.DictReader(fp)
            candidates = []
            for entry in reader:
                data = dict(
                    first_name=entry['Full Name'].split()[0],
                    last_name=entry['Full Name'].split()[1],
                    email=entry['Email'],
                    tech_stack=entry['Technologies'].split('|'),
                    main_skill=entry['Main Skill'],
                    main_skill_grade=entry['Main Skill Grade']
                )
                candidates.append(cls(**data))
        return candidates


if __name__ == '__main__':
    # main()
    candidate_list = Candidate.from_csv(' candidates.csv')
    [print(x.first_name, x.tech_stack)for x in candidate_list]
