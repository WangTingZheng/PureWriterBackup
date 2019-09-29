from ebooklib import epub

book = epub.EpubBook()
# set metadata
book.set_identifier("id123456")
book.set_title("Sample book")
book.set_language("zh-cn")

book.add_author("Author Authorowski")
book.add_author(
    "Danko Bananko", file_as="Gospodin Danko Bananko", role="ill", uid="coauthor"
)

# create chapter
c1 = epub.EpubHtml(title="Intro", file_name="chap_01.xhtml", lang="hr")
c1.content = u"<h1>hello</h1><p>Zaba je skocila u baru.</p>"

# add chapter
book.add_item(c1)

# define Table Of Contents
book.toc = (
    epub.Link("chap_01.xhtml", "Introduction", "intro"),
    (epub.Section("Simple book"), (c1,)),
)

# add default NCX and Nav file
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())

# define CSS style
style = "BODY {color: white;}"
nav_css = epub.EpubItem(
    uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style
)

# add CSS file
book.add_item(nav_css)

# basic spine
book.spine = ["nav", c1]

# write to the file
epub.write_epub("test.epub", book, {})
