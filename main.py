import asyncio
import requests
import sqlite3

conn = sqlite3.connect('levels.db')
cur = conn.cursor()
cur.execute('CREATE TABLE levels (id integer, level integer, xp integer)')

id = input("What is your server's id? ")
token = input("What is your auth token? ")
r = requests.get(f'https://mee6.xyz/api/plugins/levels/leaderboard/{id}', headers={"Authorization":token})
players_json = r.json()['players']
for i in players_json:
    print(f"ID: {i['id']} || Level: {i['level']} || xp: {i['xp']}")
    cur.execute('INSERT INTO levels (id, level, xp) VALUES (?, ?, ?)',
                        (i['id'], i['level'], i['xp']))
conn.commit()
conn.close()
print("Dumped to levels.db, tbl: levels")

