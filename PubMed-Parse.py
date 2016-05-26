import urllib2 as url

# Initialize output HTML file and fill with just enough to make a 
# minimal HTML5 document

pubHTML = open('Publications.html','w')

pubHTML.write("<!DOCTYPE html>\n")
pubHTML.write("<html lang=en>\n")
pubHTML.write("<head>\n")
pubHTML.write("<meta charset=utf-8>\n")
pubHTML.write("<title>Publication List</title>\n")
pubHTML.write("</head>\n")
pubHTML.write("<body>\n")
pubHTML.write("<ol reversed>\n")

# Use NCBI E-Utils to search PubMed for a given query and return a 
# list of P(ub)M(ed)IDs which can then be used with E-Summary to get 
# the metadata for each publication.
# 
# Modify NumResults for...a different max number of results.

Base         = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
eSearch      = "esearch.fcgi?db=pubmed&term="
eSummary     = "esummary.fcgi?db=pubmed&id="
Query        = "aditya%20radhakrishnan[author]"
NumResults   = 1000

QueryURL     = Base + eSearch + Query + "&retmax=" + str(NumResults)

PubMedList   = url.urlopen(QueryURL)

for line in PubMedList:
    if line[0:4] == "<Id>":
        try:
            IDList
        except NameError:
            IDList = line[4:12]
        else:
            IDList = IDList + "," + line[4:12]

print IDList
            
QueryURL     = Base + eSummary + IDList
Publications = url.urlopen(QueryURL)

# Go through the XML metadata file and extract all the data required
# in a proper publication citation.

for line in Publications:
    
    # Initialize variables on each instance of DocSum. Else, parse the
    # relevant data.
    
    if line[1:5] == "<Id>":
        DOILink = ""
        PMCLink = ""
        AFlag   = 0
        Link    = line[5:-6]
    if line[1:21] == "<Item Name=\"PubDate\"":
        Date = line[34:-8]
        Year = Date[0:4]
    if line[1:20] == "<Item Name=\"Source\"":
        Journal = line[35:-8]
    if line[2:21] == "<Item Name=\"Author\"":
        if AFlag == 0:
            Author = line[36:-8]
            AFlag  = 1
        else:
            Author = Author + ", " + line[36:-8]
    if line[1:19] == "<Item Name=\"Title\"":
        Title = line[34:-8]
    if line[1:20] == "<Item Name=\"Volume\"":
        Volume = line[35:-8]
    if line[1:19] == "<Item Name=\"Pages\"":
        Pages = line[34:-8]
    if line[2:18] == "<Item Name=\"doi\"":
        DOILink = "http://dx.doi.org/" + line[33:-8]
    if line[2:18] == "<Item Name=\"pmc\"":
        PMCLink = "http://www.ncbi.nlm.nih.gov/pmc/articles/" + line[33:-8]

    if line[0:9] == "</DocSum>":
        if (DOILink == "") and (PMCLink == ""):
            OutL = "No Link Available"
        elif DOILink == "":
            OutL = PMCLink
        else:
            OutL = DOILink

        OutS = "<li> " + Author + ". (" + Year + ") " + Title + " <em>"
        OutS = OutS + Journal + "</em> " + Volume + ": " + Pages + "<br />"
            
        pubHTML.write(OutS)
            
        OutS = "<a href=\"http://ncbi.nlm.nih.gov/pubmed/" + Link + "\">PubMed Link</a>"

        if OutL == "No Link Available":
            OutS = OutS + "<br />"
        else:
            OutS = OutS + " | <a href=\"" + OutL + "\">Link to Article</a><br />"
            
        pubHTML.write(OutS)

pubHTML.write("</ol>")
pubHTML.write("</body>\n")
pubHTML.write("</html>\n")
pubHTML.close()
