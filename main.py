from db_mockup.candidates import candidates
from db_mockup.jobs import jobs
from utilities import candidate_utilities
from models.job import Job

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    current_candidates = candidate_utilities.create_candidate_list(candidates)
    for job in jobs:
        current_job = Job(job.get('id'), job.get('title'), job.get('skills'))
        matching_candidates = candidate_utilities.candidate_finder_by_skills(current_job, current_candidates)
        print('The best candidates for job number: ' + str(current_job.id) + ' - ' + current_job.title + ' position: ')
        print(matching_candidates)
c