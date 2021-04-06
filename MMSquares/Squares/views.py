from random import random
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm, UploadCSVForm
from .models import WinningNumbers, LosingNumbers
from .helpers import random_numbers
import pandas as pd
from django.contrib import messages



def homepage(request):
    if request.method == 'POST' and 'new_numbers' in request.POST:
        # Get new winning team numbers
        winning_numbers = random_numbers()
        # Get losing team numbers
        losing_numbers = random_numbers()

        # Update WinningNumbers model
        WinningNumbers.objects.filter(id=1).update(
            spot1=winning_numbers[0],
            spot2=winning_numbers[1],
            spot3=winning_numbers[2],
            spot4=winning_numbers[3],
            spot5=winning_numbers[4],
            spot6=winning_numbers[5],
            spot7=winning_numbers[6],
            spot8=winning_numbers[7],
            spot9=winning_numbers[8],
            spot10=winning_numbers[9],
        )
        # Save WinningNumbers model
        for item in WinningNumbers.objects.filter(id=1):
            item.save()

        # Update LosingNumbers model
        LosingNumbers.objects.filter(id=1).update(
            spot1=losing_numbers[0],
            spot2=losing_numbers[1],
            spot3=losing_numbers[2],
            spot4=losing_numbers[3],
            spot5=losing_numbers[4],
            spot6=losing_numbers[5],
            spot7=losing_numbers[6],
            spot8=losing_numbers[7],
            spot9=losing_numbers[8],
            spot10=losing_numbers[9],
        )
        # Save LosingNumbers model
        for item in LosingNumbers.objects.filter(id=1):
            item.save()



    # Winning team's numbers saved in database
    win_nums = WinningNumbers.objects.values()[0]
    # Turn dictionary into a list to better output into the HTML table
    win_nums = [value for key, value in win_nums.items()]
    # Remove the first number as it's just the ID
    win_nums = win_nums[1:]

    # Losing team's numbers saved in database
    los_nums = LosingNumbers.objects.values()[0]
    # Turn dictionary into a list to better output into the HTML table
    los_nums = [value for key, value in los_nums.items()]
    # Remove the first number as it's just the ID
    los_nums = los_nums[1:]


    # Do the following on both GET and POST method
    try:
        # Read in the CSV without headers
        pool = pd.read_csv(r'C:\Users\chizj\OneDrive\Coding\March Madness Squares\MMSquares\csv_files\squares.csv', header=None)
        # Turn into a dictionary - orient='records' is so the key/values are row/columns so it outputs correctly by row in html
        pool = pool.to_dict(orient='records')

        # Zip both los_nums with pool initials - needs to be a tuple to output in readable format
        los_num_plus_pool = tuple(zip(los_nums, pool))

        return render(request, 'squares/homepage.html', {
            'los_num_plus_pool': los_num_plus_pool,
            'win_nums': win_nums,
            'los_nums': los_nums
        })
    except:
        return render(request, 'squares/homepage.html', {
            'message': 'Something went wrong. Cannot find CSV file.'
        })


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            # Login the user
            login(request, user)
            messages.success(request, "New Admin created.")
            # Upon logging the user in redirect them to the homepage
            return redirect('homepage')
        messages.error(request, "Unsuccessful registration. Invalid infromation.")
    # If method == GET
    return render(request, 'squares/register.html', {
        'form': RegisterForm()
    })


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # Authenticate the user
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    # If method == GET
    return render(request, 'squares/login.html', {
        'form': LoginForm()
    })


def logout_user(request):
    # Logout user and return to homepage
    logout(request)
    return render(request, 'squares/homepage.html')


def upload(request):
    if request.method == 'POST':
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            # Save CSV file
            form.save()
            return HttpResponseRedirect('/')
    else:
        return render(request, 'squares/upload.html', {
            'form': UploadCSVForm()
        })
