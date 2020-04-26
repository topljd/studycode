from lxml import etree
str_origin = '''
<?xml version="1.0" encoding="ISO-8859-1"?>
<bookstore>
<book>
  <title lang="eng">Harry Potter</title>
  <price>29.99</price>
</book>
<book>
  <title lang="eng">Learning XML</title>
  <price>39.95</price>
</book>
</bookstore>
'''
str_xml = etree.HTML(str_origin)
#bookstore
result = str_xml.xpath('bookstore')
print(result)
#[]

#/bookstore
result = str_xml.xpath('/bookstore')
print(result)
#[]

