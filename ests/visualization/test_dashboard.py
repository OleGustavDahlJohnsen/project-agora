"""
Project Agora: Unit Tests for Visualization Systems
"""
import pytest
from src.visualization.dashboard import Dashboard

# Mock matplotlib to prevent it from creating a GUI window during tests
@pytest.fixture(autouse=True)
def mock_matplotlib(mocker):
    mocker.patch('matplotlib.pyplot.ion')
    mocker.patch('matplotlib.pyplot.subplots')
    mocker.patch('matplotlib.pyplot.pause')

def test_dashboard_data_handling():
    """
    Tests that the Dashboard class correctly appends new data to its
    history lists. Does not test the visual plot itself.
    """
    dashboard = Dashboard()
    
    assert len(dashboard.day_history) == 0
    assert len(dashboard.wellbeing_history) == 0

    # Simulate an update
    world_state_1 = {"day": 1, "user_wellbeing": 7.5, "project_progress": 25.0}
    dashboard.update(world_state_1)

    assert len(dashboard.day_history) == 1
    assert dashboard.day_history[0] == 1
    assert dashboard.wellbeing_history[0] == 7.5

    # Simulate another update
    world_state_2 = {"day": 2, "user_wellbeing": 7.8, "project_progress": 25.5}
    dashboard.update(world_state_2)

    assert len(dashboard.day_history) == 2
    assert dashboard.day_history[1] == 2
    assert dashboard.wellbeing_history[1] == 7.8
