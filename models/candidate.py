class Candidate:
    def __init__(self, id, title, skills_ids):
        self.id = id
        self.title = title
        self.skills_ids = skills_ids

    # Adds skill to candidate skills
    def add_skill(self, skill_id):
        if skill_id not in self.skills_ids:
            self.skills_ids.append(skill_id)

    # Removes skill from candidate skills
    def remove_skill(self, skill_id):
        if skill_id in self.skills_ids:
            self.skills_ids.remove(skill_id)

    # Changes candidate title
    def change_title(self, title):
        self.title = title
