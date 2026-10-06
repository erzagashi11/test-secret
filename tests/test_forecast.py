import unittest

from weather.forecast import format_summary, summarize


class SummarizeTests(unittest.TestCase):
    DAYS = [
        {"temp_c": 12, "rain_mm": 0},
        {"temp_c": 18, "rain_mm": 3.5},
        {"temp_c": 15, "rain_mm": 1},
    ]

    def test_min_max_average(self):
        summary = summarize(self.DAYS)
        self.assertEqual((summary["min"], summary["max"], summary["avg"]), (12, 18, 15.0))

    def test_counts_rainy_days(self):
        self.assertEqual(summarize(self.DAYS)["rainy_days"], 2)

    def test_empty_forecast_is_an_error(self):
        with self.assertRaises(ValueError):
            summarize([])

    def test_format(self):
        text = format_summary({"min": 1, "max": 9, "avg": 5.0, "rainy_days": 0})
        self.assertEqual(text, "Min 1 C, max 9 C, average 5.0 C, rainy days: 0")


if __name__ == "__main__":
    unittest.main()
