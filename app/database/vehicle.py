from app.database import get_db


def output_formatter(results):           #results will be tuple of tuples
    out = []                            #empty list
    for result in results:              #For each loop.
        result_dict = {
            "id": result[0],
            "color": result[1],
            "license_plate": result[2],
            "v_type": result [3],
            "owner_id": result[4],
            "active": result[5]
        }
        out.append(result_dict)
    return out


def insert(vehicle_dict):
    value_tuple = (
        vehicle_dict.get("color"),
        vehicle_dict.get("license_plate"),
        vehicle_dict.get("v_type"),
        vehicle_dict.get("owner_id")
    )
    statement = """
        INSERT INTO vehicle (
            color,
            licence_plate,
            v_type,
            owner_id
        ) VALUES (?, ?, ?,?)
    """
    cursor = get_db()
    cursor.execute(statement, value_tuple)
    cursor.commit()
    cursor.close()


def scan():
    cursor = get_db().execute("SELECT * FROM vehicle WHERE active=1", ())
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)

def select_by_id(pk):
    cursor = get_db().execute("SELECT *FROM vehicle WHERE id=?", (pk,))
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)

def update(pk, vehicle_data):              #user_data parameter is a dictionary (dict type)
    value_tuple = (
        vehicle_data.get("color"),
        vehicle_data.get("license_plate"),
        vehicle_data.get("v_type"),
        vehicle_data.get("owner_id"),
        pk
    )

    statement = """
        UPDATE vehicle
        SET color=?,
        license_plate=?,
        v_type=?
        WHERE id=?
"""
    cursor = get_db()
    cursor.execute(statement, value_tuple)
    cursor.commit()
    cursor.close()