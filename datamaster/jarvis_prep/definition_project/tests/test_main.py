from unittest.mock import MagicMock, patch

import pytest

from definition_project.new import main, merge_silver, process_args


@patch('definition_project.new.DeltaTable')
def test_merge_silver(mock_delta_table):
    pass


def test_process_args():
    pass


@patch('definition_project.new.SparkSession')
@patch('definition_project.new.merge_silver')
def test_main(mock_merge_silver, mock_spark_session):
    pass
