from models.candidate import Candidate


def create_candidate_list(candidates_array):
    candidates_list = []
    for candidate in candidates_array:
        candidates_list.append(Candidate(candidate.get('id'), candidate.get('title'), candidate.get('skills')))
    return candidates_list


def candidate_finder_by_title(job, candidates):
    candidates_for_job = []
    for candidate in candidates:
        if candidate.title == job.title:
            candidates_for_job.append(candidate)
    return candidates_for_job


def candidate_finder_by_skills(job, candidates, with_title=True, minimum_skills=2):
    candidates_for_job = []

    if with_title:
        candidates_list = candidate_finder_by_title(job, candidates)
    else:
        candidates_list = candidates

    for candidate in candidates_list:
        skills_match = 0
        for skill in job.skills:
            if skill in candidate.skills:
                skills_match += 1

        if skills_match > 0:
            candidates_for_job.append({'candidate_id': candidate.id, 'number_of_skills_match': skills_match})

    candidates_for_job.sort(key=lambda x: x.get('number_of_skills_match'), reverse=True)
    return candidates_for_job


def candidate_finder(job, candidates):
    print('1')
