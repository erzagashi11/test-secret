import sys

from weather.forecast import format_summary, load_days, summarize


def main(argv):
    path = argv[1] if len(argv) > 1 else "data/forecast.json"
    try:
        print(format_summary(summarize(load_days(path))))
    except (OSError, ValueError, KeyError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
