from math import ceil
from typing import List


class PhotoAlbum:

    PHOTOS_PER_PEGE: int = 4
    DASHES = 11

    def __init__(self, pages: int):
        self.pages = pages
        self.photos: List[List[str]] = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):

        return cls(ceil(photos_count / cls.PHOTOS_PER_PEGE))

    def add_photo(self, label: str) -> str:

        for page_num, page in enumerate(self.photos):

            if len(page) < self.PHOTOS_PER_PEGE:

                slot = len(page) + 1
                page.append(label)

                return f"{label} photo added successfully on page {page_num + 1} slot {slot}"

        return "No more free slots"

    def display(self) -> str:

        output = ["-" * self.DASHES]

        for page in self.photos:

            output.append(("[] " * len(page)).strip())
            output.append("-" * self.DASHES)

        return "\n".join(output)


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
