from typing import List, Dict

from psycopg2 import sql
from psycopg2.extras import RealDictCursor

import database_common, re


@database_common.connection_handler
def get_mentors(cursor: RealDictCursor) -> list:
    query = """
        SELECT first_name, last_name, city
        FROM mentor
        ORDER BY first_name"""
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_mentors_by_last_name(cursor: RealDictCursor, last_name: str) -> list:
    query = """
        SELECT first_name, last_name, city
        FROM mentor
        WHERE LOWER(last_name) = LOWER(%(last_name)s)
        ORDER BY first_name"""
    cursor.execute(query, {'last_name': last_name})
    return cursor.fetchall()


@database_common.connection_handler
def get_cities(cursor: RealDictCursor) -> list:
    query = """
        SELECT DISTINCT city from mentor;
    """
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_mentors_by_city(cursor: RealDictCursor, city: str) -> list:
    query = """
        SELECT first_name, last_name, city
        FROM mentor
        WHERE city = %(city)s"""
    cursor.execute(query, {'city': city})
    return cursor.fetchall()


@database_common.connection_handler
def get_applicant_data_by_name(cursor: RealDictCursor, name: str) -> list:
    query = """
        SELECT CONCAT(first_name, ' ', last_name) AS full_name, phone_number
        FROM applicant
        WHERE first_name = %(name)s OR last_name = %(name)s
        """
    cursor.execute(query, {'name': name})
    return cursor.fetchall()


@database_common.connection_handler
def get_applicant_data_by_email_ending(cursor: RealDictCursor, email_ending: str) -> list:
    cursor.execute("""
        SELECT CONCAT(first_name, ' ', last_name) AS full_name, phone_number
        FROM applicant
        WHERE SUBSTR(email, POSITION('@' in email)) = %(email_ending)s
        """, {'email_ending': email_ending})
    return cursor.fetchall()

@database_common.connection_handler
def get_applicants(cursor: RealDictCursor) -> list:
    cursor.execute("""
    SELECT first_name, last_name, phone_number, email, application_code 
    FROM applicant
    """)
    return cursor.fetchall()
