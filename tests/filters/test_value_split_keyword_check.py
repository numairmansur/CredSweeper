import pytest

from credsweeper.filters import ValueSplitKeywordCheck
from tests.filters.conftest import LINE_VALUE_PATTERN
from tests.test_utils.dummy_line_data import get_line_data


class TestValueSplitKeywordCheck:

    @pytest.mark.parametrize("line", ["abstract,and_so_on", "ani dammi lwnes", "unique#string"])
    def test_value_split_keyword_check_p(self, file_path: pytest.fixture, line: str) -> None:
        line_data = get_line_data(file_path, line=line, pattern=LINE_VALUE_PATTERN)
        assert ValueSplitKeywordCheck().run(line_data) is False

    @pytest.mark.parametrize("line", ["abstract and so on", "Any dummy lines", "unique string"])
    def test_value_split_keyword_check_n(self, file_path: pytest.fixture, line: str) -> None:
        line_data = get_line_data(file_path, line=line, pattern=LINE_VALUE_PATTERN)
        assert ValueSplitKeywordCheck().run(line_data) is True

    def test_value_split_keyword_check_none_value_n(self, file_path: pytest.fixture) -> None:
        line_data = get_line_data(file_path, line="")
        assert ValueSplitKeywordCheck().run(line_data) is True
