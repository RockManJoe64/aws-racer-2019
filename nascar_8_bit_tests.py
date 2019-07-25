import unittest
from rewardfunctions import nascar_8_bit


class RewardFunctionTests(unittest.TestCase):
    def setUp(self):
        self.params = {
            "all_wheels_on_track": True,
            "speed": 3,
            "waypoints": [[5, 0], [0, 0]],
            "closest_waypoints": [0, 1],
            "heading": 180,
        }

    def test_speed_on_track_increasing_reward(self):
        for speed in range(3, 5):
            with self.subTest(speed=speed):
                self.params["speed"] = speed
                reward = nascar_8_bit(self.params)
                self.assertGreaterEqual(reward, 20, "speed=%d" % speed)

    def test_speed_on_track_decreasing_reward(self):
        for speed in [1, 2]:
            with self.subTest(speed=speed):
                self.params["speed"] = speed
                reward = nascar_8_bit(self.params)
                self.assertLessEqual(reward, 10, "speed=%d" % speed)

    def test_heading_on_track_increasing_reward(self):
        for heading in [170, 180, 190]:
            with self.subTest(heading=heading):
                self.params["heading"] = heading
                reward = nascar_8_bit(self.params)
                self.assertGreaterEqual(reward, 20, "heading=%d" % heading)

    def test_heading_on_track_decreasing_reward(self):
        for heading in [160, 200]:
            with self.subTest(heading=heading):
                self.params["heading"] = heading
                reward = nascar_8_bit(self.params)
                self.assertLessEqual(reward, 10, "heading=%d" % heading)


if __name__ == '__main__':
    unittest.main()
