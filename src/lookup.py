
from .data.module_code import ModuleCode
from .data.skill import Skill
from .mapping.lo_ksb_map import skills
from .mapping.module_lo_map import module_map


def mod_code_to_ksbs(mod_code: str) -> list[Skill]:
    mod = ModuleCode(0)
    try:
        mod = ModuleCode[mod_code.upper()]
    except KeyError:
        return []

    los = [lo[1] for lo in module_map if lo[0] == mod]
    mod_skills = [s[0] for s in skills if s[1] in los]

    return mod_skills
