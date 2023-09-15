#!/usr/bin/python3
"""
    Module connect to MySQL using MySQLdb Module
    – selects all states but filters by names
    starting with N using MySQL regex operator
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cursor = db.cursor()
    query = '''SELECT * FROM states WHERE states.name
        LIKE BINARY "'''+argv[4]+'" ORDER BY states.id'
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(row)
