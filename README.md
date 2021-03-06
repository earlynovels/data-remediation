# Data Remediation
Remediation of END dataset, summer 2018.

This repository contains files and process documentation pertaining to to remediation of the Early Novels Dataset initiated in May 2018.
The most recent master copy of the dataset is located on the [END Dataset repository](<https://github.com/earlynovels/end-dataset>).

## Summary of changes to dataset

- 8-3-18 remediating errors in complete dataset 09122017-full.mrk

- 11-7-18 checking/remediation of Summer 2018 new records (new-records-09072018.xml)

- 11-28-18 identifying and removing empty records from canonical datafile. Empty records can be viewed [here](https://github.com/earlynovels/data-remediation/blob/master/old/pre-2014-empty-recs.xml)

- 11-28-18 compiling remediated datasets for new canonical dataset: (11282018-full.xml)

- 1-11-19 adding 18 previously excluded 2015 records: (missing-2015.xml)

## Summer 2018 Dataset modifications

Remediating 2017 and previous records: Changes pushed directly to [09132017-full.mrk](/earlynovels/data-remediation/blob/master/09132017-full.mrk)
- All records with no date given filler date 10/10/10 (END only began to record dates in 2011, and so these records are generally the early ones, barring those later records that for some reason are dateless.) 6/18/2018
- Added 260$c to records 440217, 440221, 440259 (identified by Alice as being without a publication date.) 6/20/2018
- Other records provided by Alice have weirder issues: 380966 has different date in 260 vs. 001. 440313 and 440377 are both missing entire 260 field. 440425 is just a bizarre record, very sparse?
- Changed “Title-page” to “Title Page” in 599$b 6/28/2018
- Changed “First person” to “First-person” in 592$b (2 modifications) 6/28/2018
- Changeed “Table of Contents” to “Table of contents” in 520$a (119 modifications) 7/2/2018
- Changed “To the reader” to “To the Reader” in 520$a (156 modifications) 7/2/2018
- Deleted period from “To the Reader.” in 520$a (1 modification) 7/2/2018

### 246$d
- Change “Letter press” to Letter-press” (6 modifications) 7/5/2018
- Change “Letter- press” to “Letter-press” 7/5/2018
- Change “Letter-Press” to “Letter-press” (44 modifications) 7/5/2018
- Change “Letter-press “ to “Letter-press” (4 modifications) 7/5/2018
- Change “Letter-press,” to “Letter-press” (1 modifications) 7/5/2018
- Change “Letter-press.” to “Letter-press” (4 modifications) 7/5/2018
- Change “letter-press” to “Letter-press” (2 modifications) 7/5/2018
- Change “Lettter-press” to “Letter-press” (2 modifications) 7/5/2018
- “Letter-ress” to “Letter-press” (1 modifications) 7/5/2018

### 246$g
- “full” to “Full” (3 modifications) 7/5/2018
- “Half.” to “Half” (2 modifications) 7/5/2018

### 246$v
- “v. 1” to “v.1” (23 modifications) 7/5/2018
- “v. 2” to “v.2” (21 modifications) 7/5/2018
- “v. 3” to “v.3” (4 modifications) 7/5/2018
- “v. 4” to “v.4” (2 modifications) 7/5/2018
- “v. 5” to “v.5” (2 modifications) 7/5/2018
- “v. 6” to “v.6” (2 modifications) 7/5/2018
- “v. 7” to “v.7” (2 modifications) 7/5/2018
- “v.I” to “v.1” (1 modification) 7/5/2018
- “v. I” to “v.1” (3 modifications) 7/5/2018
- “v.1 “ to “v.1” (29 modifications) 7/5/2018
- “v.2 “ to “v.2” (17 modifications) 7/5/2018
- “v.3 “ to “v.3” (4 modifications) 7/5/2018
- (One or two errors I made but fixed--When I replace “v.I” to “v.1”, it turned entries like “v.II” into “v.1I” “v.III” into “v.1II”--I think I caught and fixed all of them)

### 246$x
- “Work “ to “Work” (13 modifications) 7/6/2018
- “Volume “ to “Volume” (11 modifications) 7/6/2018
- 250$b
- “Edition” to “edition” (10 modifications) 7/6/2018
- “edition.” to “edition” (115 modifications) 7/6/2018
- “edition “ to “edition” (3 modifications) 7/6/2018

### 260$a
- “London :” to “London” (524 modifications) 7/6/2018
- “London:” to “London” (63 modifications) 7/6/2018
- “ London” to “London” (2 modifications) 7/6/2018
- “[London] :” to “[London]” (3 modifications) 7/6/2018
- “London “ to “London” (16 modifications) 7/6/2018
- “[Baltimore] :” to “[Baltimore]” (1 modification) 7/6/2018
- “[New York] :” to “[New York]” (1 modification) 7/6/2018
- “[Philadelphia?] :” to “[Philadelphia?]” (1 modification) 7/6/2018
- “[Philadelphia] :” to “[Philadelphia]” (1 modification) 7/6/2018
- “Albany :” to “Albany” (2 modifications) 7/6/2018
- “Berwick:” to “Berwick” (1 modification) 7/6/2018
- “Boston :” to “Boston” (31 modifications)  7/6/2018
- “Boston,” to “Boston” (3 modifications) 7/6/2018
- “Boston:” to “Boston” (2 modifications) 7/6/2018
- “Brattleborough :” to “Brattleborough” (1 modification) 7/6/2018
- “Brookfield,” to “Brookfield” (1 modification) 7/6/2018
- “Cambridge:” to “Cambridge” (1 modification) 7/6/2018
- “Chiswick :” to “Chiswick” (1 modification) 7/6/2018
- “Cincinnati :” to “Cincinnati” (2 modifications) 7/6/2018
- “St. Louis :” to “St. Louis” (1 modification) 7/6/2018
- “Dublin :” to “Dublin” (62 modifications) 7/6/2018
- “Dublin “ to “Dublin” (3 modifications) 7/6/2018
- “Edinburgh :” to “Edinburgh” (36 modifications) 7/6/2018
- “Exeter :” to “Exeter” (1 modification) 7/6/2018
- “ :” deleted (211 modifications) 7/6/2018
- “:” deleted (28 modifications) 7/6/2018
- “;” deleted (3 modifications) 7/7/2018
- “London,” to “London” (66 modifications) 7/7/2018
- “London.” to “London” (12 modifications) 7/7/2018
- “A Londres,” to “A Londres” (1 modification) 7/7/2018
- “Parma.” to “Parma” (1 modification) 7/7/2018
- “Philadelphia,” to “Philadelphia” (4 mods) 7/7/2018
- “Philadelphia.” to “Philadelphia” (2 mods) 7/7/2018
- “New York.” to “New York” (1 mod) 7/7/2018

### 300$x
- “Duodecimio” to “Duodecimo” (1) 7/11/2018
- “duodecimo” to “Duodecimo” (5) 7/11/2018
- “Duodecimo “ to “Duodecimo” (10) 7/11/2018
- “Duodecimo.” to “Duodecimo” (7) 7/11/2018
- “Ocatvo” to “Octavo” (2) 7/11/2018
- “Octavo.” to “Octavo” (2) 7/11/2018

### 520$a
- “Dedication.” to “Dedication” (2 mods) 7/10/2018
- 520$c
- “Back “ to “Back” (5) 7/11/2018
- “Front” to “Front” (7) 7/11/2018
- “Front “ to “Front” (19) 7/11/2018
- “Front.” to “Front” (12) 7/11/2018
- “Middle.” to “Middle” (3) 7/11/2018
- Delete “.” (15) 7/11/2018
- 520$v
- “v. 1” to “v.1” (16) 7/11/2018
- “v. 2” to “v.2” (15) 7/11/2018
- “v.1.” to “v.1” (17) 7/11/2018
- “v.1 “ to “v.1” (23) 7/11/2018
- “v.2.” to “v.2” (10) 7/11/2018
- “v.2 “ to “v.2” (8) 7/11/2018
- “Vol. 1” to “v.1” (2) 7/11/2018

### 591$v
- “v.1.” to “v.1” (4) 7/17/2018
- “v.2.” to “v.2” (5) 7/17/2018
- “v.v1” to “v.1” (1) 7/17/2018

### 592$a
- “Dramatic Dialogue” to “Dramatic dialogue” (1) 7/17/2018
- “Dramatic dialogue “ to “Dramatic dialogue” (2) 7/17/2018
- “First-person.” to “First-person” (4) 7/17/2018
- “First person” to “First-person” 7/17/2018
- “Third person” to “Third-person” 7/17/2018
- “Third- person” to “Third-person” (1) 7/17/2018
- “Third-Person” to “Third-person” (3) 7/17/2018
- “Third-person “ to “Third-person” (2) 7/17/2018
- 592$b
- “Dramatic Dialogue” to “Dramatic dialogue” (6) 7/17/2018
- “Epistolary” to “Letters” (81) 7/17/2018
- “First-person “ to “First-person” (1) 7/17/2018
- “Letter(s)” to “Letters” (19) 7/17/2018
- “Third person” to “Third-person” (3) 7/17/2018
- “Third-person “ to “Third-person” (1) 7/17/2018
- “Poem(s)” to “Poems” (25) 7/17/2018
- “Poem” to “Poems” (29) 7/17/2018
- “Poemss” to “Poems” (28) 7/17/2018
- NOTES:
- A lot of the info in this subfield should be in 592$c such as “Poems” “Sheet music” etc.
- “Essay” has been used several times, but isn’t a term we have in the guide.
- 592$c
- “Dramatic Dialogue” to “Dramatic dialogue” (3) 7/17/2018
- “Dramatic dialogue as in a play” to “Dramatic dialogue” (3) 7/17/2018
- “Poem” to “Poems” (450) 7/17/2018
- “Poemss” to “Poems” (426) 7/17/2018
- “Dramatic dialogue” to “Theatrical dialogue” (14) 7/17/2018
- “Poems “ to “Poems” (5) 7/17/2018
- “sheet music” to “Sheet music” (1) 7/17/2018
- “Sheet music “ to “Sheet music” (4) 7/17/2018
- “Theatrical Dialogue” to “Theatrical dialogue” (1) 7/17/2018
- NOTES:
- Lots of terms used here that aren’t controlled/in the guide
- Lots of multiple 592s
- Probably could change “Verse” to “Poems” but want to make sure cataloger wasn’t somehow distinguishing between the two?
- What to do with “Song”?

### 594$v
- “v. 1” to “v.1” (9) 7/17/2018
- “v. 2” to “v.2” (5) 7/17/2018
- “v.2.” to “v.2” (2) 7/17/2018
- 595$v
- “v. 1 “ to “v.1” (1) 7/17/2018
- “v. 1” to “v.1” (5) 7/17/2018

### 596a
- “Translation “ to “Translation” (5) 7/17/2018
- 596b
- “Advertisement “ to “Advertisement” (1) 7/17/2018
- “Title page” to “Title Page” (163) 7/17/2018
- “To the reader” to “To the Reader” (3) 7/17/2018
- “The Editor’s Advertisment” to “Advertisement” (2) 7/17/2018
- “Preface, by the translator” to “Preface” (1) 7/17/2018
- “Full title page” to “Title Page” (11) 7/17/2018
- NOTES:
- Many uncontrolled terms
- Appears to have been used instead of a 599 a few times
- 596$c
- “French “ to “French” (5) 7/18/2018
- 596$d
- NOTES:
- Two people used this field as a location field? I.e. one record says “Title page” another “Title Page”. Should probably just be deleted.
- 596$v
- “v. 2” to “v.2” (1) 7/18/18

### 599$a
- “Author (source text) “ to “Author (source text)” (3) 7/18/18
- “Author( text)” to “Author (text)” (1) 7/18/18
- “Author(paratext)” to “Author (paratext)” (28) 7/18/18
- “Author(text)” to “Author (text)” (58) 7/18/18
- “Editor (text) “ to “Editor (text)” 7/18/18
- “(text) “ to “(text)” (24) 7/18/18
- “Translator(text)” to “Translator (text)” (4) 7/18/18
- “(paratext) “ to “(paratext)” (6) 7/18/18
- “Editor(text)” to “Editor (text)” (3) 7/18/18
- NOTES:
- Some wacky ones in here, such as “Editor (Footnotes)” and “Illustrator (paratext)”, etc. One “Publisher ()”, which should just be deleted presumably?
- 599$b
- “By Proper Name” to “Proper name” (14) 7/18/18
- “By proper name” to “Proper name” (21) 7/18/18
- “Proper name “ to “Proper name” (8) 7/18/18
- “Generic/ Descriptive” to “Generic/Descriptive” 7/18/18
- “Generic/Description” to “Generic/Descriptive” (5) 7/18/18
- “Generic/descriptive” to “Generic/Descriptive” (432) 7/18/18
- “Genertic/Descriptive” to “Generic/Descriptive” (1) 7/18/18
- “Genetic/Descriptive” to “Generic/Descriptive” (1)  7/18/18
- “Proper Name” to “Proper name” (22)  7/18/18
- “Proper name “ to “Proper name” (1) 7/18/18
- “Reference to other works.” to “Reference to other works” (2) 7/18/18
- “Personal name” to “Proper name” (7) 7/18/18
- “General/Descriptive” to “Generic/Descriptive” (7) 7/18/18
- “General/descriptive” to “Generic/Descriptive” (6) 7/18/18
- 599$3
- “Title page” to “Title Page” (839) 7/18/18
- “Dedication.” to “Dedication” (1) 7/18/18
- “First title page” to “Title Page” (1)  7/18/18
- “Full title page” to “Title Page” (89) 7/18/18
- “Full Title Page” to “Title Page” (11) 7/18/18
- 599$5
- “Female “ to “Female” (2) 7/24/18
- “Indeterminate “ to “Indeterminate” (4) 7/24/18
- “Male “ to “Male” (9) 7/24/18
- “Unknown” to “Indeterminate” 7/24/18
- 599$6
- “Female “ to “Female” (4) 7/24/18
- “Male “ to “Male” (11) 7/24/18
- “Indeterminate” to “Unknown” (27) 7/24/18
- “Unknown “ to “Unknown” (4) 7/24/18
- “Unkown” to “Unknown” (2)7/24/18

### 656a
- “Mixed-genre” to “Mixed Genre” (14)
- “Mixed genre” to “Mixed Genre” (178)
- “Nonfiction” to “Non-fiction” (2)
- “Mixed Genre “ to “Mixed Genre” (2)
- “Mixed-Genre” to “Mixed Genre” (5)

### 656c
- “No clear relation to work” to “No relation” (1)
- “Same Publisher” to “Same publisher” (22)
- “Same Author” to “Same author” (1)
- “Same publisher “ to “Same publisher” (2)
- “Same publisher.” to “Same publisher” (2)
- “Same publishers” to “Same publisher” (1)
- “Same author “ to “Same author” (4)

### 656v
- “v. 2” to “v.2” (3)
- “v.2 “ to “v.2” (2)
- “v. 3” to “v.3” (2)
- “v.1.” to “v.1” (1)
- “v.1 “ to “v.1” (1)
- “v.3 “ to “v.3” (1)

### 700$4
- “Author (bookplate) “ to “Author (bookplate) (5)
- “Auhor (text)” to “Author (text) (1)
- “Author (epigraph) “ to “Author (epigraph)”
- “Author (Inscription) “ to “Inscribed by”
- “Author (inscription) to “Inscribed by” (118)
- “Author (paratextual essay)” to “Author (paratext)” (5)
- “Author (text) “ to “Author (text)” (11)
- “Author(paratext)” to “Author (paratext)” (10)
- “Author(text)” to “Author (text)” (38)
- “Inscribed  by” to “Inscribed by” (2)
- “Inscribed by “ to “Inscribed by” (7)
- “Inscribed name” to “Inscribed by” (28)
- “Inscription” to “Inscribed by” (3)
- “Printed by (text)” to “Printed by” (5)
- “Printed for “ to “Printed for” (51)
- “Printed for(text)” to “Printed for” (16)
- “Supposed author” to “Supposed author (text)” (75)
- “Supposed Author (text)” to “Supposed author (text)”
- “Supposed author (text) (text)” to “Supposed author (text) (51)
- “Supposed author (text).” to “Supposed author (text)” (1)
- “Translated by” to “Translator (text)” (7)
- “Translator(text)” to “Translator (text)” (5)
- “Author( paratext)” to “Author (paratext)” (1)
- “Dedicated to” to “Dedicatee” (12)
- “Illustrator” to “Author (Illustration)” (28)
- “Illustrated by” to “Author (Illustration)
- “Author (Illustration)” to “Author (illustration)” (32)

Completed 8-3-18 by Sam Herron

## Fall 2018 data remediation

Remediation and quality control of Summer 2018 records: changes made directly to [new-records-09072018.xml](/earlynovels/data-remediation/blob/master/new-records-09072018.xml)

- Fixed fields 999$b and 999$c
- Standardized control terms for 700$4 and 700$5
- Standardized control terms in 599$a, b, 3, 5, 6
- Standardized 595$b
- Standardized fields 592$b and 592$c
- Standardized control terms in field 592$a
- Standardized control terms in field 520$a
- Standardized 250$b field
- Standardized control term in 700$4: “Author (text)” and control term …  …
- Standardized “London” in field “260”, subfield “a”
- standardized control terms: v.1, v.2
- Standardized control terms in field "246", subfield "v": v.1, v.2, v.…  …
- Finished fixing subfield errors
- Fixing subfield code errors

Completed 11-28-18 by Ina Chen and Alice McGrath
