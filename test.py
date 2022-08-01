import pytest
from main import check_document_existance
from main import add_new_shelf
from yand import create_folder
@pytest.mark.parametrize(
    "number, ex_result",
    [
        ("2207 876234", True),
        ("11-2", True),
        ("10006", True),
        ("2344324", False),
        ("fwcs34", False)
    ]
)
def test_check_document_existance(number, ex_result):
    result = check_document_existance(number)
    assert result == ex_result


@pytest.mark.parametrize(
    "shelf, expected_res",
    [
        ("4", ("4", True)),
        ("5", ("5", True)),
        ("3", ("3", False))
    ]
)
def test_add_new_shelf(shelf, expected_res):
    actual_res = add_new_shelf(shelf)
    assert actual_res == expected_res

@pytest.mark.parametrize(
    "name, status_code",
    [
        ("FOLDER", 201),
        ("NAME", 201),
        ("NAME", 409)
    ]
)
def test_create_folder(name, status_code):
    actual_result = create_folder(name)
    assert actual_result == status_code
