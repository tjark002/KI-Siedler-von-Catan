@echo off 
REM ACHTUNG: Diese müssen zwingend mit einer Kommandozeile aus dem Projektordner heraus aufgerufen werden! Es wird keinerlei Haftung für die Auswirkungen dieses Skripts übernommen.
REM Der Name der Haupt-Tex-Datei (z.B. Arbeit) muss als Argument übergeben werden.
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