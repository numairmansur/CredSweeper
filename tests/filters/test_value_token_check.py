import pytest

from credsweeper.filters import ValueTokenCheck
from tests.filters.conftest import LINE_VALUE_PATTERN
from tests.test_utils.dummy_line_data import get_line_data


class TestValueTokenCheck:

    def test_value_token_check_p(self, file_path: pytest.fixture, success_line: pytest.fixture) -> None:
        line_data = get_line_data(file_path, line=success_line, pattern=LINE_VALUE_PATTERN)
        assert ValueTokenCheck().run(line_data) is False

    @pytest.mark.parametrize("line", ["Crac;crackle1", "my password", "my)password"])
    def test_value_token_check_n(self, file_path: pytest.fixture, line: str) -> None:
        line_data = get_line_data(file_path, line=line, pattern=LINE_VALUE_PATTERN)
        assert ValueTokenCheck().run(line_data) is True

    def test_value_token_check_none_value_n(self, file_path: pytest.fixture, success_line: pytest.fixture) -> None:
        line_data = get_line_data(file_path, line=success_line)
        assert ValueTokenCheck().run(line_data) is True
