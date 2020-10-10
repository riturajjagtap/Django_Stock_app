from django.shortcuts import render, redirect
from .models import StockTickers
from django.contrib import messages
from .forms import StockForm
import requests
import json

def home(req):
    if req.method == 'POST':
        ticker = req.POST['ticker']
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_7180a15bddf846a783003d1849870568")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error.."
        return render(req, 'home.html', {'api':api})
    else:
        return render(req, 'home.html', {'ticker':"Enter a ticker symbol"})

def about(req):
    return render(req, 'about.html', {})

def add_stock(req):
    if req.method == 'POST':
        form = StockForm(req.POST or None)

        if form.is_valid():
            form.save()
            messages.success(req, 'Stock is added')
            return redirect('add_stock')

    else:
        ticker_data = StockTickers.objects.all()
        output = []
        for tick in ticker_data:
            api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(tick) + "/quote?token=pk_7180a15bddf846a783003d1849870568")
            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api = "Error.."

        return render(req, 'add_stock.html', {'ticker_data':ticker_data, 'output':output})

def delete_stock(req, stock_id):
    item = StockTickers.objects.get(pk=stock_id)
    item.delete()
    messages.success(req, 'Stock is deleted')
    return redirect('delete_stocks_page')

def delete_stocks_page(req):
    ticker_data = StockTickers.objects.all()
    return render(req, 'delete_stocks_page.html', {'ticker_data':ticker_data})
