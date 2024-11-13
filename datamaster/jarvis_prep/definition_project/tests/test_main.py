from unittest.mock import MagicMock, patch

import pytest

from definition_project.main import main


@patch('definition_project.main.SparkSession')
@patch('definition_project.main.merge_silver')
def test_main(mock_merge_silver, mock_spark_session):
    pass
