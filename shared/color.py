import inspect


class Color:
    white = (255, 255, 255)
    black = (0, 0, 0)
    yellow = (255, 255, 0)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    purple = (128, 0, 128)
    green = (0, 128, 0)
    orange = (255, 165, 0)
    brown = (165, 42, 42)
    silver = (192, 192, 192)
    grey = (128, 128, 128)

    # just color RGBs not name
    @staticmethod
    def all():
        temp = []
        for i in inspect.getmembers(Color):
            if not i[0].startswith('_') and not i[0] == 'all':

                temp.append(i[1])
        return temp
