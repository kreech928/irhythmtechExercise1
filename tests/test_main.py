import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import logging
from src.app.main import monitor_v_temp
from fixtures.dmm_dumies import *


def test_within_threshold_constant():
    result = monitor_v_temp(threshold=0.1, i=3, interval=0, dmm=DummyDMMConstant())
    assert result is True


def test_exceeds_threshold_constant(caplog):
    with caplog.at_level(logging.INFO):
        result = monitor_v_temp(threshold=0.5, i=1, interval=0, dmm=DummyDMMThresholdExceeded())
    assert result is False
    assert any(rec.levelno == logging.ERROR for rec in caplog.records)


def test_many_iterations_random_close():
    dmm = DummyDMMRandomClose(seed=999)
    result = monitor_v_temp(threshold=0.2, i=50, interval=0, dmm=dmm)
    assert result is True


def test_many_iterations_random_correlated():
    dmm = DummyDMMRandomCorrelated(seed=42, window=0.03)
    result = monitor_v_temp(threshold=0.05, i=150, interval=0, dmm=dmm)
    assert result is True