import json


def test_add_new_task(client):
    response = client.post("/task", json={"name": "吃早餐"});
    task = json.loads(response.data)
    assert task.get('name')  == "吃早餐"

def test_search_task_by_id(client):
    response = client.get("/task/0");
    task = json.loads(response.data)
    assert task.get('id') == 0

def test_update_task_by_id(client):
    response = client.put("/task/0", json={"name": "吃早餐", "status": 1});
    task = json.loads(response.data)
    assert task.get('status') == '1'

def test_list_all_tasks(client):
    response = client.get("/task")
    tasks = json.loads(response.data)
    assert len(tasks) == 1

def test_del_task_by_id(client):
    response = client.delete("/task/0");
    assert json.loads(response.data) == ""