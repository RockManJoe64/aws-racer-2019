import unittest
from hypothesis import given
import hypothesis.strategies as st
from rewardfunctions import nascar_8_bit


class RewardFunctionTests(unittest.TestCase):
    # Returns True or False.
    def test(self):
        self.assertTrue(True)

    @given(st.integers(1, 4))
    def test_speed_on_track(self, speed):
        params = {
            "all_wheels_on_track": True,
            "speed": speed,
            "waypoints": [[0, 0], [5, 0]],
            "closest_waypoints": [0, 1],
            "heading": -180,
        }
        reward = nascar_8_bit(params)
        self.assertGreaterEqual(reward, 10, "Failed when speed at %d" % speed)


if __name__ == '__main__':
    unittest.main()
