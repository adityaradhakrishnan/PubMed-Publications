# PubMed-Parse
A python script to scrape the PubMed database via NCBI E-Utils to generate an HTML file with a publication list for a given query, including both PubMed and journal article links. Quick and easy publication lists for academic web pages.

Currently, you have to edit the script directly, namely the "Query" variable. A future version will support a command line argument.

Furthermore, this code can be simplified by using the [Entrez module from Biopython](http://biopython.org/DIST/docs/api/Bio.Entrez-module.html), but this implementation works with Python out of the box.
