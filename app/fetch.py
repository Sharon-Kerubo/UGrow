from .models import *
import psycopg2
from sqlalchemy import func
from sqlalchemy.sql import select
import json

def get_crops():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="crops")
        postgreSQL_select_Crops = "select * from app_crops"
        cursor = connection.cursor()
        cursor.execute(postgreSQL_select_Crops)
        app_crops = cursor.fetchall()

        crop_data = {}
        for row in app_crops:
            crop_data['name'] = str(row[1])
            crop_data['rainfall'] = str(row[2])
            crop_data['ph'] = str(row[3])
            crop_data['temperature'] = str(row[4])
            crop_data['humidity'] = str(row[5])
            crop_data['drainage'] = str(row[6])
            print(crop_data)

    except(Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def get_humidity():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="crops")
        postgreSQL_select_Humidity = "select * from app_humidity"
        cursor = connection.cursor()
        cursor.execute(postgreSQL_select_Humidity)
        app_humidity = cursor.fetchall()

        humidity_data = {}
        for row in app_humidity:
            humidity_data['element'] = str(row[1])
            humidity_data['jan'] = str(row[2])
            humidity_data['feb'] = str(row[3])
            humidity_data['mar'] = str(row[4])
            humidity_data['apr'] = str(row[5])
            humidity_data['may'] = str(row[6])
            humidity_data['jun'] = str(row[7])
            humidity_data['jul'] = str(row[8])
            humidity_data['aug'] = str(row[9])
            humidity_data['sep'] = str(row[10])
            humidity_data['oct'] = str(row[11])
            humidity_data['nov'] = str(row[12])
            humidity_data['dec'] = str(row[13])
            humidity_data['area_id'] = int(row[14])
            print(humidity_data)


    except(Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def get_rainfall():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="crops")
        postgreSQL_select_Rainfall = "select * from app_rainfall"
        cursor = connection.cursor()
        cursor.execute(postgreSQL_select_Rainfall)
        app_rainfall = cursor.fetchall()

        rainfall_data = {}
        for row in app_rainfall:
            rainfall_data['element'] = str(row[1])
            rainfall_data['jan'] = str(row[2])
            rainfall_data['feb'] = str(row[3])
            rainfall_data['mar'] = str(row[4])
            rainfall_data['apr'] = str(row[5])
            rainfall_data['may'] = str(row[6])
            rainfall_data['jun'] = str(row[7])
            rainfall_data['jul'] = str(row[8])
            rainfall_data['sep'] = str(row[10])
            rainfall_data['oct'] = str(row[11])
            rainfall_data['nov'] = str(row[12])
            rainfall_data['dec'] = str(row[13])
            rainfall_data['area_id'] = int(row[14])
            print(rainfall_data)


    except(Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def get_temperature():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="crops")
        postgreSQL_select_Temperature = "select * from app_temperature"
        cursor = connection.cursor()
        cursor.execute(postgreSQL_select_Temperature)
        app_humidity = cursor.fetchall()

        temperature_data = {}
        for row in app_humidity:
            temperature_data['element'] = str(row[1])
            temperature_data['jan'] = str(row[2])
            temperature_data['feb'] = str(row[3])
            temperature_data['mar'] = str(row[4])
            temperature_data['apr'] = str(row[5])
            temperature_data['may'] = str(row[6])
            temperature_data['jun'] = str(row[7])
            temperature_data['jul'] = str(row[8])
            temperature_data['aug'] = str(row[9])
            temperature_data['sep'] = str(row[10])
            temperature_data['oct'] = str(row[11])
            temperature_data['nov'] = str(row[12])
            temperature_data['dec'] = str(row[13])
            temperature_data['area_id'] = int(row[14])
            print(temperature_data)


    except(Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def get_area():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="crops")

        query = "SELECT phaq, drai, drai_descr, soil, lndf_descr, slop, ST_AsText (ST_Transform (geom, 4326)) from app_soils"
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

        data = {}
        for row in result:
            data['ph'] = str(row[0])
            data['drainage_desc'] = str(row[1])
            data['soil drainage'] = str(row[2])
            data['soil class'] = str(row[3])
            data['relief'] = str(row[4])
            data['slope'] = str(row[5])
            data['area'] = str(row[6])
            print(data)

    except(Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
