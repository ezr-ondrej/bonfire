import pytest

from bonfire.utils import (
    split_equals,
    validate_time_string,
    get_version,
    hms_to_seconds
)


@pytest.mark.parametrize(
    "list_of_str, expected",
    [
        (
            ["t1=test1", "t2=test2"],
            {"t1": "test1", "t2": "test2"}
        ),
        (
            ["company=redhat", "team=Dev Prod"],
            {"company": "redhat", "team": "Dev Prod"}
        ),
    ]
)
def test_split_equals_pass(list_of_str, expected):
    result = split_equals(list_of_str)

    assert result == expected


@pytest.mark.parametrize(
    "list_of_str",
    [
        (
            ["t1 = test1", "t2 = test2"],
        ),
        (
            ["t1 test1", "t2 test2"],
        ),
    ]
)
def test_split_equals_fail(list_of_str: list):
    with pytest.raises(Exception):
        split_equals(list_of_str)


@pytest.mark.parametrize(
    "time, expected",
    [
        (
            "30m", "30m"
        ),
        (
            "1h45m", "1h45m"
        ),
        (
            "1h20s", "1h20s"
        ),
        (
            "2h15m32s", "2h15m32s"
        ),
    ]
)
def test_validate_time_string(time: str, expected: str):
    result = validate_time_string(time)

    assert result == expected


def test_get_version():
    result = get_version()

    assert result != "0.0.0"


@pytest.mark.parametrize(
    "seconds, expected",
    [
        (
            "1h", 3600
        ),
        (
            "45m", 2700
        ),
        (
            "65s", 65
        ),
        (
            "1h30m", 5400
        ),
    ]
)
def test_hms_to_seconds(seconds: str, expected: int):
    result = hms_to_seconds(seconds)

    assert result == expected