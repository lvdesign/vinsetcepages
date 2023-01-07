import datetime
from django.db import connection


def myDate():
    toto = datetime.date.today()
    return toto


def dump_queries() :
    qs = connection.queries
    for q in qs:
        print(q)