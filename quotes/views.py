from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages

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
	import requests
	import json

	if request.method == 'POST':
		form = StockForm(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request, ("Stock has been added."))
			return redirect('add_stock')

	else:
		ticker = Stock.objects.all()  #takes everything in the db and calls it ticker
		output = []					  #empty list
		for ticker_item in ticker:    #loop through each ticker in db
			api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_6c36eb84289d4373b6609895281d26de")
			try:
				api = json.loads(api_request.content)  #load the api pull
				output.append(api)                     #append the api pull to output list
			except Exception as e:
				api = "Error..."

		return render(request, 'add_stock.html', {'ticker':ticker, 'output': output})

def delete(request, stock_id):
	item = Stock.objects.get(pk=stock_id)
	item.delete()
	messages.success(request, ("Stock has been deleted."))
	return redirect(delete_stock)

def delete_stock(request):  #passing in browsers request
	ticker = Stock.objects.all()  #takes everything in the db and calls it ticker
	return render(request, 'delete_stock.html', {'ticker':ticker})














