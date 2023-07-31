# Wikipedia Replication
This is project number 1 of the CS50 Web Development course with Django and JavaScript lectured by Harvard CS department.

## Screencast of project

## Entry Page
Visiting /wiki/TITLE, where TITLE is the title of an encyclopedia entry, renders a page that displays the contents of that encyclopedia entry.

If an entry is requested that does not exist, the user is presented with an error page indicating that their requested page was not found.

If the entry does exist, the user is presented with a page that displays the content of the entry. The title of the page includes the name of the entry.

<img width="945" alt="image" src="https://github.com/Fernando-Urbano/cs50w-p1-wiki/assets/99626376/555a4ae3-2160-4273-b092-fba9ac7317e0">

## Index Page
The user can click on any entry name to be taken directly to that entry page.

![image](https://github.com/Fernando-Urbano/cs50w-p1-wiki/assets/99626376/7b1c7bda-0d86-4c87-a182-75c828c41b71)

## Search
Allow the user to type a query into the search box in the sidebar to search for an encyclopedia entry.

If the query matches the name of an encyclopedia entry, the user is redirected to that entry’s page.

If the query does not match the name of an encyclopedia entry, the user is instead taken to a search results page that displays a list of all encyclopedia entries that have the query as a substring. For example, if the search query were "ytho", then "Python" appears in the search results.

Clicking on any of the entry names on the search results page takes the user to that entry’s page.

![image](https://github.com/Fernando-Urbano/cs50w-p1-wiki/assets/99626376/6376eedb-a055-488e-b797-a4f16924f502)

## New Page
Clicking “Create New Page” in the sidebar takes the user to a page where they can create a new encyclopedia entry.

Users can enter a title for the page and, in a textarea, can enter the Markdown content for the page.

![image](https://github.com/Fernando-Urbano/cs50w-p1-wiki/assets/99626376/41f90f04-afba-48f7-b7a4-a054d77bf882)

Users can click a button to save their new page.

When the page is saved, if an encyclopedia entry already exists with the provided title, the user is presented with an error message. Otherwise, the encyclopedia entry is saved to disk, and the user is taken to the new entry’s page.

![image](https://github.com/Fernando-Urbano/cs50w-p1-wiki/assets/99626376/81d5871f-c349-4c5c-b74e-186fe1b1f715)

## Edit Page
On each entry page, the user can click a link to be taken to a page where the user can edit that entry’s Markdown content in a textarea.

The textarea is pre-populated with the existing Markdown content of the page. (i.e., the existing content should be the initial value of the textarea).

The user can click a button to save the changes made to the entry.

Once the entry is saved, the user is redirected back to that entry’s page.

![image](https://github.com/Fernando-Urbano/cs50w-p1-wiki/assets/99626376/bbe6b158-6808-4c30-9d83-9035b09abd97)

## Random Page
Clicking “Random Page” in the sidebar takes the user to a random encyclopedia entry.

![image](https://github.com/Fernando-Urbano/cs50w-p1-wiki/assets/99626376/4fb23d33-69ea-487b-bd21-794662fcf374)

## Markdown to HTML Conversion
On each entry’s page, any Markdown content in the entry file should be converted to HTML before being displayed to the user.



