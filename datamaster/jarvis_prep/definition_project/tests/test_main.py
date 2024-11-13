from unittest.mock import MagicMock, patch

import pytest

from definition_project.main import main


@patch('definition_project.main.SparkSession')
def test_main(mock_spark_session):
    pass
