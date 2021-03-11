from db_mockup.candidates import candidates  # Candidates mockup
from db_mockup.jobs import jobs              # Jobs mockup
from utilities import candidate_utilities    # Candidates utilities
from models.job import Job                   # Job model

# Specify the maximum number of candidates to be returned for a job. (all = -1)
max_candidates = 5

# Main function - creates a list of candidates objects, loops over jobs and calls candidate_finder for each job.
if __name__ == '__main__':
    current_candidates = candidate_utilities.create_candidates_list(candidates)
    for job in jobs:

        current_job = Job(job.get('id'), job.get('title'), job.get('skills_ids'))
        matching_candidates = candidate_utilities.candidate_finder(current_job, current_candidates, max_candidates)  # Limit the number of candidates for position by adding the limit here

        if matching_candidates:
            print('The best candidates for job number: ' + str(
                current_job.id) + ' - ' + current_job.title + ' position: \n' + str(matching_candidates) + '\n')
        else:
            print('The are not candidates for job number: ' + str(
                current_job.id) + ' - ' + current_job.title + ' position. \n')
