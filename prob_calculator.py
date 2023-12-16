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

        contents_copy = copy.deepcopy(self.contents)
        while len(contents_copy) > 0:
            random_number = random.randrange(0, len(contents_copy))
            element = contents_copy.pop(random_number)
            result += element
        return result


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    matches_found = 0

    draws = []
    for index in range(0, num_experiments):
        draws.append(hat.draw(num_balls_drawn))

        def array_to_dict():
            return reduce(
                lambda x, y:
                    x.update({'y': x['y']+1}) if hasattr(x,
                                                         'y') else x.update('y', 1),
                draws,
                {}
            )
        draws_dict = map(array_to_dict, draws)
        expected_color_names = expected_balls
        for element in draws_dict:
            if set(vars(element).keys()) == set(vars(expected_balls).keys()):
                pass
