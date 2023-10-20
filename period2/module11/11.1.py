class publication:

    def __init__(self, name):
        self.name = name

    def print_information(self):
        print(f"Publication: {self.name}")

class book(publication):

    def __init__(self, name, author, page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)

    def print_information(self):
        super().print_information()
        print(f"Author: {self.author}.\n{self.page_count} pages")

class magazine(publication):

    def __init__(self, name, chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)

    def print_information(self):
        super().print_information()
        print(f"Chief editor: {self.chief_editor}.")

list_publication = []
list_publication.append(magazine("Donald Duck", "Aki Hyyppä"))
list_publication.append(book("Compartment No. 6", "Rosa Liksom", 192))

for p in list_publication:
    p.print_information()