from urllib.parse import urlparse
from pathlib import Path
import aocd


def fetch_input_example(year, day):
    data = aocd.get_data(day=day, year=year)
    if data.startswith("Puzzle inputs differ"):
        raise RuntimeError("Unable to fetch puzzle input, check session exists")
    return data


if __name__ == "__main__":
    get_base_url = input("Enter day url: ")

    year, _, day = urlparse(get_base_url).path.split("/")[1:]
    day = int(day)
    year = int(year)

    basepath = Path(f"./{year}/{day:02}")
    basepath.mkdir(parents=True, exist_ok=True)

    with open(f"{basepath}/advent_{year}_{day:02}.py", "w") as newfile:
        pass

    with open(f"{basepath}/test_advent_{year}_{day:02}.py", "w") as newfile:
        pass

    with open(f"{basepath}/advent_{year}_{day:02}_input.txt", "w") as newfile:
        newfile.write(fetch_input_example(year=year, day=day))
