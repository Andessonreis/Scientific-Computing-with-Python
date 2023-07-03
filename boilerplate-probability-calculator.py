import copy
import random
from unittest import main

# Hat class
class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents += [color] * count

    def draw(self, num_balls):
        drawn_balls = []
        if num_balls >= len(self.contents):
            return self.contents
        for _ in range(num_balls):
            ball_index = random.randint(0, len(self.contents) - 1)
            drawn_balls.append(self.contents.pop(ball_index))
        return drawn_balls

# Experiment function
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        success = True
        for color, count in expected_balls.items():
            if drawn_balls.count(color) < count:
                success = False
                break
        if success:
            success_count += 1
    return success_count / num_experiments

# Main code
if __name__ == '__main__':
    random.seed(95)
    hat = Hat(blue=4, red=2, green=6)
    probability = experiment(
        hat=hat,
        expected_balls={"blue": 2, "red": 1},
        num_balls_drawn=4,
        num_experiments=3000
    )
    print("Probability:", probability)

    # Run unit tests automatically
    main(module='test_module', exit=False)
