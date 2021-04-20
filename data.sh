API_URL=http://localhost:8000

curl -d '{"title":"Ketchup", "description":"Bottle of ketchup"}' -H "Content-Type: application/json" -X POST $API_URL
curl -d '{"title":"Mustard", "description":"Jar of mustard"}' -H "Content-Type: application/json" -X POST $API_URL
curl -d '{"title":"Cheese", "description":"Big ball of cheese"}' -H "Content-Type: application/json" -X POST $API_URL