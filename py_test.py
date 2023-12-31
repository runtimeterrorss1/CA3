from app import app

def test_add():
    with app.test_client() as client:
        response = client.get('calc/add/4/2')
        assert response.get_data(as_text=True) == '6'

def test_div():
    with app.test_client() as client:
        response = client.get('calc/div/6/3')
        assert response.get_data(as_text=True) == '2.0'

def test_multiply():
    with app.test_client() as client:
        response = client.get('calc/mul/2/3')
        assert response.get_data(as_text=True) == '6'

        response = client.get('calc/mul/1/2')
        assert response.get_data(as_text=True) == '2'