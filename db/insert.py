import datetime
import time
from db import connection


def coin_data_insert(coin_data, thread_num):
    cursor = connection.cursor_function()
    try:
        coin_kodu = coin_data.symbol
        islem_zaman_birimi = coin_data.interval
        gelen_veri_zamani = coin_data.time
        olusturma_zamani = datetime.datetime.now()

        indikator_values = [(coin_kodu, indikator_adi, indikator_degeri, islem_zaman_birimi, olusturma_zamani, gelen_veri_zamani)
                            for indikator_adi, indikator_degeri in coin_data.indicators.items()]

        cursor.executemany("INSERT INTO INDICATOR_DATA(SYMBOL_CODE, INDICATOR_NAME, INDICATOR_VALUE, INTERVAL_TYPE, INSERTED_DATE_TIME, INCOMING_DATA_DATE_TIME) VALUES(?,?,?,?,?,?)",
                           indikator_values)
        cursor.commit()

    except Exception as e:
        print(e, "coin_data_insert")
        return e
