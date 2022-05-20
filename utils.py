import json
from pprint import pprint

from config.config import PATH


def load_candidates_from_json(path=PATH):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_all_candidates():
    data = load_candidates_from_json()
    return data


def get_candidate_pk(pk):
    candidates = get_all_candidates()
    for candidate in candidates:
        if candidate['id'] == pk:
            return candidate


def get_candidates_by_name(name):
    candidates = get_all_candidates()
    candidates_name = []
    for candidate in candidates:
        if name.lower() in candidate['name'].lower():
            candidates_name.append(candidate)
    return candidates_name


def get_candidates_by_skill(skill):
    candidates = get_all_candidates()
    candidate_skill = []
    for candidate in candidates:
        if skill.lower() in candidate['skills']:
            candidate_skill.append(candidate)
    return candidate_skill


# pprint(get_all_candidates())
