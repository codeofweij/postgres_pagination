"""
 Postgres Pagination Example
"""


MAX_FETCH_SIZE = 500

def paginate(namelist_id):
    """
    returns page index followed by the name of the first row.
    example:
    page | rows      | start name
    1.   |1-499      | ""
    2.   |500-999    | Charles Frank
    3.   |1000-1499  | Harrison Peter
    4.   |1500-1999  | Laura Jones
    5.   |2000-2300  | Zack Peter

    """

    pagination = {}
    db = get_database()
    try:
        cursor = db.cursor()
        fetch_size = 1000

        paginate = """
            select row_id, name from 
            (
            select row_number() over (order by name) as row_id, name  
              from core.names
             where namelist_id = %s
             order by name
            ) t
            where t.row_id %% %s = 0  or t.row_id = 1
        """
        paginate = paginate % (namelist_id, MAX_FETCH_SIZE)

        cursor.execute(paginate)
        for (rownum, name) in cursor.fetchall():

            page = (rownum/MAX_FETCH_SIZE+1)
            pagination[page] = name

        cursor.close()
    except Exception, e:
        log.info(e)
        errors.handle(e)
    finally:
        db.close()

    return pagination

def get_names(namelist_id, start_name):
    """
    returns first 500 entries starting from start_name.
    
    """
    items = []
    db = get_database()
    try:
        cursor = db.cursor()

        sql = """
        select n.id, n.name, n.details
          from core.namelist nl 
          join core.names si on ( n.namelist_id = nl.id )
          where nl.id = %s 
            and n.name >= '%s'
            order by n.name
            fetch first %s rows only
            """

        sql = sql % (namelist_id, start_name, MAX_FETCH_SIZE)

        cursor.execute(sql)
        items = [dict(id=rs[0], name=rs[1], detail=rs[2]) for rs in cursor.fetchall()]
    except Exception, e:
        log.info(e)
        errors.handle(e)
    finally:
        db.close()

    return items
