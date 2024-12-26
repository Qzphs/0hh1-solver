from tkinter import PhotoImage


class Asset:

    def __init__(self, filename: str):
        self.filename = filename
        self._image: PhotoImage | None = None

    def image(self):
        if self._image is None:
            self._image = PhotoImage(file=self.filename)
        return self._image
