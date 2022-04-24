import json
import pytest
from app.app import create_app
from app.data.task import TASKS

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_add_new_task(client):
    response = client.post("/task", json={"name": "吃早餐"});
    task = json.loads(response.data)
    assert task.get('name')  == "吃早餐"

def test_list_all_tasks(client):
    response = client.post("/task", json={"name": "吃午餐"});
    response = client.post("/task", json={"name": "吃晚餐"});
    response = client.post("/task", json={"name": "吃宵夜"});
    response = client.get("/task")
    tasks = json.loads(response.data)
    assert len(tasks) == 4

def test_search_task_by_id(client):
    response = client.post("/task", json={"name": "吃晚餐"});
    response = client.get("/task/2");
    task = json.loads(response.data)
    assert task.get('id') == 2 and task.get("name") == "吃晚餐" and task.get("status") == 0

def test_del_task_by_id(client):
    response = client.delete("/task/1");
    assert json.loads(response.data) == ""

def test_update_task_by_id(client):
    response = client.put("/task/0", json={"name": "吃早午餐", "status": 1});
    task = json.loads(response.data)
    assert task.get('status') == '1' and task.get("name") == "吃早午餐" 

