import sqlite3
from typing import List
import datetime

from model import MyPackage

conn = sqlite3.connect("packages.db")
c = conn.cursor()


def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS mypacks (
    package text,
    date_added text
    )""")


create_table()


def insert_package(mpacks: MyPackage):
    c.execute("select count(*) FROM mypacks")

    with conn:
        c.execute(
            "INSERT INTO mypacks VALUES (:package, :date_added)",
            {'package': mpacks.package, 'date_added': mpacks.date_added, })


def get_all_packages() -> List[MyPackage]:
    c.execute("select * from mypacks")
    results = c.fetchall()
    mypacks = []
    for result in results:
        mypacks.append(MyPackage(*result))
    return mypacks
