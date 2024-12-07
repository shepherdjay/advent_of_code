from hypothesis import strategies as st


@st.composite
def positive_example(draw, max_size: int, min_value: int = 1) -> tuple[int, list[int]]:
    values = draw(
        st.lists(st.integers(min_value=min_value, max_value=1000), min_size=2, max_size=max_size)
    )
    total = values[0]
    for n in values[1:]:
        match draw(st.sampled_from(["multiply", "add"])):
            case "multiply":
                total *= n
            case "add":
                total += n

    return total, values


@st.composite
def negative_example(draw: st.DrawFn, max_size: int) -> tuple[int, list[int]]:
    _, values = draw(positive_example(max_size=max_size, min_value=2))
    total = draw(st.sampled_from(values))

    return total, values


@st.composite
def full_report(draw: st.DrawFn, max_size_per_example: int, max_report_size: int) -> str:
    positive_examples = []
    negative_examples = []
    report = []

    report_size = draw(st.integers(min_value=1, max_value=max_report_size))
    for _ in range(report_size):
        match draw(st.sampled_from(["positive", "negative"])):
            case "positive":
                example = draw(positive_example(max_size=max_size_per_example))
                positive_examples.append(example)
            case "negative":
                example = draw(negative_example(max_size=max_size_per_example))
                negative_examples.append(example)
        report.append(example)

    puzzle_input = ""
    for total, value_list in report:
        puzzle_input += f"{total}: {' '.join([str(x) for x in value_list])}\n"

    expected_result = sum([x for x, _ in positive_examples])

    return expected_result, puzzle_input
