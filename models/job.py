class Job:
    def __init__(self, id, title, skills):
        self.id = id
        self.title = title
        self.skills = skills

    def add_skill(self, skill):
        if skill not in self.skill:
            self.skills.append(skill)

    def remove_skill(self, skill):
        if skill in self.skills:
            self.skills.remove(skill)
