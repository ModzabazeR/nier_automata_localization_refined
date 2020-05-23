#!/usr/bin/python3

from format.utils import *


class Header:
    @staticmethod
    def parse(reader):
        result = Header()
        result.magic = read_bytes(reader, 118)
        assert_magic(result.magic, b"FTB ")
        result.textures_count = read_int(reader, 2)
        result.unknown = read_bytes(reader, 2)
        result.chars_count = read_int(reader, 2)
        result.textures_offset = read_int(reader, 4)
        result.chars_offset = read_int(reader, 4)
        result.chars_offset2 = read_int(reader, 4)
        return result

    def serialize(self):
        result = bytearray()
        result += self.magic
        result += write_int(self.textures_count, 2)
        result += self.unknown
        result += write_int(self.chars_count, 2)
        result += write_int(self.textures_offset, 4)
        result += write_int(self.chars_offset, 4)
        result += write_int(self.chars_offset, 4)
        return result


class Character:
    @staticmethod
    def parse(reader):
        result = Character()
        result.char = read_utf16(reader, 2)
        result.texture_id = read_int(reader, 2)
        result.width = read_int(reader, 2)
        result.height = read_int(reader, 2)
        result.u = read_int(reader, 2)
        result.v = read_int(reader, 2)
        return result

    def serialize(self):
        result = bytearray()
        result += write_utf16(self.char, 2)
        result += write_int(self.texture_id, 2)
        result += write_int(self.width, 2)
        result += write_int(self.height, 2)
        result += write_int(self.u, 2)
        result += write_int(self.v, 2)
        return result


class File:
    @staticmethod
    def parse(reader):
        result = File()
        reader.seek(0)
        result.header = Header.parse(reader)

        reader.seek(result.header.textures_offset)
        result.textures = read_bytes(reader, result.header.textures_count * 16)

        reader.seek(result.header.chars_offset)
        result.chars = []
        for i in range(result.header.chars_count):
            result.chars.append(Character.parse(reader))
        return result

    def find_space_for_glyph(self, glyph_size, texture_size, page):
        glyphs = [
            (c.u, c.v, c.width, c.height) for c in self.chars if c.texture_id == page
        ]
        w = glyph_size[0]
        h = glyph_size[1]
        x = texture_size[0] - w - 1
        y = texture_size[1] - h - 1

        def collides_with_boxes(box, otherboxes):
            x, y, w, h = box
            for otherbox in otherboxes:
                x2, y2, w2, h2 = otherbox
                if x < x2 + w2 and x + w > x2 and y < y2 + h2 and y + h > y2:
                    return True
            return False

        while not collides_with_boxes((x, y, w, h), glyphs) and y > 0:
            y -= 1
        y += 1
        while not collides_with_boxes((x, y, w, h), glyphs) and x > 0:
            x -= 1
        x += 1
        if not collides_with_boxes((x, y, w, h), glyphs):
            return (x, y)
        raise Exception("cannot place character")

    def add_character(self, value, texture, width, height, u, v):
        char = Character()
        char.char = value
        char.texture_id = texture
        char.width = width - 1
        char.height = height - 1
        char.u = u
        char.v = v
        self.chars.append(char)
        self.chars.sort(key=lambda c: c.char)

    def get_glyphs(self, textures, font_id=0):  # font_id is ignored
        result = {}
        for c in self.chars:
            if c.width == 0 or c.height == 0 or not c.char:
                continue
            u1 = c.u
            u2 = c.u + c.width + 1
            v1 = c.v
            v2 = c.v + c.height + 1
            result[c.char] = textures[c.texture_id].crop((u1, v1, u2, v2))
        return result

    def serialize(self):
        result = bytearray()
        self.header.chars_count = len(self.chars)
        result += self.header.serialize()
        result += self.textures
        for c in self.chars:
            result += c.serialize()
        result += b"\0" * 0x88  # padding?
        return result
