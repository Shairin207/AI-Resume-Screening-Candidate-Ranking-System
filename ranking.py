from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_score(resume_text, job_description):

    documents = [resume_text, job_description]

    cv = CountVectorizer()

    matrix = cv.fit_transform(documents)

    similarity = cosine_similarity(matrix)[0][1]

    return round(similarity * 100, 2)


def skill_gap(candidate_skills, required_skills):

    missing = []

    for skill in required_skills:

        if skill.lower() not in [
                s.lower()
                for s in candidate_skills]:

            missing.append(skill)

    return missing