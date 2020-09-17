@echo off 
REM ACHTUNG: Diese m�ssen zwingend mit einer Kommandozeile aus dem Projektordner heraus aufgerufen werden! Es wird keinerlei Haftung f�r die Auswirkungen dieses Skripts �bernommen.
REM Der Name der Haupt-Tex-Datei (z.B. Arbeit) muss als Argument �bergeben werden.
cd %~dp0
set texSource=%1
pdflatex  -synctex=1 -interaction=nonstopmode --src-specials "%texSource%.tex"
bibtex "%texSource%"
makeindex "%texSource%.nlo" -s nomencl.ist -o "%texSource%.nls"
makeglossaries "%texSource%"
pdflatex  -synctex=1 -interaction=nonstopmode --src-specials "%texSource%.tex"
pdflatex  -synctex=1 -interaction=nonstopmode --src-specials "%texSource%.tex"
makeindex "%texSource%.nlo" -s nomencl.ist -o "%texSource%.nls"
pdflatex  -synctex=1 -interaction=nonstopmode --src-specials "%texSource%.tex"
clean.bat