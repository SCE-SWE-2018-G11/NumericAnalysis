import CubicSpline
import unittest

x_values = [1, 2, 3, 4, 5]
y_values = [1, 2, 1, 1.5, 1]

class Test(unittest.TestCase):
    def test_cubicsplinederivatives(self):
        results = CubicSpline.CubicSplineDerivatives(x_values, y_values, 0, 0)
        expected_results = (0, -3.9642857, 3.8571429, -2.4642857, 0) # Taken from presentation slide 10
        self.assertEqual(len(results), len(expected_results))
        for i in range(len(results)):
            self.assertEqual(results[i], expected_results[i])

    def test_cubicspline(self):
        results = CubicSpline.NaturalCubicSpline(x_values, y_values)

        expected_results = (
            # Coefficients of polynomials for each range
            # Taken from presentation slide 11, and ran through WolframAlpha
            (0, -0.321429, 1.98214, -0.660714),
            (23.7142, -25.2499, 9.80353, -1.30357),
            (47.9285, -40.3927, 11.4107, -1.05357),
            (52.7852, -30.8925, 6.16065, -0.41071)
        )

        self.assertEqual(len(results), len(expected_results))
        for i in range(len(results)):
            self.assertEqual(len(results[i]), len(expected_results[i]))
            for j in range(len(results[i])):
                self.assertEqual(results[i][j], expected_results[i][j])

if __name__ == '__main__':
    unittest.main()
