from datetime import date
from django.shortcuts import render


all_posts = [
    {
        "slug": "hike-in-the-mountains-v1",
        "image": "avocado1.png",
        "author": "Minh Tin",
        "date": date(2022, 1, 9),
        "title": "Mountains Hiking 1",
        "excerpt": " There's nothing like the views you get when hiking in the mountains 1!",
        "content": """
            One day at a cake shop, I met a man selling apples, For money he wanted to
            swap, But I really wanted some apelles. "Got any apelles?" asked I. "For
            that's how I'll spend my money." "No apelles here!" said the guy. He seemed
            to find it quite funny. "We've got some lovely cats, I'll give you a very
            fine price." "I'd rather have some ziggurats." The man blinked rapidly
            thrice. The man seemed exceptionally zany, And his manner was strangely
            amused. He wasn't what I would call brainy, Great disdain he noticeably
            oozed. Like others, he thought I was odd, Some say I'm a bit amazing. Still
            he gave me a courteous nod, As if he thought I was plenty blazing.

            One day at a cake shop, I met a man selling apples, For money he wanted to
            swap, But I really wanted some apelles. "Got any apelles?" asked I. "For
            that's how I'll spend my money." "No apelles here!" said the guy. He seemed
            to find it quite funny. "We've got some lovely cats, I'll give you a very
            fine price." "I'd rather have some ziggurats." The man blinked rapidly
            thrice. The man seemed exceptionally zany, And his manner was strangely
            amused. He wasn't what I would call brainy, Great disdain he noticeably
            oozed. Like others, he thought I was odd, Some say I'm a bit amazing. Still
            he gave me a courteous nod, As if he thought I was plenty blazing.

            One day at a cake shop, I met a man selling apples, For money he wanted to
            swap, But I really wanted some apelles. "Got any apelles?" asked I. "For
            that's how I'll spend my money." "No apelles here!" said the guy. He seemed
            to find it quite funny. "We've got some lovely cats, I'll give you a very
            fine price." "I'd rather have some ziggurats." The man blinked rapidly
            thrice. The man seemed exceptionally zany, And his manner was strangely
            amused. He wasn't what I would call brainy, Great disdain he noticeably
            oozed. Like others, he thought I was odd, Some say I'm a bit amazing. Still
            he gave me a courteous nod, As if he thought I was plenty blazing.
        """,
    },
    {
        "slug": "hike-in-the-mountains-v2",
        "image": "avocado2.png",
        "author": "James Loduca",
        "date": date(2022, 1, 9),
        "title": "UntilWeAllBelong Toolkit",
        "excerpt": " There's nothing like the views you get when hiking in the mountains 2!",
        "content": """
            One day at a cake shop, I met a man selling apples, For money he wanted to
            swap, But I really wanted some apelles. "Got any apelles?" asked I. "For
            that's how I'll spend my money." "No apelles here!" said the guy. He seemed
            to find it quite funny. "We've got some lovely cats, I'll give you a very
            fine price." "I'd rather have some ziggurats." The man blinked rapidly
            thrice. The man seemed exceptionally zany, And his manner was strangely
            amused. He wasn't what I would call brainy, Great disdain he noticeably
            oozed. Like others, he thought I was odd, Some say I'm a bit amazing. Still
            he gave me a courteous nod, As if he thought I was plenty blazing.

            One day at a cake shop, I met a man selling apples, For money he wanted to
            swap, But I really wanted some apelles. "Got any apelles?" asked I. "For
            that's how I'll spend my money." "No apelles here!" said the guy. He seemed
            to find it quite funny. "We've got some lovely cats, I'll give you a very
            fine price." "I'd rather have some ziggurats." The man blinked rapidly
            thrice. The man seemed exceptionally zany, And his manner was strangely
            amused. He wasn't what I would call brainy, Great disdain he noticeably
            oozed. Like others, he thought I was odd, Some say I'm a bit amazing. Still
            he gave me a courteous nod, As if he thought I was plenty blazing.

            One day at a cake shop, I met a man selling apples, For money he wanted to
            swap, But I really wanted some apelles. "Got any apelles?" asked I. "For
            that's how I'll spend my money." "No apelles here!" said the guy. He seemed
            to find it quite funny. "We've got some lovely cats, I'll give you a very
            fine price." "I'd rather have some ziggurats." The man blinked rapidly
            thrice. The man seemed exceptionally zany, And his manner was strangely
            amused. He wasn't what I would call brainy, Great disdain he noticeably
            oozed. Like others, he thought I was odd, Some say I'm a bit amazing. Still
            he gave me a courteous nod, As if he thought I was plenty blazing.
        """,
    },
    {
        "slug": "hike-in-the-mountains-v3",
        "image": "avocado3.png",
        "author": "Minh Tin",
        "date": date(2022, 1, 9),
        "title": "Mountains Hiking 3",
        "excerpt": " There's nothing like the views you get when hiking in the mountains 3!",
        "content": """
            One day at a cake shop, I met a man selling apples, For money he wanted to
            swap, But I really wanted some apelles. "Got any apelles?" asked I. "For
            that's how I'll spend my money." "No apelles here!" said the guy. He seemed
            to find it quite funny. "We've got some lovely cats, I'll give you a very
            fine price." "I'd rather have some ziggurats." The man blinked rapidly
            thrice. The man seemed exceptionally zany, And his manner was strangely
            amused. He wasn't what I would call brainy, Great disdain he noticeably
            oozed. Like others, he thought I was odd, Some say I'm a bit amazing. Still
            he gave me a courteous nod, As if he thought I was plenty blazing.

            One day at a cake shop, I met a man selling apples, For money he wanted to
            swap, But I really wanted some apelles. "Got any apelles?" asked I. "For
            that's how I'll spend my money." "No apelles here!" said the guy. He seemed
            to find it quite funny. "We've got some lovely cats, I'll give you a very
            fine price." "I'd rather have some ziggurats." The man blinked rapidly
            thrice. The man seemed exceptionally zany, And his manner was strangely
            amused. He wasn't what I would call brainy, Great disdain he noticeably
            oozed. Like others, he thought I was odd, Some say I'm a bit amazing. Still
            he gave me a courteous nod, As if he thought I was plenty blazing.

            One day at a cake shop, I met a man selling apples, For money he wanted to
            swap, But I really wanted some apelles. "Got any apelles?" asked I. "For
            that's how I'll spend my money." "No apelles here!" said the guy. He seemed
            to find it quite funny. "We've got some lovely cats, I'll give you a very
            fine price." "I'd rather have some ziggurats." The man blinked rapidly
            thrice. The man seemed exceptionally zany, And his manner was strangely
            amused. He wasn't what I would call brainy, Great disdain he noticeably
            oozed. Like others, he thought I was odd, Some say I'm a bit amazing. Still
            he gave me a courteous nod, As if he thought I was plenty blazing.
        """,
    },
]


def get_date(post):
    return post['date']

# Create your views here.


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]

    return render(request, 'blog/index.html', {
        "posts": latest_posts,
    })


def posts(request):
    return render(request, 'blog/all-posts.html', {
        "all_posts": all_posts,
    })


def post_detail(request, slug):
    indentified_post = next(post for post in all_posts if post['slug'] == slug)
    print(len(indentified_post))
    return render(request, 'blog/post-detail.html', {
        "post": indentified_post,
    })
