from rich.console import Console
from typing import List

# Elements in the list can be:
# 1. Range of code points in the destructed list format (e.g. *list(range({start unicode (inclusive)}, {end unicode (exclusive)})))
# 2. A single code point (eg. just 0x0e01)
chars_to_add: List[int] = [
    # Thai glyphs (https://www.compart.com/en/unicode/block/U+0E00)
    # Change it to your language unicode range (see: https://www.compart.com/en/unicode/block)
    # Note that some code point in the block might not be used. For example, in Thai block, the
    # range is 0x0e00 - 0x0e7f but 0x0e3b - 0x0e3e and 0x0e5c - 0x0e7f is not used.
    # only add the code point that is used in the font.
    *list(range(0x0e01, 0x0e31)),
    *list(range(0x0e3f, 0x0e47)),
    *list(range(0x0e4f, 0x0e5c)),
]

class MyConsole(Console):
    HEADING_STYLE = "bold white on blue"

    def heading(self, text: str):
        super().rule(f"[{self.HEADING_STYLE}]{text}", style=self.HEADING_STYLE)


langFormats = {
    "jp": {
        "default": "",
        "novel": ""
    },
    "en": {
        "default": "_us",
        "novel": "_eng"
    },
    "fr": {
        "default": "_fr",
        "novel": "_fra"
    },
    "it": {
        "default": "_it",
        "novel": "_ita"
    },
    "de": {
        "default": "_de",
        "novel": "_ger"
    },
    "es": {
        "default": "_es",
        "novel": "_esp"
    },
}