class Book(object):

    def __init__(self, name, num_chapters):
        self.name = name
        self.num_chapters = num_chapters
        if num_chapters <= 0 or num_chapters > 150:
            raise ValueError('Invalid number of chapters')
        self.chapter_descr = [None] * num_chapters


    def set_chapter_descr(self, chapter, descr):
        """Sets the chapter description

        Arguments:
        chapter -- chapter number
        descr -- the description for the chapter        

        Raises:
        IndexError if chapter outside of bounds
        ValueError if descr is an empty string or None
        """
        if (chapter <= 0 or chapter > self.num_chapters):
            raise IndexError('Invalid chapter number')
        if (descr == "" or descr is None):
            raise ValueError("Invalid description")
        self.chapter_descr[chapter - 1] = descr