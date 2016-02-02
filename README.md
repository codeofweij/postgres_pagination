# postgres_pagination

code to manage pagination for a dataset's larger than 100k+ rows. 

# why in postgres ?

this saves time from generating the pagination for every lookup. Pagination objects are easy to store in advance.

# how it works

	calling repository.paginate(...) will return a hash of pages to the first entry of the page

	page | name
    1.   | ""
    2.   | Charles Frank
    3.   | Harrison Peter
    4.   | Laura Jones
    5.   | Zack Peter

    this once saved will be used to pass the respective name into 

    repository.get_names(...)


# caveats

will not work without proper indexing to ensure the table does not do a full scan when looking up 1 page element.

