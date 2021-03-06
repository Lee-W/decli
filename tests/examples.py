import argparse
import textwrap
from decli import cli


def main_example():
    """https://docs.python.org/3/library/argparse.html#example"""
    data = {
        "description": "Process some integers.",
        "arguments": [
            {
                "name": "integers",
                "metavar": "N",
                "type": int,
                "nargs": "+",
                "help": "an integer for the accumulator",
            },
            {
                "name": "--sum",
                "dest": "accumulate",
                "action": "store_const",
                "const": sum,
                "default": max,
                "help": "sum the integers (default: find the max)",
            },
        ],
    }
    parser = cli(data)
    return parser


def complete_example():
    data = {
        "prog": "cz",
        "formatter_class": argparse.RawDescriptionHelpFormatter,
        "description": "The software does this and that",
        "epilog": "This is the epilooogpoe  ",
        "arguments": [
            {
                "name": "--debug",
                "action": "store_true",
                "default": False,
                "help": "use debug mode",
            },
            {
                "name": ["-v", "--version"],
                "action": "store_true",
                "default": False,
                "help": "get the installed version",
                "group": "ops",
            },
            {"name": "--save", "group": "ops"},
        ],
        "subcommands": {
            "title": "main",
            "description": "main commands",
            "commands": [
                {
                    "name": "all",
                    "help": "check every values is true",
                    "func": all,
                },
                {
                    "name": ["sum", "s"],
                    "help": "new project",
                    "func": sum,
                    "arguments": [
                        {
                            "name": "integers",
                            "metavar": "N",
                            "type": int,
                            "nargs": "+",
                            "help": "an integer for the accumulator",
                        },
                        {"name": "--name", "nargs": "?"},
                    ],
                },
            ],
        },
    }
    parser = cli(data)
    return parser


def name_or_flags():
    """https://docs.python.org/3/library/argparse.html#name-or-flags"""
    data = {
        "prog": "sti",
        "arguments": [{"name": ["-f", "--foo"]}, {"name": "bar"}],
    }
    return data


def compose_clis_using_parents():
    """
    Sometimes, several cli share a common set of arguments.
    Rather than repeating the definitions of these arguments,
    one or more parent clis with all the shared arguments can be passed
    to parents= argument to cli.

    https://docs.python.org/3/library/argparse.html#parents
    """
    parent_foo_data = {
        "add_help": False,
        "arguments": [{"name": "--foo-parent", "type": int}],
    }
    parent_bar_data = {
        "add_help": False,
        "arguments": [{"name": "--bar-parent", "type": int}],
    }
    parent_foo_cli = cli(parent_foo_data)
    parent_bar_cli = cli(parent_bar_data)

    parents = [parent_foo_cli, parent_bar_cli]
    return parents


def using_formatter_class():
    """https://docs.python.org/3/library/argparse.html#formatter-class"""
    data = {
        "prog": "PROG",
        "formatter_class": argparse.RawDescriptionHelpFormatter,
        "description": textwrap.dedent(
            """\
            Please do not mess up this text!
            --------------------------------
                I have indented it
                exactly the way
                I want it
            """
        ),
    }
    return data


def prefix_chars():
    data = {
        "prog": "PROG",
        "prefix_chars": "+",
        "arguments": [{"name": ["+f", "++foo"]}, {"name": "++bar"}],
    }
    return data


def grouping_arguments():
    data = {
        "prog": "mycli",
        "arguments": [
            {
                "name": "--new",
                "help": "This does not belong to a group but its a long help",
            },
            {
                "name": "--init",
                "help": "This does not belong to a group but its a long help",
            },
            {
                "name": "--run",
                "group": "app",
                "help": "This does not belong to a group",
            },
            {
                "name": "--build",
                "group": "app",
                "help": "This does not belong to a group",
            },
            {
                "name": ["--install", "--add"],
                "group": "package",
                "metavar": "package_name",
                "nargs": "+",
                "help": "This belongs to a group",
            },
            {
                "name": "--remove",
                "group": "package",
                "help": "This belongs to a group",
            },
            {
                "name": "--why",
                "group": "package",
                "help": "This belongs to a group",
            },
        ],
    }
    return data


def exclusive_group():
    data = {
        "prog": "app",
        "arguments": [
            {"name": "--install", "exclusive_group": "ops"},
            {"name": "--purge", "exclusive_group": "ops"},
        ],
    }
    return data
