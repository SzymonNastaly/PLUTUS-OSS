from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

# sample company data
company_data = """{"name": "TEST 1 AG", "ticker": "T1A.DE", "current_liab": 1000000, "equity": 1000000,
                 "total_assets": 1000000, "revenue12": 1000000, "revenue13": 1000000, "revenue14": 1000000,
                 "revenue15": 1000000, "revenue16": 1000000, "ebit": -1000000, "netincome12": 1000000, 
                 "netincome13": -1000000, "netincome14": -1000000, "netincome15": -1000000, "netincome16": -1000000, 
                 "free_cashflow": -110000, "eps12": 1.00, "eps13": -0.10, "eps14": 1.00, "eps15": 1.00, 
                 "eps16": 1.00, "eps_e": 1.00, "total_dividend": 0, "dividend_ps": 0.0}"""

new_company_data = """{"name": "TEST 2 AG", "ticker": "T2A.DE", "current_liab": 1000000, "equity": 1000000,
                 "total_assets": 1000000, "revenue12": 1000000, "revenue13": 1000000, "revenue14": 1000000,
                 "revenue15": 1000000, "revenue16": 1000000, "ebit": -1000000, "netincome12": 1000000, 
                 "netincome13": -1000000, "netincome14": -1000000, "netincome15": -1000000, "netincome16": -1000000, 
                 "free_cashflow": -1000000, "eps12": 1.00, "eps13": -0.10, "eps14": 1.00, "eps15": 1.00, 
                 "eps16": 1.00, "eps_e": 1.00, "total_dividend": 0, "dividend_ps": 0.0}"""



class TodoListAPIViewTestCase(APITestCase):
    """Testing the functionality of the list API view"""

    def setUp(self):
        self.username = "testadmin"
        self.email = "test@admin.com"
        self.password = "you_know_nothing"
        self.user = User.objects.create_superuser(self.username, self.email, self.password)
        self.token, created = Token.objects.get_or_create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_company(self):
        """Testing creation with admin account"""
        response = self.client.post("/stock/", data=company_data, content_type="application/json")

        self.assertEqual(201, response.status_code)
        self.assertEqual(eval(company_data)["name"], response.data["name"])
        # TODO: Is this eval safe?


class StockDetailAPIViewTestCase(APITestCase):
    """Testing the functionality of the detail API view"""

    def setUp(self):
        self.username = "testadmin"
        self.email = "test@admin.com"
        self.password = "you_know_nothing"
        self.user = User.objects.create_superuser(self.username, self.email, self.password)
        self.token, created = Token.objects.get_or_create(user=self.user)
        self.api_authentication()
        response = self.client.post("/stock/", data=company_data, content_type="application/json")

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_company(self):
        """Testing company retrieve with non-admin account"""
        new_user = User.objects.create_user("newuser", "user@email.com", "newpass")
        new_token, created = Token.objects.get_or_create(user=new_user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(new_token))
        response = self.client.get("/stock/3", follow=True)

        self.assertEqual(200, response.status_code)
        self.assertEqual(eval(company_data)["name"], response.data["name"])

    def test_edit_company_authorization(self):
        """Testing company edit with non-admin account (not allowed)"""
        new_user = User.objects.create_user("newuser", "user@email.com", "newpass")
        new_token, created = Token.objects.get_or_create(user=new_user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(new_token))
        response = self.client.put("/stock/3/", data=company_data, content_type="application/json")

        self.assertEqual(403, response.status_code)
        self.assertEqual("permission_denied", response.data["detail"].code)

    def test_edit_company(self):
        """Testing company edit with admin account (allowed)"""
        response = self.client.put("/stock/1/", data=new_company_data, content_type="application/json")

        self.assertEqual(200, response.status_code)
        self.assertEqual(eval(new_company_data)["name"], response.data["name"])

# TODO: Teardown method
