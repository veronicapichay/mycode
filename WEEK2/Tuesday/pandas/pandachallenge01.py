#!/usr/bin/python3
"""Veronica Pichay | TLG Learning
   Challenge Solution 01 - JSON to CSV"""

import pandas

def main():

    # create a dataframe from json
    df = pandas.read_json("5movies.json")

    # writeout dataframe to CSV
    df.to_csv("5movies-translated-from-json.csv")

if __name__ == "__main__":
    main()

