from database import database_toko

class ProductService:
    def fetchProducts(self):
        result = db_object.fetch_data(f"SELECT * FROM Products")
        return result
    
    def fetchProductById(self, id):
        query = """
        SELECT * FROM Products WHERE user_id = %s
        """

        value = (id,)

        result = db_object.fetch_data(query, value)

     

product_services = ProductService()