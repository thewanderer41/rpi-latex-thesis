RPI Thesis LaTeX
================

Check out the original version [markemer/rpi-latex-thesis](http://github.com/markemer/rpi-latex-thesis).

I have made a number of changes to the Thesis class;
**These changes are in no way endorsed by any official at RPI/OGE.**

## Summary of Changes

- Now using Unix line-endings, with no blank spaces at the end of lines
- Commented out the bibentry def.
  Un-comment [line 314](https://github.com/gonsie/rpi-latex-thesis/blob/master/thesis.cls#L314) "for use in making an unnumbered bibliography with hanging indents."
- Added a Candidacy title page (no signature lines).
  Use the command `\softtitlepage`.
- Added command for self attribution footnote. See [template/rpithes.tex:27](https://github.com/gonsie/rpi-latex-thesis/blob/master/template/rpithes.tex#L27) and the OGE Thesis Manual (page 12).

# RPI Resources

Hard copies of some of the needed forms can be found in the OGE-forms folder.

- RPI's Office of Graduate Education for Current Students: http://gradoffice.rpi.edu/update.do?catcenterkey=2
  - see right-hand sidebar for links to forms and checklists
- RPI's Academic Calendar: http://www.rpi.edu/academics/calendar
  - includes thesis/dissertation due dates
  - includes deadlines for defences
- Offical Thesis/Dissertation guide: http://www.rpi.edu/dept/grad/docs/ThesisManual.pdf
  - includes guidelines for citing your own work
  - includes document style/formatting specifications
- dotCIO Thesis Page: http://dotcio.rpi.edu/services/printing-publishing/thesis-preparation
  - includes original LaTeX and MSWord templates

# Pro Tips!

Over the years, many students have had difficulties in having their theses accepted by OGE.
In an attempt to alleviate this process, several individuals have passed on their wisdom.
These pro-tips can be found in the tips folder, including:

- [ThesisFormatting.md](https://github.com/gonsie/rpi-latex-thesis/blob/master/tips/ThesisFormatting.md): This file lists several reasons why a thesis was returned to a student.
- [Medha_Atre_Comments.md](https://github.com/gonsie/rpi-latex-thesis/blob/master/tips/Medha_Atre_Comments.md): This file contains Medha's comments on the thesis submission process, as emailed to the CSGrads list in September 2011.
- [Terry_Hayden_Pro_Tips.md](https://github.com/gonsie/rpi-latex-thesis/blob/master/tips/Terry_Hayden_Pro_Tips.md): This file is a collection of several tips from Terry Hayden.
