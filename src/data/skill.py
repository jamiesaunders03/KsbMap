
from dataclasses import dataclass
from ksb_group import KsbGroup


@dataclass
class Skill:
    code: str
    """Skill Code, e.g. S1"""

    group: KsbGroup
    """The KSB group this belongs to"""

    description: str
    """Description of the Skill"""

    def __hash__(self):
        return hash(self.code)

    def __eq__(self, other):
        return isinstance(other, Skill) and self.code == other.code
