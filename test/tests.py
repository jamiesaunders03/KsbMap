from datetime import datetime, timedelta

from src.data.module_code import ModuleCode
from src.lookup import mod_code_to_ksbs, filter_se_skills


def test_faster_than_manually_doing_it():
    start = datetime.now()
    _ = mod_code_to_ksbs(ModuleCode.DC3MLN, filter=filter_se_skills)
    end = datetime.now()

    # I don't think this is a hard target to beat...
    assert end - start < timedelta(minutes=10)
