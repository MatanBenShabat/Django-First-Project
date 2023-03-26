from django.urls import reverse
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string

# Create your views here.


monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Meditate for at least 10 minutes every day!",
    "may": "Read at least one book every week!",
    "june": "Try a new hobby or activity every week!",
    "july": "Eat a new type of fruit or vegetable every day!",
    "august": "Write a journal entry every day!",
    "september": "Drink at least 8 glasses of water every day!",
    "october": "Do a random act of kindness every day!",
    "november": "Learn a new language for at least 20 minutes every day!",
    "december": None
}


def index(request):
    months = list(monthly_challenges.keys())
    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    # response_data = f"<ul>{list_items}</ul>"

    # return HttpResponse(response_data)
    return render(request, "challenges/index.html", {"months": months})


def monthly_challenge_by_number(request, month):
    if month > 12 or month <= 0:
        return HttpResponseNotFound("Invalid month!")

    months = list(monthly_challenges.keys())
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {"text": challenge_text, "month_name": month})
    except:
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
        raise Http404()
