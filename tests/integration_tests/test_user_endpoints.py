

def test_delete_user_success(testing_app, valid_user_delete_id):
    response = testing_app.delete(f"/user/{valid_user_delete_id}")
    assert response.status_code == 200
    
def test_double_delete_user_fail(testing_app, valid_user_delete_id):
    response = testing_app.delete(f"/user/{valid_user_delete_id}")
    assert response.status_code == 200
    second_response = testing_app.delete(f"/user/{valid_user_delete_id}")
    assert second_response.status_code == 404
    assert second_response.json() == "User doesn't exist"

def test_invalid_user_id_fails(testing_app, invalid_user_delete_id):
    response = testing_app.delete(f"/user/{invalid_user_delete_id}")
    assert response.status_code == 404
    assert response.json() == "User doesn't exist"

def test_put_user_returns_correct_results(testing_app, sample_full_user_profile):
    user_id = 1
    response = testing_app.put(f"/user/{user_id}", json=sample_full_user_profile.model_dump())
    assert response.status_code == 200

def test_put_user_twice_returns_correct_results(testing_app, sample_full_user_profile):
    user_id = 1
    response = testing_app.put(f"/user/{user_id}", json=sample_full_user_profile.model_dump())
    assert response.status_code == 200

    second_response = testing_app.put(f"/user/{user_id}", json=sample_full_user_profile.model_dump())
    assert second_response.status_code == 200

