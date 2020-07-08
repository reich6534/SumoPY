class Book(object):

    def __init__(self, name, num_chapters):
        self.name = name
        self.num_chapters = num_chapters
        if num_chapters <= 0 or num_chapters > 150:
            raise ValueError('Invalid number of chapters')
        self.chapter_descr = [None] * num_chapters


    def set_chapter_descr(self, chapter, descr):

        if (chapter < 1 or chapter > self.num_chapters):
            raise IndexError('Chapter is outside of bounds')
        if (descr == "" or descr is None):
            raise ValueError("Invalid description")
        self.chapter_descr[chapter - 1] = descr

    def get_num_chapters(self):
        return self.num_chapters
