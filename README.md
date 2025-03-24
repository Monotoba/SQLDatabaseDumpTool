# Database Dump Tool

## Overview
The **Database Dump Tool** is a command-line utility designed to back up all databases from various database management systems (DBMS) into individual dump files. It supports a wide range of databases, including MySQL, MariaDB, PostgreSQL, CouchDB, CockroachDB, MongoDB, Oracle, SQL Server, and SQLite.

This tool is ideal for server migrations, backup automation, and database archival.

## Features
- **Supports Multiple DBMS**: MySQL, MariaDB, PostgreSQL, CouchDB, CockroachDB, MongoDB, Oracle, SQL Server, and SQLite.
- **Automatic DBMS Detection**: If the database type is not specified, the tool attempts to identify it.
- **Comprehensive Dumps**: Includes all database objects such as tables, views, triggers, users, and permissions.
- **User Authentication**: Allows specifying a database username and password.
- **Flexible Output Location**: Specify a destination folder to store database dumps.
- **Cross-Platform**: Works on Linux, macOS, and Windows.

## Installation
Ensure the necessary database utilities are installed on your system:
- `mysqldump` for MySQL/MariaDB
- `pg_dumpall` for PostgreSQL
- `mongodump` for MongoDB
- `cockroach dump` for CockroachDB
- `exp` for Oracle
- `sqlcmd` for SQL Server
- `sqlite3` for SQLite

Clone the repository and navigate into the project folder:
```sh
 git clone https://github.com/your-repo/database-dump-tool.git
 cd database-dump-tool
```

## Usage

### Basic Syntax
```sh
python db_dump_tool.py --host <hostname> --user <username> --password <password> --destination-folder <destination_folder> [--db-type <db_type>]
```

### Command-Line Arguments
| Argument | Description |
|----------|-------------|
| `--host` | Database server hostname or IP address (e.g., `localhost`). |
| `--user` | Database username. |
| `--password` | Database user password. |
| `--destination-folder` | Path to store database dump files. |
| `--db-type` | *(Optional)* Specify database type (`mysql`, `mariadb`, `postgresql`, `couchdb`, `cockroachdb`, `mongodb`, `oracle`, `sqlserver`, `sqlite`). If omitted, the script attempts auto-detection. |

### Examples
#### **Dump all MySQL databases**
```sh
python db_dump_tool.py --host localhost --user root --password mypassword --destination-folder /backups
```

#### **Dump all PostgreSQL databases**
```sh
python db_dump_tool.py --host localhost --user postgres --password secret --destination-folder /backups --db-type postgresql
```

#### **Dump all MongoDB databases**
```sh
python db_dump_tool.py --host localhost --user admin --password mongo123 --destination-folder /backups --db-type mongodb
```

## Output
The tool generates database dump files in the specified destination folder. File formats vary by database type:
- **MySQL/MariaDB**: `database_name.sql`
- **PostgreSQL**: `postgresql_all.sql`
- **CouchDB**: `database_name.json`
- **CockroachDB**: `cockroach_all.sql`
- **MongoDB**: BSON/JSON dump directories.
- **Oracle**: `oracle_backup.dmp`
- **SQL Server**: `sqlserver_backup.bak`
- **SQLite**: `sqlite_backup.sql`

## Troubleshooting
### **Common Errors and Fixes**
1. **`Unsupported DB type`**: Ensure the correct database type is provided or that auto-detection is functioning properly.
2. **`Unable to connect to database`**: Verify credentials, host, and firewall settings.
3. **`Permission denied`**: Ensure the script has permission to write to the destination folder.
4. **`Command not found`**: Ensure required database utilities are installed and accessible in the system `PATH`.

## License
This project is licensed under the **MIT License**. You are free to use, modify, and distribute the software under the terms of this license. See the `LICENSE` file for details.

## Contributing
Contributions are welcome! Feel free to submit pull requests with improvements or fixes.

## Support
For support, refer to the official documentation of the respective database systems or join database community forums.

## Acknowledgments
Thanks to the open-source communities of MySQL, PostgreSQL, MongoDB, Oracle, SQL Server, and other DBMS developers for providing robust database tools.

---

### Happy Backing Up!
