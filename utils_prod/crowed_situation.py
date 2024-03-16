import asyncio
import pymysql
from datetime import datetime, timedelta
from utils.speech_synthesis import text_to_speech

# Paramètres de connexion
HOST = "37.187.92.31"
PORT = 9103
USER = "cow2024"
PASSWORD = "password"
DB = "proximus"
TABLE = "proximus"  # Remplacez par votre nom de table réel

def get_rows_with_timestamp_and_coordinates(cursor, simulated_time):
    query = f"SELECT * FROM {TABLE} WHERE timestamp = %s AND ST_Contains(ST_GeomFromText(wkt), POINT(4.4404401974129915, 50.40490262773668))"
    cursor.execute(query, (simulated_time,))
    result = cursor.fetchall()
    return result

async def main():
    print("Main of crowded_situation.py")
    connection = pymysql.connect(host=HOST, port=PORT, user=USER, password=PASSWORD, db=DB)
    try:
        start_time = datetime(2023, 2, 2, 21, 0, 0)

        simulated_time = start_time

        while True:
            simulated_time_str = simulated_time.strftime('%Y-%m-%d %H:%M:%S')

            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                rows = get_rows_with_timestamp_and_coordinates(cursor, simulated_time_str)

                if rows:
                    for row in rows:
                        total_personnes = str(row["total"])
                        text_to_speech(
                            "Vous entrez dans une zone dont la foule estimée est de " + total_personnes + " personnes.")
                        print("Ligne trouvée:")
                        print(row)
                else:
                    print(f"Aucune ligne trouvée pour le timestamp simulé: {simulated_time_str}")

            simulated_time += timedelta(minutes=5)

            await asyncio.sleep(1)

    finally:
        connection.close()


asyncio.run(main())
