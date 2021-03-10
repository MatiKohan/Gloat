class Candidate:
    def __init__(self, id, title, skills):
        self.id = id
        self.title = title
        self.skills = skills

    def add_skill(self, skill):
        self.skills.append(skill)

    def remove_skill(self, skill):
        self.skills.remove(skill)

    def change_title(self, title):
        self.title = title
