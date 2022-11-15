# SET UP

### Open powershell from project directory and run this:
```powershell
env\Scripts\activate.bat
```

### Install packages and modules from requirements.txt:
```powershell
pip install -r requirements.txt
```

### Get the database and table ready:
```bash
python database.py
```

You are now all set.

# Commands

### list all entries
```bash
python main.py list
```

### create entry
```bash
python main.py create "a text string to record task purpose"
```

### update entry message
```bash
python main.py update [id] "New Message"
```

### delete entry
```bash
python main.py delete [id]
```

### stop entry
```bash
python main.py stop [id]
```
Duration is calculated once the record is stopped.
