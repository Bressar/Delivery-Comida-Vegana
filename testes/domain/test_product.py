from src.domain.product import Product

# Instancia e testa o customer
def test_should_create_product():
    product = Product(
        name= "Feijoada", description="Feijoada Vegana", price=30
        ) 
    # validação do produto -> True/False
    assert product.name == "Feijoada"
    assert product.description == "Feijoada Vegana"
    assert product.price == 30.0
    #print(product.model_dump()) # for debug
    
    