class Job:
    def __init__(self, id, title, skills_ids):
        self.id = id
        self.title = title
        self.skills_ids = skills_ids

    # Adds skill to job required skills
    def add_skill(self, skill_id):
        if skill_id not in self.skills_ids:
            self.skills_ids.append(skill)

    # Removes skill from job required skills
    def remove_skill(self, skill_id):
        if skill_id in self.skills_ids:
            self.skills_ids.remove(skill_id)
