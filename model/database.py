import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="database_toko"
    )

def check_login(username_admin, password_admin):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM user_admin WHERE username_admin=%s AND password_admin=%s"
    cursor.execute(query, (username_admin, password_admin))
    
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user

def get_barang():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT nama_barang, kategori_barang, kode_barang, stok FROM barang"
    )

    data = cursor.fetchall()

    conn.close()
    return data


def insert_barang(nama, kategori, kode):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO barang (nama_barang, kategori_barang, kode_barang, stok)
        VALUES (%s, %s, %s, %s)
        """,
        (nama, kategori, kode, 0)
    )
    conn.commit()
    cursor.close()
    conn.close()


def delete_barang(kode_barang):
    conn = get_connection()
    cursor = conn.cursor()

    query = "DELETE FROM barang WHERE kode_barang = %s"
    cursor.execute(query, (kode_barang,))

    conn.commit()
    cursor.close()
    conn.close()

def get_barang_low_stock():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nama_barang, kategori_barang, kode_barang, stok FROM barang WHERE stok < 5")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

def update_stok(kode_barang, stok_baru):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "UPDATE barang SET stok = %s WHERE kode_barang = %s"
    cursor.execute(sql, (stok_baru, kode_barang))
    conn.commit()
    cursor.close()
    conn.close()