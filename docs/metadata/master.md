---
header-includes: 
  - \input{metadata/solarized-colors.tex}
  - \input{metadata/listings-setup.tex}
---

\frontmatter

$if(title)$
\begin{titlepage}
    \begin{center}
        \vspace*{1cm}
        \Huge
        \textbf{$title$}
        
        \vspace{0.5cm}
        \large
        $author$
        
        \vfill
        
        $date$
    \end{center}
\end{titlepage}
$endif$

% \input{content/abstract.md}
\tableofcontents

\mainmatter

\input{docs/sections/computational_thinking.md}
\input{docs/sections/arbeitshypothese.md}
\input{docs/sections/methode.md}
\input{docs/sections/kern.md}
\input{docs/sections/daten.md}
\input{docs/sections/auswertung.md}
\input{docs/sections/ausblick.md}
\input{docs/sections/reflexion.md}

\backmatter

\input{docs/sections/literatur.md}
\input{docs/sections/verzeichnisse.md}
\input{docs/sections/import_code.md}
