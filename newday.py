from urllib.parse import urlparse
from pathlib import Path
import aocd

BASEPATH = Path(__file__).parent.resolve()

def fetch_input_example(session, year, day):
    data = aocd.get_data(session=session, day=day, year=year)
    return data


if __name__ == "__main__":
    get_base_url = input("Enter day url: ")

    year, _, day = urlparse(get_base_url).path.split("/")[1:]
    day = int(day)
    year = int(year)

    advent_path = Path(f"{BASEPATH}/advent_of_code/{year}/{day:02}")
    advent_path.mkdir(parents=True, exist_ok=True)

    with open(f"{advent_path}/day{day:02}.py", "w") as newfile:
        template_file = open(f'{BASEPATH}/templates/day.py.template').read()
        newfile.write(template_file)

    with open(f"{advent_path}/test_day{day:02}.py", "w") as newfile:
        pass
    with open(f'{BASEPATH}/.token') as infile:
        session = infile.read().strip()
    with open(f"{advent_path}/input.txt", "w") as newfile:
        newfile.write(fetch_input_example(session, year=year, day=day))
