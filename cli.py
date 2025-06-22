from src.lookup import mod_code_to_ksbs, filter_se_skills, filter_ba_skills
from src.data.module_code import ModuleCode


from itertools import islice
from typing import Iterable


def _get_cli_args(args: list[tuple[str, str]]) -> dict[str, object]:
    cli_args = dict(help=False, list=False, module="", filter="")
    for opt, arg in args:
        if opt in ("-m", "--module"):
            cli_args["module"] = arg
        elif opt in ("-f", "--filter"):
            cli_args["filter"] = arg
        elif opt in ("-h", "--help"):
            cli_args["help"] = True
        elif opt in ("-l", "--list"):
            cli_args["list"] = True

    return cli_args


def _help():
    print("INTRO")
    print("\tWelcome to the Module Skill CLI")
    print("\tYou can use this to search for the relevant KSBs for each module")
    print("")
    print("ARGS")
    print("\t-h|--help                         The help pages (this)")
    print("\t-l|--list                         List all known module codes")
    print("\t-m|--module=    [module code]     The module code to search. If not looking at the help pages or module ")
    print("\t                                  list then this is a required argument")
    print("\t-f|--filter=    [filter string]   Optional filter to only show either BA/SE skills, if this starts with ")
    print("\t                                  a 's', doesn't show BA only skills. If it starts with a 'b', doesn't")
    print("\t                                  show SE only skills")
    print("")
    print("EXAMPLES")
    print("\tpython3 cli.py -m DC3IPR")
    print("\t\tGet all skills that should be displayed in the DC3IPR Module")
    print("")
    print("\tpython3 cli.py -m DC2TPR --filter=se")
    print("\t\tGet all skills that a software engineer should demonstrate during the team project module")


def _list_all_modules():
    print("MODULE LIST:")
    for mod in ModuleCode:
        print(f"    {mod.name}")


def _search(mod_code: str, filter: str):
    if mod_code == "":
        raise ValueError("Please specify a module code")

    try:
        mod = ModuleCode[mod_code.upper()]
    except KeyError:
        raise ValueError(f"Unknown module code: {cli_args['module']}")

    filter_func = None
    if filter.lower().startswith("s"):
        filter_func = filter_se_skills
    elif filter.startswith("b"):
        filter_func = filter_ba_skills
    elif filter != "":
        print(f"Unknown filter modifier: {filter}, no filtering taking place")

    skills = mod_code_to_ksbs(mod, filter=filter_func)

    print("Code    | Group                     | Description")
    print("        |                           |")

    line_wrap = '\n' + ' ' * 38
    for skill in skills:
        desc: str = line_wrap.join(_batched(skill.description, 140))
        print(f"{skill.code:<8}| {skill.group.name:<25} | {desc}")


def _batched(string: str, max_len: int) -> list[str]:
    """Split string into max length lines"""
    words: list[str] = string.split(" ")
    lines: list[str] = []

    line = ""
    for word in words:
        if len(word) + len(line) > max_len and line != "":
            lines.append(line)
            line = word
        else:
            line += f"{word} "

    if len(line) > 0:
        lines.append(line)
    return lines

if __name__ == '__main__':
    import getopt
    import sys

    short_ops = "m:f:hl"
    long_ops = ["module=", "filter=", "help", "list"]

    optlist, _ = getopt.getopt(sys.argv[1:], short_ops, long_ops)
    cli_args = _get_cli_args(optlist)

    if len(optlist) == 0 or cli_args["help"]:
        _help()
    elif cli_args["list"]:
        _list_all_modules()
    else:
        _search(str(cli_args["module"]), str(cli_args["filter"]))
