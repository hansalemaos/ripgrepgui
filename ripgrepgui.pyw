from hackyargparser import add_sysargv
import os
from tkinter import *
import pandas as pd
from pandastable import Table
from rushex import FullBore
from shellextools import (
    format_folder_drive_path_backslash,
    add_multi_commands_to_drive_and_folder, get_my_icon, get_monitors_resolution,get_filepath
)
import sys

from tkinteruserinput import get_user_input
class TestApp(Frame):
        def __init__(self,df, parent=None):
            self.parent = parent
            Frame.__init__(self)
            self.main = self.master
            self.resolution = get_monitors_resolution()[0]
            self.monitor_w = self.resolution['width']
            self.monitor_h = self.resolution['height']
            self.main.geometry(f'{self.monitor_w-100 }x{self.monitor_h-100}')
            self.main.title('RipGrep results')
            f = Frame(self.main)
            f.pack(fill=BOTH,expand=1)
            if 'aa_replacement' in df:
                df = df.drop(columns='aa_replacement')
            if 'aa_newfilename' in df:
                df = df.drop(columns='aa_newfilename')
            self.table = pt = Table(f, dataframe=df.copy(),
                                    showtoolbar=True, showstatusbar=True)
            self.table.autoResizeColumns()
            pt.show()

myicon = get_my_icon("regexlogo.ico")
@add_sysargv
def main(path: str = "", action: str = ""):
    """
    This function takes in two optional parameters: path and action. It formats the path to ensure it has a backslash,
    gets the filepath for rg.exe, creates a FullBore object with the ripgrep path, and initializes an empty DataFrame.
    It then prompts the user to input regular expressions and file types, validates the input, and stores them in
    regular_expressions and allowed_extensions respectively. Depending on the value of action, it calls the find_all_in_folders
    method of the FullBore object with the appropriate parameters and stores the result in dfa. Finally, it creates a TestApp
    object with dfa and returns it.

    :param path: A string representing the path to search for files in. Defaults to an empty string.
    :param action: A string representing the action to perform. Defaults to an empty string.
    :return: A TestApp object containing the results of the search.
    """
    path = format_folder_drive_path_backslash(path)
    ripgreppath = get_filepath(r"rg.exe")
    monsterregex = FullBore(ripgrepexe=ripgreppath)
    dfa=pd.DataFrame()
    user_input = get_user_input(
        linesinputbox=20,
        size="900x450",
        title="Regular Expressions",
        textabovebox="Regular expressions - one per line - no whitespace at the end",
        submitbutton="Submit",
        regexcheck=r".*",
        showerror=("Error", "This is not a regular expression!"),
        showinfo=None,
        showwarning=None,
        icon=myicon,
    )
    regular_expressions = [g for x in user_input.splitlines() if (g := x.strip())]

    user_input = get_user_input(
        linesinputbox=20,
        size="900x450",
        title="File types",
        textabovebox="File types - separated with some kind of white space",
        submitbutton="Submit",
        regexcheck=r".*",
        showerror=("Error", "This is not a file type!"),
        showinfo=None,
        showwarning=None,
        icon=myicon,
    )
    allowed_extensions = tuple(['.' + g.lower().strip('. ') for x in user_input.split() if (g := x.strip())])

    if action == "NOFLAGS":
        dfa = monsterregex.find_all_in_folders(
            regular_expressions=regular_expressions,
            folders=[path],
            ignore_case=False,
            allowed_extensions=allowed_extensions,
            binary=False,
            dfa_size="1G",
            multiline=False,
            multiline_dotall=False,
            field_match_separator="ÇÇÇÇÇ",
        )

    if action == "DOTALL":
        dfa = monsterregex.find_all_in_folders(
            regular_expressions=regular_expressions,
            folders=[path],
            ignore_case=False,
            allowed_extensions=allowed_extensions,
            binary=False,
            dfa_size="1G",
            multiline=False,
            multiline_dotall=True,
            field_match_separator="ÇÇÇÇÇ",
        )

    if action == "MULTILINE":
        dfa = monsterregex.find_all_in_folders(
            regular_expressions=regular_expressions,
            folders=[path],
            ignore_case=False,
            allowed_extensions=allowed_extensions,
            binary=False,
            dfa_size="1G",
            multiline=True,
            multiline_dotall=False,
            field_match_separator="ÇÇÇÇÇ",
        )

    if action == "MULTILINE_DOTALL":
        dfa = monsterregex.find_all_in_folders(
            regular_expressions=regular_expressions,
            folders=[path],
            ignore_case=False,
            allowed_extensions=allowed_extensions,
            binary=False,
            dfa_size="1G",
            multiline=True,
            multiline_dotall=True,
            field_match_separator="ÇÇÇÇÇ",
        )

    if action == "BIN":
        dfa = monsterregex.find_all_in_folders(
            regular_expressions=regular_expressions,
            folders=[path],
            ignore_case=False,
            allowed_extensions=allowed_extensions,
            binary=True,
            dfa_size="1G",
            multiline=False,
            multiline_dotall=False,
            field_match_separator="ÇÇÇÇÇ",
        )

    if action == "BIN_DOTALL":
        dfa = monsterregex.find_all_in_folders(
            regular_expressions=regular_expressions,
            folders=[path],
            ignore_case=False,
            allowed_extensions=allowed_extensions,
            binary=True,
            dfa_size="1G",
            multiline=False,
            multiline_dotall=True,
            field_match_separator="ÇÇÇÇÇ",
        )

    if action == "BIN_MULTILINE":
        dfa = monsterregex.find_all_in_folders(
            regular_expressions=regular_expressions,
            folders=[path],
            ignore_case=False,
            allowed_extensions=allowed_extensions,
            binary=True,
            dfa_size="1G",
            multiline=True,
            multiline_dotall=False,
            field_match_separator="ÇÇÇÇÇ",
        )

    if action == "BIN_MULTILINE_DOTALL":
        dfa = monsterregex.find_all_in_folders(
            regular_expressions=regular_expressions,
            folders=[path],
            ignore_case=False,
            allowed_extensions=allowed_extensions,
            binary=True,
            dfa_size="1G",
            multiline=True,
            multiline_dotall=True,
            field_match_separator="ÇÇÇÇÇ",
        )

    if action == "I":
        dfa = monsterregex.find_all_in_folders(
            regular_expressions=regular_expressions,
            folders=[path],
            ignore_case=True,
            allowed_extensions=allowed_extensions,
            binary=False,
            dfa_size="1G",
            multiline=False,
            multiline_dotall=False,
            field_match_separator="ÇÇÇÇÇ",
        )

    if action == "I_DOTALL":
        dfa = monsterregex.find_all_in_folders(
            regular_expressions=regular_expressions,
            folders=[path],
            ignore_case=True,
            allowed_extensions=allowed_extensions,
            binary=False,
            dfa_size="1G",
            multiline=False,
            multiline_dotall=True,
            field_match_separator="ÇÇÇÇÇ",
        )

    if action == "I_MULTILINE":
        dfa = monsterregex.find_all_in_folders(
            regular_expressions=regular_expressions,
            folders=[path],
            ignore_case=True,
            allowed_extensions=allowed_extensions,
            binary=False,
            dfa_size="1G",
            multiline=True,
            multiline_dotall=False,
            field_match_separator="ÇÇÇÇÇ",
        )

    if action == "I_MULTILINE_DOTALL":
        dfa = monsterregex.find_all_in_folders(
            regular_expressions=regular_expressions,
            folders=[path],
            ignore_case=True,
            allowed_extensions=allowed_extensions,
            binary=False,
            dfa_size="1G",
            multiline=True,
            multiline_dotall=True,
            field_match_separator="ÇÇÇÇÇ",
        )

    if action == "I_BIN":
        dfa = monsterregex.find_all_in_folders(
            regular_expressions=regular_expressions,
            folders=[path],
            ignore_case=True,
            allowed_extensions=allowed_extensions,
            binary=True,
            dfa_size="1G",
            multiline=False,
            multiline_dotall=False,
            field_match_separator="ÇÇÇÇÇ",
        )

    if action == "I_BIN_DOTALL":
        dfa = monsterregex.find_all_in_folders(
            regular_expressions=regular_expressions,
            folders=[path],
            ignore_case=True,
            allowed_extensions=allowed_extensions,
            binary=True,
            dfa_size="1G",
            multiline=False,
            multiline_dotall=True,
            field_match_separator="ÇÇÇÇÇ",
        )

    if action == "I_BIN_MULTILINE":
        dfa = monsterregex.find_all_in_folders(
            regular_expressions=regular_expressions,
            folders=[path],
            ignore_case=True,
            allowed_extensions=allowed_extensions,
            binary=True,
            dfa_size="1G",
            multiline=True,
            multiline_dotall=False,
            field_match_separator="ÇÇÇÇÇ",
        )

    if action == "I_BIN_MULTILINE_DOTALL":
        dfa = monsterregex.find_all_in_folders(
            regular_expressions=regular_expressions,
            folders=[path],
            ignore_case=True,
            allowed_extensions=allowed_extensions,
            binary=True,
            dfa_size="1G",
            multiline=True,
            multiline_dotall=True,
            field_match_separator="ÇÇÇÇÇ",
        )

    app = TestApp(dfa)
    return app


if __name__ == "__main__":
    if len(sys.argv) == 1:
        futurnameofcompiledexe = "ripgrepgui.exe"
        multicommands = [
            {
                "mainmenuitem": "RipGrep",
                "submenu": "NOFLAGS",
                "folderinprogramdata": "RCTools",
                "add2drive": True,
                "add2folder": True,
                "additional_arguments": "--action NOFLAGS",
            },

            {
                "mainmenuitem": "RipGrep",
                "submenu": "DOTALL",
                "folderinprogramdata": "RCTools",
                "add2drive": True,
                "add2folder": True,
                "additional_arguments": "--action DOTALL",
            },

            {
                "mainmenuitem": "RipGrep",
                "submenu": "MULTILINE",
                "folderinprogramdata": "RCTools",
                "add2drive": True,
                "add2folder": True,
                "additional_arguments": "--action MULTILINE",
            },

            {
                "mainmenuitem": "RipGrep",
                "submenu": "MULTILINE_DOTALL",
                "folderinprogramdata": "RCTools",
                "add2drive": True,
                "add2folder": True,
                "additional_arguments": "--action MULTILINE_DOTALL",
            },

            {
                "mainmenuitem": "RipGrep",
                "submenu": "BIN",
                "folderinprogramdata": "RCTools",
                "add2drive": True,
                "add2folder": True,
                "additional_arguments": "--action BIN",
            },

            {
                "mainmenuitem": "RipGrep",
                "submenu": "BIN_DOTALL",
                "folderinprogramdata": "RCTools",
                "add2drive": True,
                "add2folder": True,
                "additional_arguments": "--action BIN_DOTALL",
            },

            {
                "mainmenuitem": "RipGrep",
                "submenu": "BIN_MULTILINE",
                "folderinprogramdata": "RCTools",
                "add2drive": True,
                "add2folder": True,
                "additional_arguments": "--action BIN_MULTILINE",
            },

            {
                "mainmenuitem": "RipGrep",
                "submenu": "BIN_MULTILINE_DOTALL",
                "folderinprogramdata": "RCTools",
                "add2drive": True,
                "add2folder": True,
                "additional_arguments": "--action BIN_MULTILINE_DOTALL",
            },

            {
                "mainmenuitem": "RipGrep",
                "submenu": "I",
                "folderinprogramdata": "RCTools",
                "add2drive": True,
                "add2folder": True,
                "additional_arguments": "--action I",
            },

            {
                "mainmenuitem": "RipGrep",
                "submenu": "I_DOTALL",
                "folderinprogramdata": "RCTools",
                "add2drive": True,
                "add2folder": True,
                "additional_arguments": "--action I_DOTALL",
            },

            {
                "mainmenuitem": "RipGrep",
                "submenu": "I_MULTILINE",
                "folderinprogramdata": "RCTools",
                "add2drive": True,
                "add2folder": True,
                "additional_arguments": "--action I_MULTILINE",
            },

            {
                "mainmenuitem": "RipGrep",
                "submenu": "I_MULTILINE_DOTALL",
                "folderinprogramdata": "RCTools",
                "add2drive": True,
                "add2folder": True,
                "additional_arguments": "--action I_MULTILINE_DOTALL",
            },

            {
                "mainmenuitem": "RipGrep",
                "submenu": "I_BIN",
                "folderinprogramdata": "RCTools",
                "add2drive": True,
                "add2folder": True,
                "additional_arguments": "--action I_BIN",
            },

            {
                "mainmenuitem": "RipGrep",
                "submenu": "I_BIN_DOTALL",
                "folderinprogramdata": "RCTools",
                "add2drive": True,
                "add2folder": True,
                "additional_arguments": "--action I_BIN_DOTALL",
            },

            {
                "mainmenuitem": "RipGrep",
                "submenu": "I_BIN_MULTILINE",
                "folderinprogramdata": "RCTools",
                "add2drive": True,
                "add2folder": True,
                "additional_arguments": "--action I_BIN_MULTILINE",
            },

            {
                "mainmenuitem": "RipGrep",
                "submenu": "I_BIN_MULTILINE_DOTALL",
                "folderinprogramdata": "RCTools",
                "add2drive": True,
                "add2folder": True,
                "additional_arguments": "--action I_BIN_MULTILINE_DOTALL",
            },

        ]
        add_multi_commands_to_drive_and_folder(
            futurnameofcompiledexe,
            multicommands,
        )
    else:
        try:
            app=main()
            app.mainloop()
            try:
                sys.exit(0)
            finally:
                os._exit(0)

        except Exception as fe:
            print(fe)
            try:
                sys.exit(1)
            finally:
                os._exit(1)


