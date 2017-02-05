# Dieses Programm fügt alle jpg-Bilder im aktuellen Ordner in ein gelatextes Pdf ein
# Daniel Fertmann

import os
import re

print()
print("##########################################")
print("#      A       t         PPP  DDD  FFFFF #")
print("#     AA       t         P  P D  D   F   #")
print("#    A A       ttt   oo  P  P D  D   F   #")
print("#   AAAA u  u  t    o  o PPP  D  D   FFF #")
print("#  A   A u  u  t    o  o P    D  D   F   #")
print("# A    A  uuuu  ttt  oo  P    DDD    F   #")
print("##########################################")
print()

pfad = os.getcwd()
pfadSplit = os.path.split(pfad)
aufgabenKategorie, aufgabenArt = pfadSplit[1], os.path.split(pfadSplit[0])[1]
login = os.getlogin() # liest Nutzername aus.

print("###Hallo",login+"!!!")

print("###Suche Bilder im akuellen Ordner (" + pfad + ") ...")
dir = os.listdir()
bilder = list(filter(lambda x: re.match(r".*jpg",x.lower()), dir))# Regulärer Ausdruck, um Bilder zu filtern

print("###Erstelle TEX-Datei...")
dateiInhalt = r"""
\documentclass{scrartcl}
\usepackage[utf8]{inputenc}
\usepackage{german}
% \usepackage[latin1]{inputenc}
\usepackage[german]{babel}

% zusätzliche mathematische Symbole, AMS=American Mathematical Society
\usepackage{amssymb}

% fürs Einbinden von Graphiken
\usepackage{graphicx}

% für Namen etc. in Kopf- oder Fußzeile
\usepackage{fancyhdr}

% erlaubt benutzerdefinierte Kopfzeilen
\pagestyle{fancy}

% Definition der Kopfzeile
\lhead{
""" + login + r"""
}
\chead{Mathe}
\rhead{\today{}}
\lfoot{}
\cfoot{Seite \thepage}
\rfoot{}

\begin{document}

\section*{""" + aufgabenArt + " " + aufgabenKategorie + r"""}
"""

for bild in bilder:
    dateiInhalt += r"""
\subsection*{""" + bild.replace("_","\_") + r"""}
\includegraphics[width=1\textwidth]{""" + bild + r"""}

    """
dateiInhalt += "\n\end{document}"

f = open("inhalt.tex","w")
f.write(dateiInhalt)
f.close()

print("###Erzeuge PDF-Datei mit LaTex...")
os.system("pdflatex inhalt.tex")

print("###und nochmal für die Seitennummer...")
os.system("pdflatex inhalt.tex")

print("###Datei 'inhalt.pdf' ist fertig!!!")
