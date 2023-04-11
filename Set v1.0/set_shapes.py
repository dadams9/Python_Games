import pygame as pg

class set_shapes:
    #methods
    def __init__(self, s='circle', n=1, c=(155, 0, 0), p='solid'):
        self.shape = s
        self.number = n
        self.color = c
        self.pattern = p

    def __str__(self):
        return "Shape:{}, Number:{}, Color:{}, Pattern:{}".format(self.shape, self.number, self.color, self.pattern)

    def get_shape(self):
        return self.shape
    def set_shape(self, s):
        self.shape = s

    def get_number(self):
        return self.number
    def set_number(self, n):
        self.number = n

    def get_color(self):
        return self.color
    def set_color(self, c):
        self.color = c

    def get_pattern(self):
        return self.pattern
    def set_pattern(self, p):
        self.pattern = p

    def create_shape(self, surf, x, y):
        #Draw a triangle of any pattern, color, or number --------------------------------------------------------------
        if self.shape == 'triangle':

            if self.number == 1:
                pg.draw.polygon(surf, self.color, [(x + 115, y + 115), (x + 185, y + 115), (x + 150, y + 50)])

                if self.pattern == 'hollow':
                    pg.draw.polygon(surf, (255, 255, 255), [(x + 120, y + 112), (x + 180, y + 112), (x + 150, y + 57)])

                elif self.pattern == 'striped':
                    j = [110, 101, 92, 82, 72, 60, 72, 82, 92, 101, 110]
                    h = [3, 12, 21, 31, 41, 53, 41, 31, 21, 12, 3]
                    k = 0
                    for i in range(120, 186, 6):
                        pg.draw.rect(surf, (255, 255, 255), [x + i, y + j[k], 2, h[k]])
                        k += 1

            if self.number == 2:
                pg.draw.polygon(surf, self.color, [(x + 52, y + 115), (x + 122, y + 115), (x + 87, y + 50)])
                pg.draw.polygon(surf, self.color, [(x + 174, y + 115), (x + 244, y + 115), (x + 209, y + 50)])

                if self.pattern == 'hollow':
                    pg.draw.polygon(surf, (255, 255, 255), [(x + 57, y + 112), (x + 117, y + 112), (x + 87, y + 57)])
                    pg.draw.polygon(surf, (255, 255, 255), [(x + 179, y + 112), (x + 239, y + 112), (x + 209, y + 57)])

                elif self.pattern == 'striped':
                    j = [110, 101, 92, 82, 72, 60, 72, 82, 92, 101, 110]
                    h = [3, 12, 21, 31, 41, 53, 41, 31, 21, 12, 3]
                    k = 0
                    for i in range(57, 123, 6):
                        pg.draw.rect(surf, (255, 255, 255), [x + i, y + j[k], 2, h[k]])
                        k += 1

                    k = 0
                    for i in range(179, 245, 6):
                        pg.draw.rect(surf, (255, 255, 255), [x + i, y + j[k], 2, h[k]])
                        k += 1


            if self.number == 3:
                pg.draw.polygon(surf, self.color, [(x + 22, y + 115), (x + 92, y + 115), (x + 57, y + 50)])
                pg.draw.polygon(surf, self.color, [(x + 115, y + 115), (x + 185, y + 115), (x + 150, y + 50)])
                pg.draw.polygon(surf, self.color, [(x + 208, y + 115), (x + 278, y + 115), (x + 243, y + 50)])

                if self.pattern == 'hollow':
                    pg.draw.polygon(surf, (255, 255, 255), [(x + 27, y + 112), (x + 87, y + 112), (x + 57, y + 57)])
                    pg.draw.polygon(surf, (255, 255, 255), [(x + 120, y + 112), (x + 180, y + 112), (x + 150, y + 57)])
                    pg.draw.polygon(surf, (255, 255, 255), [(x + 213, y + 112), (x + 273, y + 112), (x + 243, y + 57)])

                elif self.pattern == 'striped':
                    j = [110, 101, 92, 82, 72, 60, 72, 82, 92, 101, 110]
                    h = [3, 12, 21, 31, 41, 53, 41, 31, 21, 12, 3]
                    k = 0
                    for i in range(27, 93, 6):
                        pg.draw.rect(surf, (255, 255, 255), [x + i, y + j[k], 2, h[k]])
                        k += 1

                    k = 0
                    for i in range(120, 186, 6):
                        pg.draw.rect(surf, (255, 255, 255), [x + i, y + j[k], 2, h[k]])
                        k += 1

                    k = 0
                    for i in range(213, 279, 6):
                        pg.draw.rect(surf, (255, 255, 255), [x + i, y + j[k], 2, h[k]])
                        k += 1


        #Draw a square of any pattern, color, or number-----------------------------------------------------------------
        if self.shape == 'square':
            if self.number == 1:
                pg.draw.rect(surf, self.color, [x + 115, y + 52, 70, 70])

                if self.pattern == 'hollow':
                    pg.draw.rect(surf, (255, 255, 255), [x + 120, y + 57, 60, 60])

                if self.pattern == 'striped':
                    for i in range(119, 180, 6):
                        pg.draw.rect(surf, (255, 255, 255), [x+i, y+56, 2, 62])

            elif self.number == 2:
                pg.draw.rect(surf, self.color, [x + 52, y + 52, 70, 70])
                pg.draw.rect(surf, self.color, [x + 174, y + 52, 70, 70])

                if self.pattern == 'hollow':
                    pg.draw.rect(surf, (255, 255, 255), [x + 57, y + 57, 60, 60])
                    pg.draw.rect(surf, (255, 255, 255), [x + 179, y + 57, 60, 60])

                if self.pattern == 'striped':
                    for i in range(56, 127, 6):
                        pg.draw.rect(surf, (255, 255, 255), [x+i, y+56, 2, 62])
                    for i in range(178, 239, 6):
                        pg.draw.rect(surf, (255, 255, 255), [x+i, y+56, 2, 62])

            elif self.number == 3:
                pg.draw.rect(surf, self.color, [x + 22, y + 52, 70, 70])
                pg.draw.rect(surf, self.color, [x + 115, y + 52, 70, 70])
                pg.draw.rect(surf, self.color, [x + 208, y + 52, 70, 70])

                if self.pattern == 'hollow':
                    pg.draw.rect(surf, (255, 255, 255), [x + 27, y + 57, 60, 60])
                    pg.draw.rect(surf, (255, 255, 255), [x + 120, y + 57, 60, 60])
                    pg.draw.rect(surf, (255, 255, 255), [x + 213, y + 57, 60, 60])

                if self.pattern == 'striped':
                    for i in range(26, 90, 6):
                        pg.draw.rect(surf, (255, 255, 255), [x+i, y+56, 2, 62])
                    for i in range(119, 180, 6):
                        pg.draw.rect(surf, (255, 255, 255), [x+i, y+56, 2, 62])
                    for i in range(212, 273, 6):
                        pg.draw.rect(surf, (255, 255, 255), [x+i, y+56, 2, 62])

        #Draw a circle of any pattern, color, or number-----------------------------------------------------------------
        j = [73, 68, 61, 57, 55, 53, 55, 57, 61, 68, 73]
        r = [28, 38, 52, 60, 62, 63, 62, 60, 52, 38, 28]
        k = 0
        if self.shape == "circle":
            if self.number == 1:
                pg.draw.circle(surf, self.color, (x+150, y+87), 35)
                if self.pattern == 'hollow':
                    pg.draw.circle(surf, (255, 255, 255), (x+150, y+87), 30)
                elif self.pattern == "striped":
                    for i in range(119, 185, 6):
                        pg.draw.rect(surf, (255, 255, 255), [x + i, y + j[k], 2, r[k]])
                        k += 1

            elif self.number == 2:
                pg.draw.circle(surf, self.color, (x + 80, y + 87), 35)
                pg.draw.circle(surf, self.color, (x + 220, y + 87), 35)
                if self.pattern == 'hollow':
                    pg.draw.circle(surf, (255, 255, 255), (x + 80, y + 87), 30)
                    pg.draw.circle(surf, (255, 255, 255), (x + 220, y + 87), 30)
                elif self.pattern == "striped":
                    k = 0
                    for i in range(49, 115, 6):
                        pg.draw.rect(surf, (255, 255, 255), [x + i, y + j[k], 2, r[k]])
                        k += 1
                    k = 0
                    for i in range(189, 255, 6):
                        pg.draw.rect(surf, (255, 255, 255), [x + i, y + j[k], 2, r[k]])
                        k += 1

            elif self.number == 3:
                pg.draw.circle(surf, self.color, (x + 70, y + 87), 35)
                pg.draw.circle(surf, self.color, (x + 150, y + 87), 35)
                pg.draw.circle(surf, self.color, (x + 230, y + 87), 35)

                if self.pattern == 'hollow':
                    pg.draw.circle(surf, (255, 255, 255), (x + 70, y + 87), 30)
                    pg.draw.circle(surf, (255, 255, 255), (x + 150, y + 87), 30)
                    pg.draw.circle(surf, (255, 255, 255), (x + 230, y + 87), 30)

                elif self.pattern == 'striped':
                    for i in range(39, 105, 6):
                        pg.draw.rect(surf, (255, 255, 255), [x + i, y + j[k], 2, r[k]])
                        k += 1

                    k = 0
                    for i in range(119, 185, 6):
                        pg.draw.rect(surf, (255, 255, 255), [x + i, y + j[k], 2, r[k]])
                        k += 1

                    k = 0
                    for i in range(199, 265, 6):
                        pg.draw.rect(surf, (255, 255, 255), [x + i, y + j[k], 2, r[k]])
                        k += 1