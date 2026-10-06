"""Summarise a daily forecast stored as JSON."""

import json


def load_days(path):
    with open(path, encoding="utf-8") as handle:
        days = json.load(handle)
    if not isinstance(days, list):
        raise ValueError("forecast must be a JSON list of days")
    return days


def summarize(days):
    if not days:
        raise ValueError("forecast is empty")
    temperatures = [day["temp_c"] for day in days]
    return {
        "min": min(temperatures),
        "max": max(temperatures),
        "avg": round(sum(temperatures) / len(temperatures), 1),
        "rainy_days": sum(1 for day in days if day.get("rain_mm", 0) > 0),
    }


def format_summary(summary):
    return (
        f"Min {summary['min']} C, max {summary['max']} C, "
        f"average {summary['avg']} C, rainy days: {summary['rainy_days']}"
    )
