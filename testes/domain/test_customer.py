from src.domain.customer import Customer


# Instancia e testa o customer
def test_should_create_customer():
    customer = Customer(name="Douglas", email="bressar@bessar.com") # cria o dicionário
    
    # validação
    assert customer.name == "Douglas"
    assert customer.email == "bressar@bessar.com"   
    #print(customer.model_dump()) # for debug