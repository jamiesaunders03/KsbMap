
import re
from typing import Callable, Optional

from .data.module_code import ModuleCode
from .data.skill import Skill
from .mapping.lo_ksb_map import skills
from .mapping.module_lo_map import module_map


def mod_code_to_ksbs(mod_code: ModuleCode, filter: Optional[Callable[[list[Skill]], list[Skill]]] = None) -> list[Skill]:
    """
    Gets all the skills associated with a given module code.
    :param mod_code: The module code to get skills for.
    :param filter: Optional function - filters items in response
    :return: A list of all skills associated with a given module code.
    """

    los = [lo[1] for lo in module_map if lo[0] == mod_code]
    mod_skills = [s[0] for s in skills if s[1] in los]
    mod_skills = _get_unique(mod_skills)

    if filter is not None:
        mod_skills = filter(mod_skills)

    return mod_skills


def get_all_ksbs(filter: Optional[Callable[[list[Skill]], list[Skill]]] = None) -> list[Skill]:
    los = [lo[1] for lo in module_map]
    print(len(los))
    mod_skills = [s[0] for s in skills if s[1] in los]
    mod_skills = _get_unique(mod_skills)

    if filter is not None:
        mod_skills = filter(mod_skills)

    return mod_skills


def filter_se_skills(skill_list: list[Skill]) -> list[Skill]:
    """
    Returns a list of all skills passed in, except for ones that are for Business Analysts
    """
    return [s for s in skill_list if not s.group.name.startswith('BA')]


def filter_ba_skills(skill_list: list[Skill]) -> list[Skill]:
    """
    Returns a list of all skills passed in, except for ones that are for Software Engineers
    """
    return [s for s in skill_list if not s.group.name.startswith('SE')]


def _get_unique(skill_list: list[Skill]) -> list[Skill]:
    seen = set()
    return [s for s in skill_list if not (s in seen or seen.add(s))]
