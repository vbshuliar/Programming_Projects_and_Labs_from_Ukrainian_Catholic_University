"""Notebook."""
from datetime import date
from random import uniform


class Notebook:
    """Notebook."""

    def __init__(self, notes: list):
        """
        Receives information.
        >>> my_note = Note("Hello", ["mood", "happy"])
        >>> my_note2 = Note("Bye", ["mood", "sad"])
        >>> my_note3 = Note("Mama", ["family", "parents"])
        >>> my_notebook = Notebook([my_note, my_note2, my_note3])
        >>> my_notebook.notes[0].tags
        ['mood', 'happy']
        """
        self.notes = notes

    def __str__(self):
        """
        Brief information about notebook.
        >>> my_note = Note("Hello", ["mood", "happy"])
        >>> my_note2 = Note("Bye", ["mood", "sad"])
        >>> my_note3 = Note("Mama", ["family", "parents"])
        >>> my_notebook = Notebook([my_note, my_note2, my_note3])
        >>> print(my_notebook)
        Your notebook consists of 3 notes.
        """
        return f"Your notebook consists of {len(self.notes)} notes."

    def search(self, filter: str):
        """
        Search option.
        >>> my_note = Note("Hello", ["mood", "happy"])
        >>> my_note2 = Note("Bye", ["mood", "sad"])
        >>> my_note3 = Note("Mama", ["family", "parents"])
        >>> my_notebook = Notebook([my_note, my_note2, my_note3])
        >>> text = my_notebook.search("mood")
        >>> text[0][0]
        'Hello'
        """
        filtered = []
        for _ in self.notes:
            if filter in _.tags:
                filtered.append([_.memo, _.creation_date, _.tags])
        if len(filtered) > 0:
            return filtered
        return f"Sorry, no matches."

    def new_note(self, memo, tags=""):
        """
        Option to make new note.
        >>> my_note = Note("Hello", ["mood", "happy"])
        >>> my_notebook = Notebook([my_note])
        >>> my_notebook.new_note("Father", ["family", "parents"])
        >>> my_notebook.notes[1].memo
        'Father'
        """
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id, memo):
        """
        Modifies memo.
        >>> my_note = Note("Hello", ["mood", "happy"])
        >>> my_notebook = Notebook([my_note])
        >>> my_notebook.modify_memo(0, "Crazy")
        'No note with your id.'
        """
        for _ in self.notes:
            if _.note_id == note_id:
                _.memo = memo
                return f"Note #{note_id} was successfully modified."
        return "No note with your id."

    def modigy_tags(self, note_id, tags):
        """
        >>> my_note = Note("Hello", ["mood", "happy"])
        >>> my_notebook = Notebook([my_note])
        >>> my_notebook.modify_memo(0, ["greetings"])
        'No note with your id.'
        """
        for _ in self.notes:
            if _.note_id == note_id:
                _.tags = tags
                return f"Tags for note #{note_id} were successfully modified."
        return "No note with your id."


class Note:
    """Note."""

    def __init__(self, memo, tags):
        """
        Receives information.
        >>> my_note = Note("Hello", ["mood", "happy"])
        >>> my_note.memo
        'Hello'
        """
        self.memo = memo
        self.creation_date = str(date.today())
        self.tags = tags
        self.note_id = round(uniform(100000000, 999999999))

    def __str__(self):
        """
        Brief information about note.
        >>> my_note = Note("Hello", ["mood", "happy"])
        >>> text = my_note.__str__()
        >>> text[-18:]
        'Tags: mood, happy.'
        """
        return f"""Id: {self.note_id}.
Date: {self.creation_date}.
Text: {self.memo}.
Tags: {", ".join(self.tags)}."""

    def match(self, search_filter):
        """
        Search filter.
        >>> my_note = Note("Hello", ["mood", "happy"])
        >>> my_note.match("ell")
        True
        """
        if search_filter in self.memo:
            return True
        return False


if __name__ == "__main__":
    import doctest

    print(doctest.testmod())
