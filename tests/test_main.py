import pytest
from unittest.mock import patch
from main import app, main


@pytest.fixture
def client():
    """Fixture providing a Flask test client for testing endpoints."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index_route(client):
    """Verifies that index page renders correctly with premium web dashboard structure."""
    response = client.get("/")
    assert response.status_code == 200
    html_content = response.data.decode("utf-8")
    assert "Flask 控制中心" in html_content
    assert "19191" in html_content


def test_feature1_route(client):
    """Verifies that morning stocks page renders correctly."""
    response = client.get("/feature1")
    assert response.status_code == 200
    html_content = response.data.decode("utf-8")
    assert "晨間自選股看盤" in html_content
    assert "2330.TW" in html_content
    assert "NVDA.US" in html_content


def test_feature2_route(client):
    """Verifies that afternoon company page renders correctly."""
    response = client.get("/feature2")
    assert response.status_code == 200
    html_content = response.data.decode("utf-8")
    assert "下午上班公司工作站" in html_content
    assert "艾克美科技" in html_content
    assert "Scrum" in html_content



def test_health_route(client):
    """Verifies the health status API returns standard healthy JSON status."""
    response = client.get("/api/health")
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["success"] is True
    assert json_data["data"]["status"] == "healthy"


def test_greet_route_success(client):
    """Verifies that greet POST endpoint sanitizes input and returns correct greeting."""
    response = client.post(
        "/api/greet",
        json={"name": "  Antigravity-123!@# "}
    )
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["success"] is True
    # Sanitized "  Antigravity-123!@# " -> "Antigravity-123"
    assert "Antigravity-123" in json_data["message"]
    assert json_data["data"]["sanitized_name"] == "Antigravity-123"


def test_greet_route_empty_payload(client):
    """Verifies that greet endpoint defaults gracefully if no request payload is provided."""
    response = client.post("/api/greet", json={})
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["success"] is True
    assert "World" in json_data["message"]


def test_greet_route_invalid_json(client):
    """Verifies that greet endpoint handles invalid or empty body payloads gracefully."""
    response = client.post("/api/greet", data="not json", content_type="application/json")
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["success"] is True
    assert "World" in json_data["message"]


def test_greet_route_internal_error(client):
    """Verifies that the API handles errors gracefully returning a standard 500 JSON error."""
    with patch("main.sanitize_name", side_effect=Exception("Database connection failure")):
        response = client.post("/api/greet", json={"name": "CrashTest"})
        assert response.status_code == 500
        json_data = response.get_json()
        assert json_data["success"] is False
        assert "Internal server error" in json_data["message"]


def test_main_server_run():
    """Verifies that the application main bootstrapper initiates server execution."""
    with patch.object(app, "run") as mock_run:
        exit_code = main()
        assert exit_code == 0
        mock_run.assert_called_once_with(host="0.0.0.0", port=19191, debug=False)


def test_main_server_fail():
    """Verifies that server boot crashes are caught and return a status code of 1."""
    with patch.object(app, "run", side_effect=RuntimeError("Address already in use")):
        exit_code = main()
        assert exit_code == 1
