from ebooklib import epub


page = ()
spine = ["nav"]
x=0

def create_book():
    return epub.EpubBook()


def add_metadata(book, metadata):
    book.set_identifier(metadata["identifier"])
    book.set_title(metadata["title"])
    book.set_language(metadata["language"])
    book.add_author(metadata["author"])


def add_css(book):
    style = """
    @namespace epub "http://www.idpf.org/2007/ops";
    body {
        font-family: Cambria, Liberation Serif, Bitstream Vera Serif, Georgia, Times, Times New Roman, serif;
    }
    h2 {
        text-align: left;
        text-transform: uppercase;
        font-weight: 200;
    }
    p {
        text-indent:2em;
    }
    ol {
            list-style-type: none;
    }
    ol > li:first-child {
            margin-top: 0.3em;
    }
    nav[epub|type~='toc'] > ol > li > ol  {
        list-style-type:square;
    }
    nav[epub|type~='toc'] > ol > li > ol > li {
            margin-top: 0.3em;
    }
    """

    # add css file
    nav_css = epub.EpubItem(
        uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style
    )
    book.add_item(nav_css)


def add_page_to_toc(c):
    global page
    page = page + (c,)


def add_page(book, text, title, number):
    global spine
    global x
    c = epub.EpubHtml(title=title, file_name=str(number) + ".xhtml", lang="zh-ch")
    temp = u'<!DOCTYPE html><html lang="zh-cn"><head></head><body><h3>' + title +'</h3>'+ text + '</body></html>'
    c.content = temp
    book.add_item(c)
    spine.append(c)
    add_page_to_toc(c)


def main(metadata, text, title):
    number = len(text)
    book = create_book()
    add_metadata(book, metadata)
    x = 0
    while number != 0:
        add_page(book, text[x], title[x], x)
        x = x + 1
        number = number - 1
    book.toc = page
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    add_css(book)
    book.spine = spine
    epub.write_epub("./res/test.epub", book, {})


