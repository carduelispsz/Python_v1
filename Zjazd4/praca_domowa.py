class Element:

    def __init__(self, text):
        self.text = text

    def render(self):
        return self.text


class HeaderElement:
    def __init__(self, text):
        self.head = text

    def render(self):
        self.link = self.head.title()
        return f'# {self.head}'


class LinkElement:

    def __init__(self, text, domain):
        self.link = text
        self.domain = domain  # do not add http:// to domain input :p

    def render(self):
        self.link = f'({self.link})'
        self.domain = f'http://{self.domain}'
        return self.link + self.domain


class Document:
    def __init__(self, attribute=''):
        self.docu = [attribute]

    def add_element(self, attribute):
        self.docu.append(attribute)

def test_klasa_element():
    elem = Element('Simple text')
    assert elem.render() == 'Simple text'



#
# text = Element('Simple text')
# print(f'{text.basic_render()}')
#
# text = HeaderElement('Header header')
# print(f'{text.header_render()}')
#
# text = LinkElement('ABC', 'abc.com')
# print(f'{text.link_render()}')