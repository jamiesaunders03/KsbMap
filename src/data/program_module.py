
from dataclasses import dataclass
from module_code import ModuleCode
from learning_objective import LearningObjective


@dataclass
class ProgramModule:
    module_code: ModuleCode
    """The code for this module"""

    learning_objectives: list[LearningObjective]
    """The learning objectives relating to this module"""

    def __hash__(self):
        return hash(self.module_code)

    def __eq__(self, other):
        return isinstance(other, ProgramModule) and self.module_code == other.code

