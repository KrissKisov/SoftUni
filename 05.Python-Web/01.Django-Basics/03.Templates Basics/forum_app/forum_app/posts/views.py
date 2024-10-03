from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    context = {
        "current_time": datetime.now().time(),
        "the_date_is": {
            "month": datetime.now().strftime('%B'),
            "the_day_is": datetime.now().day,
        },
        "some_text": "this is some text, just for filtering purpose!",
        "users": ["John", "Briony", "Luis", "Jane", "Kevin"],
    }

    return render(request, 'base.html', context)


def dashboard(request):

    context = {
        "posts": [
            {
                "title": "<i>How to create django project?</i>",  # '<i>...</i>' markdown_tag in use here
                "author": "Kevin Jones",
                "content": "I **don't** know how to create django project.",  # '**...**' markdown_tag in use here
                "created_at": datetime.now(),
            },
            {
                "title": "<i>Who knows how create django project?</i>",  # '<i>...</i>' markdown_tag in use here
                "author": "David Mathews",
                "content": "I need someone to show me how to create django project.",
                "created_at": datetime.now(),
            },
            {
                "title": "<i>I'll show how to create django project!</i>",  # '<i>...</i>' markdown_tag in use here
                "author": "Millie Farris",
                "content": "",
                "created_at": datetime.now(),
            },
        ],
    }

    return render(request, 'posts/dashboard.html', context)
