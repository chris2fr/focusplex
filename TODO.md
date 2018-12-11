# Why ToDo

## Journal Activities for Historical Nostalgia

The actions of tasks done can be consulted later in life to appreciate the beauty of things. This can be a journaling tool too.

## Link to Contact Applications

The who criteriao around a task my reference entities from external calendar applications. The link could even be one-to-many, possibly.

## Link with Calendar Apps

Any what or why can include a calendar apointment with a ver prefixed to it.

## Bulk Modification of Results

A user can modify multiple todos at once to reclassify them under another taskwhy. The current process is two-step, line by line.

## Import and Export Whats

It would be nice to be able to export branches, trees and leaves of whats and to import them too.

## Unit Tests and Documentation

Code elegantly and according to good practices. The situation has already come about where I have broken simple features as seen through the web interface.

## Confirm the Who User Proxy Object

The data model considers the "Who" table to be, among other things, a proxy for users. We should make sure that this works correctly insomuch as the What object is linked to the Who object. Linking the What object to a application user could be inelegant.

I think the whats are currently assigned directly to a Django user rather than going through the Who object as a proxy. This seems inelegant to me.

## Review Ordering Options

Perhaps consider alphabetical order from within the lists, still having the top todos first. It may be better to do a recursive lookup on taskwhys under taskwhys ratjer than relyting on result__id which gives a strange behavior.

## Detach from Admin Pages 

At the current time every user needs to be a super-user with admin pages that give access to all todos in the website. The change would be to not rely on these outside admin pages for management of the todo lists.

In the interim, it is possible to add zoom in the redirect after modifications on the admin pages. That would bring us back to a filtered list.

A amjor disadvantage to the using of the admin pages is that the candidate what.result.id is not filtered to only the whats that belong to the current who of the current user.

## Integrate In-Place Editing   

The idea is to click on a line and make it directly editable.

## Have a More Appealing / Usable Layout

I really haven't paid any attention to the layout of the application. It would be nice to make it prettier and perhaps more ergonomic. 

## Drag and Drop

It would be useful to move and rearrange the todos by drag and drop. Any todo can be filed under an other why.

## Cascaded Sharing

A user may share any goal, objective or activity with others.

## Idea for the To Do Die

A TODO die would have six sides, like any die, inspired by the symbols above the numbers 1 2 3 4 5 6 on the US keyboard :

1. ! - Why (alternatively ?)
2. @ - Who
3. &#35; (hashtag) - What
4. $ - How
5. % - When 
6. ^ - Where

These could be extra fields for each todo. Each definition of a field could actually be variable.

WHY ! could be a todo or field of characters.

WHO @ could be a distinct object, either a person, an abstract concept or an organization, or a link in an LDAP directory, or a user account

WHAT # could be a todo or a text field

HOW $ could be money, a howto document, a description (text area/document)

WHEN % could be a point in time, a duration in time, a duration, a set of work sessions (past and to come), a time of day or even a semaphore waiting for input from a third part.

WHERE ^ could be a URL, an address, geo coordonates, a concept, etc

This chapter could be relegated to a TODO.md file.
