# Django Why Application

This application takes a perspective on todo lists. Why do we do what we do? I often forget myself. The point here is remember why I do what I do. The application does this by inserting a 'why' into the todo list. In order to achieve some goal I do some activity. The goal and the thing are both representable by 'todo' items. 

As a list progresses, the activities can become intermediate goals with other activities attached to them. Therefor, and this is important, the new intermediate is strictly the same as a previous activity. The todo is both an intermediate goal and an intermediate activity. The trunck todos are goals, the branch todos are intermediate activities at their base, the branch todos are intermediate goals at their bifurcations, and the leaf todos are activities.

Practicaly, it is presented in the following format :

To achieve WHY do WHAT.

Both WHY and WHAT are TODO items. A TODO is composed of a verb without in the infinitive form without the 'to' and a verb usually with a direct complement. 

The simplicity is beautiful. There is no tree view actually, just a table view. Everything is on one page. 

## Idea for the To Do Die

A TODO die would have six sides, like any die:

1. ! - Why (alternatively ?)
2. @ - Who
3. # - What
4. $ - How
5. % - When 
6. ^ - Where

These could be extra fields for each todo. Each definition of a field could actually be variable.

WHY could be a todo or field of characters.

WHO could be a distinct object, either a person, an abstract concept or an organization, or a link in an LDAP directory, or a user account

WHAT could be a todo or a text field

HOW could be money, a howto document, a description (text area/document)

WHEN could be a point in time, a duration in time, a duration, a set of work sessions (past and to come), and a time of day

WHERE could be a URL, an address, geo coordonates, a concept, etc

This chapter could be relegated to a TODO.md file.