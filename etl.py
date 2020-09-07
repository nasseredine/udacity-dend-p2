import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def redshift_cluster_connect(config):
    """Connects to the Amazon Redshift cluster and returns `connection` and `cursor` objects (from psycopg2).

    Args:
        config (dict): The configuration of the Redshift cluster to connect to.
    """
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))

    return conn.cursor(), conn


def load_staging_tables(cur, conn):
    """Loads data in the staging tables.
    
    Loads song and log data from Amazon S3 (objects storage) and insert them into the corresponding
    staging tables (see :func:`sql_queries.copy_table_queries` list) in Amazon Redshift (data warehouse).
    
    Args:
        cur (cursor): The `cursor` object to the database session (from psycopg2).
        conn (connection): The `connection` object to the database session (from psycopg2).
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """Inserts the data to the analytical tables.
    
    Inserts song and log data from the staging tables into Amazon Redshift (data warehouse)
    to the analytical tables (see :func:`sql_queries.insert_table_queries` list) in the same Amazon Redshift.
    
    Args:
        cur (cursor): The `cursor` object to the database session (from psycopg2).
        conn (connection): The `connection` object to the database session (from psycopg2).
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    - Parses the `dwh.cfg` configuration file.
    - Connects to the Redshift cluster.
    - Loads the data into the tables (see :func:`~etl.load_staging_tables`).
    - Insert the tables (see :func:`~etl.insert_tables`).
    - Closes the connection to the Redshift cluster.
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    cur, conn = redshift_cluster_connect(config)
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
