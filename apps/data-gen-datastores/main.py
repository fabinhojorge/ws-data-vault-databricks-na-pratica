from src.objects import users, rides, payments
from src.api import api_requests

urls = {
    "users": "https://random-data-api.com/api/users/random_user",
    "credit_card": "https://random-data-api.com/api/business_credit_card/random_card",
    "subscription": "https://random-data-api.com/api/subscription/random_subscription",
    "stripe": "https://random-data-api.com/api/stripe/random_stripe",
    "google_auth": "https://random-data-api.com/api/omniauth/google_get",
    "linkedin_auth": "https://random-data-api.com/api/omniauth/linkedin_get",
    "apple_auth": "https://random-data-api.com/api/omniauth/apple_get"
}

params = {
    "size": 100
}

users = users.Users()
rides = rides.Rides()
payments = payments.Payments()

print(users.get_multiple_rows(10))
print(rides.get_multiple_rows(10))
print(payments.get_multiple_rows(10))

api = api_requests.Requests()
print(api.api_get_request(urls["users"], params))
print(api.api_get_request(urls["credit_card"], params))
print(api.api_get_request(urls["subscription"], params))
print(api.api_get_request(urls["stripe"], params))
print(api.api_get_request(urls["google_auth"], params))
print(api.api_get_request(urls["linkedin_auth"], params))
print(api.api_get_request(urls["apple_auth"], params))
