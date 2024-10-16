from unittest.mock import MagicMock, patch

import pytest

from definition_project.main import main, merge_silver, process_args


@patch('definition_project.main.DeltaTable')
def test_merge_silver(mock_delta_table):
    pass


def test_process_args():
    pass


@patch('definition_project.main.SparkSession')
@patch('definition_project.main.merge_silver')
def test_main(mock_merge_silver, mock_spark_session):
    pass
