from random import random
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import LoginForm, UploadCSVForm
from .models import WinningNumbers, LosingNumbers, Players
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



    # Winning team's numbers
    win_nums = WinningNumbers.objects.values()[0]
    # Turn dictionary into a list to better output into the HTML table
    win_nums = [value for key, value in win_nums.items()]
    # Remove the first number as it's just the ID
    win_nums = win_nums[1:]

    # Losing team's numbers
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

        # Get total users and post scores
        # First grab a list of all players
        players = []
        for row in pool:
            for key, value in row.items():
                if value not in players:
                    players.append(value)
                    Players.objects.update_or_create(player=value)

        # Grab player score details
        player_scores = Players.objects.all().values_list(
            'player',
            'first_round',
            'second_round',
            'sweet_sixteen',
            'elite_eight',
            'final_four',
            'championship'
        )

        return render(request, 'squares/homepage.html', {
            'los_num_plus_pool': los_num_plus_pool,
            'win_nums': win_nums,
            'los_nums': los_nums,
            'player_scores': player_scores
        })
    except:
        return render(request, 'squares/homepage.html', {
            'message': 'Something went wrong. Cannot find CSV file.'
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
    return redirect('homepage')


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


def directions(request):
    return render(request, 'squares/directions.html')