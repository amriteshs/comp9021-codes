# Defines two classes, Point() and Disk().
# The latter has an "area" attribute and three methods:
# - change_radius(r)
# - intersects(disk), that returns True or False depending on whether
#   the disk provided as argument intersects the disk object.
# - absorb(disk), that returns a new disk object that represents the smallest
#   disk that contains both the disk provided as argument and the disk object.
#
# Written by Amritesh Singh and Eric Martin for COMP9021


from math import pi, hypot


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x:.2f}, {self.y:.2f})'


class Disk:
    def __init__(self, *, centre=Point(), radius=0.0):
        self.centre = Point(x=centre.x, y=centre.y)
        self.radius = radius
        self.area = pi * (radius ** 2)

    def __repr__(self):
        return f'Disk({self.centre}, {self.radius:.2f})'

    def change_radius(self, radius):
        self.radius = radius
        self.area = pi * (radius ** 2)

    def intersects(self, disk):
        distance_between_centres = hypot(self.centre.x - disk.centre.x, self.centre.y - disk.centre.y)

        if abs(self.radius - disk.radius) <= distance_between_centres or distance_between_centres <= self.radius + disk.radius:
            return True

        return False

    def absorb(self, disk):
        distance_between_centres = hypot(self.centre.x - disk.centre.x, self.centre.y - disk.centre.y)

        if abs(self.radius - disk.radius) < distance_between_centres:
            new_centre_x = 0.5 * (((self.centre.x - self.radius * disk.centre.x / (self.radius + distance_between_centres)) / (1 - self.radius / (self.radius + distance_between_centres))) + ((disk.centre.x - disk.radius * self.centre.x / (disk.radius + distance_between_centres)) / (1 - disk.radius / (disk.radius + distance_between_centres)))) + 0
            new_centre_y = 0.5 * (((self.centre.y - self.radius * disk.centre.y / (self.radius + distance_between_centres)) / (1 - self.radius / (self.radius + distance_between_centres))) + ((disk.centre.y - disk.radius * self.centre.y / (disk.radius + distance_between_centres)) / (1 - disk.radius / (disk.radius + distance_between_centres)))) + 0
            new_radius = 0.5 * (distance_between_centres + self.radius + disk.radius)
            return Disk(centre=Point(x=new_centre_x, y=new_centre_y), radius=new_radius)

        if self.radius <= disk.radius:
            return Disk(centre=disk.centre, radius=disk.radius)

        return Disk(centre=self.centre, radius=self.radius)


if __name__ == '__main__':
    disk_1 = Disk()
    print(disk_1)
    print(disk_1.area)
    disk_2 = Disk(centre=Point(3, 0), radius=4)
    print(disk_2.area)
    print(disk_1.intersects(disk_2))
    print(disk_2.intersects(disk_1))
    disk_3 = disk_1.absorb(disk_2)
    print(disk_3)
    disk_1.change_radius(2)
    print(disk_1.area)
    disk_3 = disk_1.absorb(disk_2)
    print(disk_1)
    print(disk_2)
    print(disk_3)
    disk_4 = Disk(centre=Point(-4, 0), radius=2)
    print(disk_4.intersects(disk_1))
    disk_5 = disk_4.absorb(disk_1)
    print(disk_5)
    disk_5.change_radius(5)
    print(disk_5)
    disk_6 = Disk(centre = Point(1, 2), radius = 6)
    print(disk_5)
    print(disk_6)
    disk_7 = disk_5.absorb(disk_6)
    print(disk_7)
    print(disk_7.area)
    disk_8 = Disk()
    print(disk_8)
    disk_8.change_radius(7)
    print(disk_8.absorb(disk_7))