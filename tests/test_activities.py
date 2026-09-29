def test_get_activities_returns_success(client):
    # Arrange
    # (no setup needed beyond the seeded activities data)

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200


def test_get_activities_includes_known_activity_with_expected_shape(client):
    # Arrange
    activity_name = "Chess Club"

    # Act
    response = client.get("/activities")

    # Assert
    data = response.json()
    assert activity_name in data
    activity = data[activity_name]
    assert activity["description"] == "Learn strategies and compete in chess tournaments"
    assert activity["schedule"] == "Fridays, 3:30 PM - 5:00 PM"
    assert activity["max_participants"] == 12
    assert activity["participants"] == ["michael@mergington.edu", "daniel@mergington.edu"]
