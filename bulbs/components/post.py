from html.parser import HTMLParser
from slugify import slugify


class PostParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.parsing_script = False
        self.content = []
        
    def handle_starttag(self, tag, attrs):
        print (tag, attrs)
        if tag == "script":
            self.parsing_script = True
        self.content.append("<{0}>".format(tag))
            
    def handle_endtag(self, tag):
        if tag == "script":
            self.parsing_script = False
        self.content.append("</{0}>".format(tag))
            
    def handle_data(self, data):
        if not self.parsing_script:
            data = data.replace("\r\n", "<br>")
        self.content.append(data)
            
    def script_content(self):
        return self.script_body
    
    def parsed_content(self):
        return self.content
        
def format_post(message):
    parser = PostParser()
    parser.feed(message)
    
    return "".join(parser.parsed_content())
    
def append_id_to_slug(slug, id):
    if id == 0:
        return slug
        
    id_slug = "{0}-{1}".format(slug, id)
    
    return id_slug