# KSB MAP

## Summary
    This is an overview of the KSB Map CLI tool and how it can be used.
    The tool aims to speed up searching through the KSB list for monthly OTJ logs by looking up all relevant skills
    by module code to give an overview of what is expected to be covered.
    Hopefully this helps to remove some of the pain of OTJ logs :)

## Set Up
    There are no external dependencies used by this tool for the CLI, so it will run with just python installed
    on your machine. Python 3.9+ is required for the type hints syntax to work, but you can remove that and it
    will probably work on versions as old as 3.6.

    If you want to run the tests for whatever reason, pytest is required which can be installed by running
    >>> pip install requirements.txt
    In your terminal of choice.

## User Reference
    Invoke the CLI using python to get the CLI help pages up, there are examples in there for how to search 
    for module codes.

    >>> py cli.py

    INTRO
            Welcome to the Module Skill CLI
            You can use this to search for the relevant KSBs for each module
    
    ARGS
            -h|--help                         The help pages (this)
            -l|--list                         List all known module codes
            -m|--module=    [module code]     The module code to search. If not looking at the help pages or module
                                              list then this is a required argument
            -f|--filter=    [filter string]   Optional filter to only show either BA/SE skills, if this starts with
                                              a 's', doesn't show BA only skills. If it starts with a 'b', doesn't
                                              show SE only skills
    
    EXAMPLES
            python3 cli.py -m DC3IPR
                    Get all skills that should be displayed in the DC3IPR Module
    
            python3 cli.py -m DC2TPR --filter=se
                    Get all skills that a software engineer should demonstrate during the team project module
