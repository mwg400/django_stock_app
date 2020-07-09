from django.shortcuts import render

# Create your views here.
def home(request):  #passing in browsers request
	import requests
	import json


	if request.method == 'POST':
		ticker = request.POST['ticker']
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_6c36eb84289d4373b6609895281d26de")

		try:
			api = json.loads(api_request.content)

		except Exception as e:
			api = "Error..."

		return render(request, 'home.html', {'api': api})

	else:
		return render(request, 'home.html', {'ticker': "Enter a ticker symbol above..."})

def about(request):  #passing in browsers request
	return render(request, 'about.html', {})

def add_stock(request):  #passing in browsers request
	return render(request, 'add_stock.html', {})