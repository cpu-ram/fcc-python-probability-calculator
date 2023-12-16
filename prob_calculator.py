from functools import reduce
import copy
import random


class Hat:
    contents = []
    data = []

    def __init__(self, **kwargs):
        self.data = kwargs
        self.contents = reduce((
            lambda x, y:
                x.append(str(y)*self.data[str(y)])),
            vars(self.data).keys(),
            self.contents
        )

    def draw(self, n):
        result = []

        if n < 1:
            raise ValueError()
        if n > len(self.data):
            return self.contents

        contentsCopy = copy.deepcopy(self.contents)
        while len(contentsCopy) > 0:
            randomNumber = random.randrange(0, len(contentsCopy))
            element = contentsCopy.pop(randomNumber)
            result += element
        return result


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    matchesFound = 0

    draws = []
    for index in range(0, num_experiments):
        draws.append(hat.draw(num_balls_drawn))

        def arrayToDict():
            return reduce(
                lambda x, y:
                    x.update({'y': x['y']+1}) if hasattr(x,
                                                         'y') else x.update('y', 1),
                draws,
                {}
            )
        drawsDict = map(arrayToDict, draws)
        expected_color_names = expected_balls
        for element in drawsDict:
            if set(vars(element).keys()) == set(vars(expected_balls).keys()):
                pass
