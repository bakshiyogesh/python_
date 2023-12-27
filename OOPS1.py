#Python class variable
from pprint import pprint
class HTML:
    version:5
    extension:"html" 

#if you trying to access class variables that doesn't exist you'll get Attribute error

extension=getattr(HTML,'extension',"text/html");
print(extension)   #in this you will also get error but we specify here default value

# as like getting attribute we have method for setting and deleting attribute
#for setting attribute
# setattr(HTML,media_type,'text/html');
#for deleting a class attribute
html=HTML()
# delattr(html,'media_type');

from pprint import pprint


class HtmlDocument:
    extension = 'html'
    version = '5'


HtmlDocument.media_type = 'text/html'

pprint(HtmlDocument.__dict__)
# Python stores class variables in the __dict__ attribute. The __dict__ attribute is a dictionary.