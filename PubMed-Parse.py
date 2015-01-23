import urllib2 as url

#
# Initialize output HTML file and fill with just
# enough to make a minimal HTML5 document
#

pubHTML = open('Publications.html','w')

pubHTML.write("<!DOCTYPE html>\n")
pubHTML.write("<meta charset=utf-8>\n")
pubHTML.write("<title>Publication List</title>\n")

#
# Technically you don't have to close the file
# object, because the OS handles that on termination
# of Python, but it's just good coding practice.
#

pubHTML.close()