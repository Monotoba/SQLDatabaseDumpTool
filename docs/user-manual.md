### User Manual for Database Dump Tool

---

#### **1. Introduction**

This tool allows you to back up all databases from various database management systems (DBMS) to individual SQL dump files. It supports a wide variety of databases, including MySQL/MariaDB, PostgreSQL, CouchDB, CockroachDB, MongoDB, Oracle, SQL Server, and SQLite.

The tool is designed for use in server migrations, backup purposes, and data migration across systems. It can be run from the command line and allows flexible configuration with various database types, user credentials, and output folder options.

---

#### **2. Supported DBMS (Database Management Systems)**

- **MySQL**: Supports dumping all databases in MySQL.
- **MariaDB**: Supports dumping all databases in MariaDB.
- **PostgreSQL**: Dumps all PostgreSQL databases using `pg_dumpall`.
- **CouchDB**: Dumps all databases and their documents in JSON format.
- **CockroachDB**: Dumps all databases to a SQL format using `cockroach dump`.
- **MongoDB**: Dumps MongoDB databases using `mongodump`.
- **Oracle**: Dumps all Oracle databases using `exp` (Export utility).
- **SQL Server**: Dumps databases using `sqlcmd` with a `.bak` file.
- **SQLite**: Dumps SQLite databases using the `.dump` command.

---

#### **3. Features**

- **Automatic Detection**: If the database type is not specified, the tool will attempt to automatically detect the DBMS by connecting to the specified host and validating the version.
- **User Authentication**: Supports authentication with username and password for each DBMS.
- **Destination Folder**: Allows specifying a folder where all the database dump files will be saved.
- **Comprehensive Dumps**: Ensures that all objects are included in the dump (tables, views, triggers, etc.), specific to the database type.

---

#### **4. Command-Line Usage**

##### **Syntax**:
```
python db_dump_tool.py --host <hostname> --user <username> --password <password> --destination-folder <destination_folder> [--db-type <db_type>]
```

##### **Arguments**:

- `--host <hostname>`: The hostname or IP address of the database server. For example, `localhost` or `db.example.com`.
- `--user <username>`: The database user with sufficient privileges to dump the databases.
- `--password <password>`: The password for the database user.
- `--destination-folder <destination_folder>`: The directory where all dump files will be saved. This folder must be writable by the user running the script.
- `--db-type <db_type>` *(Optional)*: Specify the type of database to be dumped. Available options are:
  - `mysql`
  - `mariadb`
  - `postgresql`
  - `couchdb`
  - `cockroachdb`
  - `mongodb`
  - `oracle`
  - `sqlserver`
  - `sqlite`
  
  If not specified, the tool will attempt to detect the database type automatically.

---

#### **5. Example Commands**

##### **Example 1: Dumping all databases from a MySQL server**
```
python db_dump_tool.py --host localhost --user root --password mypassword --destination-folder /backups
```

##### **Example 2: Dumping all databases from a PostgreSQL server with specified DB type**
```
python db_dump_tool.py --host localhost --user postgres --password secret --destination-folder /backups --db-type postgresql
```

##### **Example 3: Dumping all databases from a MongoDB server**
```
python db_dump_tool.py --host localhost --user admin --password mongo123 --destination-folder /backups --db-type mongodb
```

##### **Example 4: Dumping all databases from an Oracle server**
```
python db_dump_tool.py --host localhost --user oracle_user --password oracle_pass --destination-folder /backups --db-type oracle
```

##### **Example 5: Dumping all databases from a SQL Server**
```
python db_dump_tool.py --host localhost --user sa --password sqlpass --destination-folder /backups --db-type sqlserver
```

---

#### **6. Output**

The tool will generate SQL dump files (or equivalent formats) for each database in the specified destination folder. The files will be named based on the database names with `.sql` (or appropriate format) extensions.

- **MySQL/MariaDB**: `database_name.sql`
- **PostgreSQL**: `postgresql_all.sql`
- **CouchDB**: `database_name.json`
- **CockroachDB**: `cockroach_all.sql`
- **MongoDB**: A directory with databases and collections backed up as `.bson` and `.json` files.
- **Oracle**: `oracle_backup.dmp`
- **SQL Server**: `sqlserver_backup.bak`
- **SQLite**: `sqlite_backup.sql`

---

#### **7. Troubleshooting**

##### **Common Errors:**

1. **Error: `Unsupported DB type`**  
   This error occurs when an unsupported database type is specified or when an invalid DB type is auto-detected. Ensure the database type is supported and spelled correctly.
   
2. **Error: `Unable to connect to database`**  
   If the connection to the database fails, verify that the host, user credentials, and database server are correctly specified. Also, ensure that the database server is accessible from the machine running the script.

3. **Error: `Permission denied`**  
   If you encounter a permission error when attempting to write to the destination folder, make sure that the user running the script has write permissions for the specified directory.

4. **Error: `mysqldump: command not found`**  
   This error indicates that `mysqldump` (for MySQL/MariaDB) or `pg_dumpall` (for PostgreSQL) is not installed or not in the system's `PATH`. Ensure that the required database utilities are installed on the system.

---

#### **8. Considerations**

- **Database Size**: Dumping large databases can take a considerable amount of time, depending on the size of the data and the performance of the database server.
- **Storage Space**: Ensure that the destination folder has enough disk space to store the database dumps.
- **Restore Process**: The script is designed for database backup only. The restoration process for each DBMS (especially Oracle and SQL Server) may require different utilities, such as `mysqlimport` for MySQL/MariaDB or `pg_restore` for PostgreSQL.

---

### **9. Licensing and Support**  

This script is released under the **MIT License**, which allows for free use, modification, distribution, and private or commercial usage. While the script is provided as-is without warranty, users are encouraged to contribute improvements or report issues. For more details, refer to the **LICENSE** file included with the source code.  

For support, please consult the official documentation of the respective database systems or visit community forums related to MySQL, PostgreSQL, MongoDB, Oracle, SQL Server, and other supported DBMS.

---

#### **10. Conclusion**

This Database Dump Tool provides a simple, unified way to back up databases from multiple database management systems. It allows users to migrate databases, perform backups, and manage database exports across various systems, saving both time and effort in database administration.
