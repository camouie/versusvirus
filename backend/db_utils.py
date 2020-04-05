import json, psycopg2
import datetime
import sys
import random


def get_json(fl):
    try:
        return json.loads(fl)
    except ValueError as e:
        return json.loads(e)


def check_date_format(dt):
    try:
        return True, datetime.datetime.strptime(dt, '%Y-%m-%d').isoformat()
    except ValueError as e:
        return False, str(e)


def insert(conn, cur, statement):
    try:
        cur.execute(statement)
        rc = cur.rowcount
        conn.commit()
        return True, "{} rows has been inserted".format(rc)
    except psycopg2.OperationalError as e:
        cur.rollback()
        return False, str(e)


def insert_return(conn, cur, statement):
    try:
        statement += " RETURNING id"
        cur.execute(statement)
        rc = cur.rowcount
        id = cur.fetchone()[0]
        conn.commit()
        return id, "{} rows has been inserted".format(rc)
    except psycopg2.OperationalError as e:
        cur.rollback()
        return False, str(e)


def update(conn, cur, statement):
    try:
        cur.execute(statement)
        rc = cur.rowcount
        conn.commit()
        return True, "{} rows has been updated".format(rc)
    except psycopg2.OperationalError as e:
        cur.rollback()
        return False, str(e)


def format_bind(cols, rows):
    return '(' + '), ('.join([', '.join(['%s'] * cols)] * rows) + ')'


def insert_dict(conn, cur, statement, dict):
    try:
        columns = dict.keys()
        values = [dict[column] for column in columns]

        insert_statement = '{} (%s) values %s'.format(statement)
        cur.execute(insert_statement, (psycopg2.extensions.AsIs(','.join(columns)), tuple(values)))
        #cur.mogrify(insert_statement, (psycopg2.extensions.AsIs(','.join(columns)), tuple(values)))
        rc = cur.rowcount
        conn.commit()
        cur.execute("""select max(id) as max from queries;""")
        id = int(cur.fetchall()[0]["max"])

        return id, "{} rows has been inserted".format(rc)
    except psycopg2.OperationalError as e:
        cur.rollback()
        return False, str(e.message)


def insert_dict_return(conn, cur, statement, dict, id="id"):
    try:
        columns = dict.keys()
        values = [dict[column] for column in columns]

        insert_statement = '{} (%s) values %s RETURNING {1}'.format(statement, id)
        cur.execute(insert_statement, (psycopg2.extensions.AsIs(','.join(columns)), tuple(values)))
        rc = cur.rowcount
        id = cur.fetchone()[0]
        conn.commit()
        return id, "{} rows has been inserted".format(rc)
    except psycopg2.OperationalError as e:
        cur.rollback()
        return False, str(e.message)