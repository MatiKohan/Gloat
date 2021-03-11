from models.candidate import Candidate  # Candidates mockup


# Gets an array of candidates and returns an array of candidate objects
def create_candidates_list(candidates_array):
    candidates_list = []
    for candidate in candidates_array:
        candidates_list.append(Candidate(candidate.get('id'), candidate.get('title'), candidate.get('skills_ids')))
    return candidates_list


# Gets a job object, a list of candidate objects and a limit n, Returns a list of the best n matching candidates for the job sorted by title and num of skills
def candidate_finder(job, candidates, limit=-1):
    candidates_for_job = []

    for candidate in candidates:
        title_match = job.title == candidate.title
        skills_match = 0
        for skill in job.skills_ids:
            if skill in candidate.skills_ids:
                skills_match += 1
        if title_match or skills_match > 0:
            candidates_for_job.append(
                {'candidate_id': candidate.id, 'title_match': title_match, 'number_of_skills_match': skills_match})

    candidates_for_job.sort(key=lambda x: (x.get('title_match'), x.get('number_of_skills_match')), reverse=True)
    return candidates_for_job[:limit]
