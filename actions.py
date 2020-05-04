import sqlite3
from datetime import datetime

class Modactions:
    def __init__(self, mod, action, members):
        self.mod = mod
        self.action = action
        self.members = members
        
    async def actionLogger(self, mod, action,members, reason):
        now = datetime.now()
        date_string = now.strftime('%Y-%m-%d')
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        cursor.execute(f'Select reason FROM logs WHERE user_id={members}')
        result = cursor.fetchall()
        sql = ('INSERT INTO logs(user_id, reason) VALUES(?,?)')
        val = (members, f'{date_string}: {action} by {mod} | Reason: {reason}')
        cursor.execute(sql, val)
        db.commit()
