
from dataclasses import dataclass
from ksb_group import KsbGroup
from learning_objective import LearningObjective


@dataclass
class Skill:
    code: str
    """Skill Code, e.g. S1"""

    group: KsbGroup
    """The KSB group this belongs to"""

    description: str
    """Description of the Skill"""

    learning_objectives: list[LearningObjective]
    """The relevant learning objectives"""

    def __hash__(self):
        return hash(self.code)

    def __eq__(self, other):
        return isinstance(other, Skill) and self.code == other.code
