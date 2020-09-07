import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def redshift_cluster_connect(config):
    """Connects to the Amazon Redshift cluster and returns `connection` and `cursor` objects (from psycopg2).

    Args:
        config (dict): The configuration of the Redshift cluster to connect to.
    """
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))

    return conn.cursor(), conn


def drop_tables(cur, conn):
    """Drops each table using the queries in `drop_table_queries` list.
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """Creates each table using the queries in `create_table_queries` list.
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    - Parses the `dwh.cfg` configuration file.
    - Connects to the Redshift cluster.
    - Drops the tables (see :func:`~create_tables.drop_tables`).
    - Creates the tables (see :func:`~create_tables.create_tables`).
    - Closes the connection to the Redshift cluster.
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    cur, conn = redshift_cluster_connect(config)

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
