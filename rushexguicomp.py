from nutikacompile import compile_with_nuitka

wholecommand = compile_with_nuitka(
    pyfile=r"C:\ProgramData\anaconda3\envs\nu\ripgrepgui.pyw",
    icon=r"C:\ProgramData\anaconda3\envs\nu\regexlogo.ico",
    disable_console=True,
    file_version="1.0.0.0",
    onefile=True,
    outputdir="c:\\ripgrepguicompiled",
    addfiles=[
r"C:\ProgramData\anaconda3\envs\nu\rg.exe",
r"C:\ProgramData\anaconda3\envs\nu\regexlogo.ico",
    ],
    delete_onefile_temp=False,  # creates a permanent cache folder
    needs_admin=True,
    arguments2add="--msvc=14.3 --noinclude-numba-mode=nofollow --plugin-enable=tk-inter --jobs=3",
)
