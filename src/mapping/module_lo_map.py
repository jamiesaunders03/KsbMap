
from ..data.module_code import ModuleCode
from ..data.learning_objective import LearningObjective

module_map: list[tuple[ModuleCode, LearningObjective]] = [
    (ModuleCode.DC1PRP, LearningObjective.LO4_1),
    (ModuleCode.DC1PRP, LearningObjective.LO4_6),
    (ModuleCode.DC1PRP, LearningObjective.LO4_7),

    (ModuleCode.DC1FTS, LearningObjective.LO4_1),
    (ModuleCode.DC1FTS, LearningObjective.LO4_2),
    (ModuleCode.DC1FTS, LearningObjective.LO4_4),
    (ModuleCode.DC1FTS, LearningObjective.LO4_5),
    (ModuleCode.DC1FTS, LearningObjective.LO4_6),
    (ModuleCode.DC1FTS, LearningObjective.LO4_7),

    (ModuleCode.DC1CSN, LearningObjective.LO4_3),
    (ModuleCode.DC1CSN, LearningObjective.LO4_5),

    (ModuleCode.DC1SDV, LearningObjective.LO4_1),
    (ModuleCode.DC1SDV, LearningObjective.LO4_2),
    (ModuleCode.DC1SDV, LearningObjective.LO4_4),
    (ModuleCode.DC1SDV, LearningObjective.LO4_5),

    (ModuleCode.DC1IAP, LearningObjective.LO4_2),
    (ModuleCode.DC1IAP, LearningObjective.LO4_4),
    (ModuleCode.DC1IAP, LearningObjective.LO4_5),

    (ModuleCode.BN1IBO, LearningObjective.LO4_1),
    (ModuleCode.BN1IBO, LearningObjective.LO4_4),
    (ModuleCode.BN1IBO, LearningObjective.LO4_5),

    (ModuleCode.DC2TPR, LearningObjective.LO5_2),
    (ModuleCode.DC2TPR, LearningObjective.LO5_3),
    (ModuleCode.DC2TPR, LearningObjective.LO5_5),
    (ModuleCode.DC2TPR, LearningObjective.LO5_6),
    (ModuleCode.DC2TPR, LearningObjective.LO5_7),
    (ModuleCode.DC2TPR, LearningObjective.LO5_8),

    (ModuleCode.DC2PSA, LearningObjective.LO5_2),

    (ModuleCode.DC2HCI, LearningObjective.LO5_2),
    (ModuleCode.DC2HCI, LearningObjective.LO5_3),
    (ModuleCode.DC2HCI, LearningObjective.LO5_5),
    (ModuleCode.DC2HCI, LearningObjective.LO5_7),
    (ModuleCode.DC2HCI, LearningObjective.LO5_8),

    (ModuleCode.DC2MCP, LearningObjective.LO5_4),

    (ModuleCode.DC3ADG, LearningObjective.LO5_3),
    (ModuleCode.DC3ADG, LearningObjective.LO5_5),
    (ModuleCode.DC3ADG, LearningObjective.LO5_6),

    (ModuleCode.DC2SEN, LearningObjective.LO5_5),
    (ModuleCode.DC2SEN, LearningObjective.LO5_6),
    (ModuleCode.DC2SEN, LearningObjective.LO5_7),
    (ModuleCode.DC2SEN, LearningObjective.LO5_8),

    (ModuleCode.DC2PLC, LearningObjective.LO5_6),
    (ModuleCode.DC2PLC, LearningObjective.LO5_7),
    (ModuleCode.DC2PLC, LearningObjective.LO5_8),

    (ModuleCode.BS203D, LearningObjective.LO5_1),
    (ModuleCode.BS203D, LearningObjective.LO5_4),

    (ModuleCode.BN210D, LearningObjective.LO5_1),
    (ModuleCode.BN210D, LearningObjective.LO5_3),
    (ModuleCode.BN210D, LearningObjective.LO5_4),

    (ModuleCode.DC2SAN, LearningObjective.LO5_3),
    (ModuleCode.DC2SAN, LearningObjective.LO5_5),
    (ModuleCode.DC2SAN, LearningObjective.LO5_6),
    (ModuleCode.DC2SAN, LearningObjective.LO5_8),

    (ModuleCode.BF202D, LearningObjective.LO5_1),
    (ModuleCode.BF202D, LearningObjective.LO5_4),

    (ModuleCode.DC3IPR, LearningObjective.LO6_2),
    (ModuleCode.DC3IPR, LearningObjective.LO6_3),
    (ModuleCode.DC3IPR, LearningObjective.LO6_5),
    (ModuleCode.DC3IPR, LearningObjective.LO6_6),

    (ModuleCode.DC3ISC, LearningObjective.LO6_1),
    (ModuleCode.DC3ISC, LearningObjective.LO6_6),
    (ModuleCode.DC3ISC, LearningObjective.LO6_7),

    (ModuleCode.DC3ISC, LearningObjective.LO6_2),
    (ModuleCode.DC3ISC, LearningObjective.LO6_3),
    (ModuleCode.DC3DMN, LearningObjective.LO6_6),

    (ModuleCode.DC3SPM, LearningObjective.LO6_1),
    (ModuleCode.DC3SPM, LearningObjective.LO6_2),
    (ModuleCode.DC3SPM, LearningObjective.LO6_3),
    (ModuleCode.DC3SPM, LearningObjective.LO6_4),
    (ModuleCode.DC3SPM, LearningObjective.LO6_6),
    (ModuleCode.DC3SPM, LearningObjective.LO6_7),

    (ModuleCode.DC3IDG, LearningObjective.LO6_2),
    (ModuleCode.DC3IDG, LearningObjective.LO6_6),

    (ModuleCode.BM305D, LearningObjective.LO6_4),
    (ModuleCode.BM305D, LearningObjective.LO6_7),

    (ModuleCode.DC3ECS, LearningObjective.LO6_4),
    (ModuleCode.DC3ECS, LearningObjective.LO6_5),
    (ModuleCode.DC3ECS, LearningObjective.LO6_6),
    (ModuleCode.DC3ECS, LearningObjective.LO6_7),

    (ModuleCode.DC3ADG, LearningObjective.LO6_1),
    (ModuleCode.DC3ADG, LearningObjective.LO6_3),
    (ModuleCode.DC3ADG, LearningObjective.LO6_4),

    (ModuleCode.LBM404, LearningObjective.LO6_2),
    (ModuleCode.LBM404, LearningObjective.LO6_4),

    (ModuleCode.DC3MLN, LearningObjective.LO6_2),
    (ModuleCode.DC3MLN, LearningObjective.LO6_3),
    (ModuleCode.DC3MLN, LearningObjective.LO6_5),
    (ModuleCode.DC3MLN, LearningObjective.LO6_6),

    (ModuleCode.DC3CIN, LearningObjective.LO6_2),
    (ModuleCode.DC3CIN, LearningObjective.LO6_3),
    (ModuleCode.DC3CIN, LearningObjective.LO6_5),
    (ModuleCode.DC3CIN, LearningObjective.LO6_6),

    (ModuleCode.DC3MDV, LearningObjective.LO6_1),
    (ModuleCode.DC3MDV, LearningObjective.LO6_2),
    (ModuleCode.DC3MDV, LearningObjective.LO6_6),

    (ModuleCode.DC3AWD, LearningObjective.LO6_2),
    (ModuleCode.DC3AWD, LearningObjective.LO6_3),
    (ModuleCode.DC3AWD, LearningObjective.LO6_5),
    (ModuleCode.DC3AWD, LearningObjective.LO6_6),

    (ModuleCode.BN301D, LearningObjective.LO6_4),
    (ModuleCode.BN301D, LearningObjective.LO6_7),

    (ModuleCode.BN303D, LearningObjective.LO6_2),
    (ModuleCode.BN303D, LearningObjective.LO6_4),
    (ModuleCode.BN303D, LearningObjective.LO6_7),
]
