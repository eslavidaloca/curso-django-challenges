from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string #  render (line 1) does the same

# Create your views here.

# With these we would have to create a function for every month
# def january(request):
#     return HttpResponse("This works!")


# def february(request):
#     return HttpResponse("Sneak in your friend's house!")


# def march(request):
# return HttpResponse("Try getting a new job!")


def index(request):
    months = list(monthly_challenges.keys())
    
    # This was before the template render
    
    # Static form, not recommended
    # response_data = """
    #     <ul>
    #         <li><a href="/challenges/january">January</a></li>
    #     </ul>
    # """

    # Dinamic form
    # list_items = ""
    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    # response_data = f"<ul>{list_items}</ul>"

    # return HttpResponse(response_data)
    
    return render(request, "challenges/index.html", {
        "months": months
    })


monthly_challenges = {
    "january": "Eat at least 5 veggies this month",
    "february": "Play music!",
    "march": "Try getting a new job!",
    "april": "Finish a game!",
    "may": "Watch a movie!",
    "june": "Get jailed!",
    "july": "Listen to new music!",
    "august": "Save some money!",
    "september": "Get better at videogames!",
    "october": "Get in touch with old friends!",
    "november": "Search for a new car!",
    "december": None,
}


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    # return HttpResponseRedirect("/challenges/" + redirect_month) # Not dinamic, if we change the url in the urls.py file it breaks
    redirect_path = reverse(
        "month-challenge", args=[redirect_month])  # /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    # Without a dictionary with the months
    # if month == "january":
    #     challenge_text = "Eat at least 5 veggies this month"
    # elif month == "february":
    #     challenge_text = "Sneak in your friend's house!"
    # elif month == "march":
    #     challenge_text = "Try getting a new job!"
    # else:
    #     return HttpResponseNotFound("This month is not supported :(")
    try:
        challenge_text = monthly_challenges[month]
        # response_data = f"<h1>{challenge_text}</h1>" # Without a file for the view
        # return HttpResponse(challenge_text) #With this approach we only return plain text, not HTML

        # This is useless, is better to use render
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)

        # This will look for a folder named templates and then the path that we gave
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
    except:
        # Before Http404
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
        
        raise Http404() # This looks for our 404.html in the templates folder
