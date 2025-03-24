import argparse
import subprocess
import os
import sys
import mysql
import psycopg2
import sqlite3


# Function to check the DBMS type (MySQL/MariaDB/PostgreSQL, etc.)
def get_db_type(host, user, password, db_type=None):
    if db_type:
        return db_type

    try:
        # Check MySQL/MariaDB
        conn = mysql.connector.connect(host=host, user=user, password=password)
        cursor = conn.cursor()
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()[0]
        cursor.close()
        conn.close()

        if "MariaDB" in version:
            return "mariadb"
        elif "MySQL" in version:
            return "mysql"
        else:
            raise ValueError("Unable to determine MySQL/MariaDB version")

    except mysql.connector.Error:
        # Fallback: check PostgreSQL
        try:
            conn = psycopg2.connect(host=host, user=user, password=password)
            cursor = conn.cursor()
            cursor.execute("SELECT VERSION()")
            version = cursor.fetchone()[0]
            cursor.close()
            conn.close()

            if "PostgreSQL" in version:
                return "postgresql"
            else:
                raise ValueError("Unable to determine PostgreSQL version")
        except Exception as e:
            raise ValueError("Unable to connect to database")


# Function to dump databases based on DBMS
def dump_databases(host, user, password, db_type, destination_folder):
    if db_type == "mariadb" or db_type == "mysql":
        dump_command = "mysqldump" if db_type == "mysql" else "mariadbdump"
        command = [dump_command, '--host', host, '--user', user, '--password=' + password, '--all-databases',
                   '--no-tablespaces', '--routines', '--triggers']
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        databases = result.stdout.decode('utf-8').split("\n")
        for db in databases:
            if db.strip():
                db_name = db.strip()
                with open(os.path.join(destination_folder, f"{db_name}.sql"), "w") as f:
                    f.write(db)

    elif db_type == "postgresql":
        dump_command = "pg_dumpall"
        command = [dump_command, '--host', host, '--username', user, '--password', password, '--file',
                   os.path.join(destination_folder, "postgresql_all.sql")]
        subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    elif db_type == "couchdb":
        command = ["curl", "-X", "GET", f"http://{user}:{password}@{host}:5984/_all_dbs"]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        dbs = result.stdout.decode('utf-8').split("\n")
        for db in dbs:
            if db.strip():
                db_name = db.strip()
                backup_command = f"curl -X GET http://{user}:{password}@{host}:5984/{db_name}/_all_docs?include_docs=true > {os.path.join(destination_folder, f'{db_name}.json')}"
                subprocess.run(backup_command, shell=True)

    elif db_type == "cockroachdb":
        command = ["cockroach", "dump", "--insecure", "--host", host, "--user", user, "--password", password, "--file",
                   os.path.join(destination_folder, "cockroach_all.sql")]
        subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    elif db_type == "mongodb":
        command = ["mongodump", "--uri", f"mongodb://{user}:{password}@{host}:27017", "--out", destination_folder]
        subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    elif db_type == "oracle":
        command = ["exp", f"{user}/{password}@{host}:1521/ORCL",
                   "file=" + os.path.join(destination_folder, "oracle_backup.dmp"),
                   "log=" + os.path.join(destination_folder, "oracle_backup.log")]
        subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    elif db_type == "sqlserver":
        command = ["sqlcmd", "-S", host, "-U", user, "-P", password, "-Q",
                   f"BACKUP DATABASE [{user}] TO DISK = N'{os.path.join(destination_folder, 'sqlserver_backup.bak')}'"]
        subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    elif db_type == "sqlite":
        # For SQLite, it's just a file copy or using .dump
        command = ["sqlite3", os.path.join(destination_folder, f"{user}_backup.sql"), ".dump"]
        subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    else:
        print(f"Unsupported DB type: {db_type}")
        sys.exit(1)


# Command-line arguments
def parse_args():
    parser = argparse.ArgumentParser(description="Migrate MySQL, MariaDB, PostgreSQL, CouchDB, and more")
    parser.add_argument('--host', required=True, help="Database host")
    parser.add_argument('--user', required=True, help="Database user")
    parser.add_argument('--password', required=True, help="Database password for user")
    parser.add_argument('--destination-folder', required=True, help="Destination folder for dump files")
    parser.add_argument('--db-type',
                        choices=['mysql', 'mariadb', 'postgresql', 'couchdb', 'cockroachdb', 'mongodb', 'oracle',
                                 'sqlserver', 'sqlite'], help="Specify DB type if known")

    return parser.parse_args()


def main():
    args = parse_args()

    # Determine the DB type (if not provided, we'll detect it)
    db_type = get_db_type(args.host, args.user, args.password, args.db_type)

    print(f"Detected DB type: {db_type}")

    # Dump the databases
    dump_databases(args.host, args.user, args.password, db_type, args.destination_folder)
    print(f"Databases have been dumped to {args.destination_folder}")


if __name__ == '__main__':
    main()
