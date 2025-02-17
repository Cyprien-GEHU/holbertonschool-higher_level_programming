#!/usr/bin/python3
"""
the programme will:
- fetch and print all title of the request
- fetch and save all id, title and body of a request into csv file
"""
import requests
import csv


def fetch_and_print_posts():
    """
    the function fetch_and_print_posts
    """
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code: {}".format(r.status_code))
    if r.status_code == 200:
        post = r.json()
        for data in post:
            print(data['title'])


def fetch_and_save_posts():
    """
    the function fetch_and-save_posts
    """
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.status_code == 200:
        post = r.json()
        data = [{'id': new['id'], 'title': new['title'],
                'body': new['body']} for new in post]

        with open("posts.csv", "w") as c:
            fieldnames = ['id', 'title', 'body']
            wry = csv.DictWriter(c, fieldnames=fieldnames)
            wry.writeheader()
            wry.writerows(data)
