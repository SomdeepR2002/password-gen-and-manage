from utils.db_config import dbconfig
from getpass import getpass
import hashlib
from rich import print as printc
from rich.console import Console
import sys
import secrets
import string

console = Console()

def gen_device_secret(length=10):
    return ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(length))

def config():
    # Initialize database connection and cursor
    db = dbconfig()  # Call the dbconfig function to connect to the database
    cursor = db.cursor()  # Retrieve the cursor for SQL operations

    printc("[green][+] Creating new config [/green]")

    # Create the 'pm' database
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS pm")
    except Exception as e:
        printc("[red][+] AN ERROR OCCURRED WHILE TRYING TO CREATE DB[/red]")
        console.print_exception(show_locals=True)
        sys.exit(0)
    printc("[green][+][/green] Database 'pm' created")

    # Create tables in 'pm' database
    try:
        cursor.execute("USE pm")
        cursor.execute("CREATE TABLE IF NOT EXISTS secrets (masterkey_hash TEXT NOT NULL, device_secret TEXT NOT NULL)")
        printc("[green][+][/green] Table 'secrets' created")

        cursor.execute("CREATE TABLE IF NOT EXISTS entries (site_name TEXT NOT NULL, site_url TEXT NOT NULL, email TEXT NOT NULL, username TEXT NOT NULL, password TEXT NOT NULL)")
        printc("[green][+][/green] Table 'entries' created")
    except Exception as e:
        printc("[red][+] AN ERROR OCCURRED WHILE CREATING TABLES[/red]")
        console.print_exception(show_locals=True)
        sys.exit(0)

    # Prompt user to set a master password
    while True:
        mpass = getpass("Choose a master password: ")
        if mpass == getpass("Re-type master password: ") and mpass != "":
            break
        printc("[yellow] Please try again. [/yellow] Passwords do not match or are empty.")

    # Hash the master password
    hashed_mpass = hashlib.sha256(mpass.encode()).hexdigest()
    printc("[green][+][/green] MASTER PASSWORD HASH GENERATED")

    # Generate Device Secret
    dsecret = gen_device_secret()
    printc("[green][+][/green] DEVICE SECRET GENERATED")

    # Insert hashed master password and device secret into the database
    try:
        query = "INSERT INTO secrets (masterkey_hash, device_secret) VALUES (%s, %s)"
        cursor.execute(query, (hashed_mpass, dsecret))
        db.commit()
        printc("[green][+][/green] Master password and device secret stored in database")
    except Exception as e:
        printc("[red][+] AN ERROR OCCURRED WHILE STORING SECRETS IN DB[/red]")
        console.print_exception(show_locals=True)
        sys.exit(0)

    # Close the database connection
    cursor.close()
    db.close()

# Call config to execute the setup
config()
