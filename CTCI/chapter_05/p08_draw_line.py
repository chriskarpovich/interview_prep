"""
A monochrome screen is stored as a single array of bytes, allowing eight consecutive pixels to be stored in one byte. The screen has width w,
where w is divisible by 8 (that is, no byte will be split across rows). The height of the screen, of course, can be derived from the length
of the array and the width. Implement a function that draws a horizontal line from (x1, y) to (x2, y).

The method signature should look something like: drawLine(byte[] screen, int width, int x1, int x2, int y)
"""

def draw_line(screen, width, x1, x2, y):
    height = int((len(screen) * 8) / width)
    width = int(width / 8)
    for i in range(height):
        for j in range(width):
            idx = j + i*height
            print(idx)
            pixel_min = j*8
            pixel_max = j*8 + 7
            row = 0
            if i == y and pixel_min >= x1:
                if x2 > pixel_max:
                    screen[idx] = 0xFF
                else:
                    x2_scaled = x2 - j*8
                    one_place = 7
                    row = 0
                    while x2_scaled >= 0:
                        row = row | (1 << one_place)
                        x2_scaled -= 1
                        one_place -= 1
                    screen[idx] = row
    print(screen)
    return screen




def test_0b11111111_0b11111111() -> None:
    screen = bytearray(2)
    draw_line(screen, width=16, x1=0, x2=15, y=0)
    assert screen == bytearray([0b11111111, 0b11111111])


def test_0b01111100() -> None:
    screen = bytearray(1)
    draw_line(screen, width=8, x1=1, x2=5, y=0)
    assert screen == bytearray([0b01111100])


def test_0b01111100_with_y_equals_1() -> None:
    screen = bytearray(3)
    draw_line(screen, width=8, x1=1, x2=5, y=1)
    assert screen == bytearray([0b00000000, 0b01111100, 0b000000000])


def test_0b00000011_0b11111111_0b11000000() -> None:
    screen = bytearray(3)
    draw_line(screen, width=24, x1=6, x2=17, y=0)
    assert screen == bytearray([0b00000011, 0b11111111, 0b11000000])

if __name__ == "__main__":
    test_0b00000011_0b11111111_0b11000000()
    test_0b01111100()
    test_0b01111100_with_y_equals_1()
    test_0b11111111_0b11111111()
