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
        while len(result) < n:
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

    def array_to_dict(arr):
        return reduce(
            lambda x, y: {**x, y:
                          x.get(y, 0) + 1},
            arr,
            {}
        )
    draws_dict = list(map(array_to_dict, draws))
    matching_draw_count = 0
    for element in draws_dict:
        if set(element.keys()) == set((expected_balls).keys()):
            matches_so_far = True
            for key in element.keys():
                if element[key] != expected_balls[key]:
                    matches_so_far = False
                    break
            if (matches_so_far):
                matching_draw_count += 1
    return matching_draw_count/num_experiments
