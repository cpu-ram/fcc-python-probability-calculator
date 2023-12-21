"""A naive probability calculator"""
from functools import reduce
import copy
import random


class Hat:
    """An abstraction representing the possible
    outcomes and their likely frequency for a single event"""
    contents = []
    data = {}

    def __init__(self, **kwargs):
        self.data = kwargs
        self.contents = reduce(
            lambda x, y: x + [str(y)] * self.data[str(y)],
            list(self.data.keys()),
            []
        )

    def draw(self, n):
        """method that returns n items randomly chosen from the ones stored"""
        result = []

        if n < 1:
            raise ValueError()
        if n > len(self.data):
            return self.contents

        contents_copy = copy.deepcopy(self.contents)
        while len(contents_copy) > 0:
            random_number = random.randrange(0, len(contents_copy))
            element = contents_copy.pop(random_number)
            result.append(element)
        return result


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """function that finds the probability of a specific
    combination of events under given conditions"""
    matches_found = 0

    draws = []
    for index in range(0, num_experiments):
        draws.append(hat.draw(num_balls_drawn))

        def array_to_dict():
            return reduce(
                lambda x, y:
                    x.update({'y': x['y'] + 1}) if hasattr(x,
                                                           'y') else x.update('y', 1),
                draws,
                {}
            )
        draws_dict = map(array_to_dict, draws)
        expected_color_names = expected_balls
        for element in draws_dict:
            if set(vars(element).keys()) == set(vars(expected_balls).keys()):
                pass
