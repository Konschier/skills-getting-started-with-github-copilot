import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app

# Snapshot of the seed data, captured once before any test mutates the in-memory store.
_original_activities = copy.deepcopy(activities)


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    activities.clear()
    activities.update(copy.deepcopy(_original_activities))
    yield
    activities.clear()
    activities.update(copy.deepcopy(_original_activities))
