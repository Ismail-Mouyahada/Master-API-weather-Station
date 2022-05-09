import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import request

# Add a new data into the database rows [table name : donnees]
@app.route('/api/v1/ajouter/', methods=['POST'])
def ajouter_donnees():

    _json = request.json
    _farenheit = _json['farenheit']
    _temperature = _json['temperature']
    _humidity = _json['humidite']
    _capteur = _json['capture']

    if  _temperature and _humidity  and _capteur and _farenheit and request.method == 'POST':
        sqlQuery = "INSERT INTO donnees( temperature, humidite, capture,farenheit) VALUES(%s, %s, %s, %s)"
        bindData_add_don = ( _temperature, _humidity, _capteur,_farenheit)
        conn = mysql.connect()
        cursor_add_don = conn.cursor()
        cursor_add_don.execute(sqlQuery, bindData_add_don)
        conn.commit()
        response_add_don = jsonify('les données ont été enregistrées avec succès !')
        response_add_don.status_code = 200
        return response_add_don
    else:
        return not_found()



# fetch all rows from  database concernning the table utilisateurs [table name : donnees]
@app.route('/api/v1/donnees/')
def lire_donnees():
    try:
        conn = mysql.connect()
        cursor_read_don = conn.cursor(pymysql.cursors.DictCursor)
        cursor_read_don.execute("SELECT id, farenheit, temperature, humidite, date, capture FROM donnees")
        empRows = cursor_read_don.fetchall()
        response_read_don = jsonify(empRows)
        response_read_don.status_code = 200
        return response_read_don
    except Exception as e:
        print(e)
    finally:
        cursor_read_don.close()
        conn.close()


@app.route('/api/v1/donnees/humidite/<int:id>')
def fitlrer_Humidite(id):
    try:
        conn = mysql.connect()
        cursor_hum = conn.cursor(pymysql.cursors.DictCursor)
        cursor_hum.execute("SELECT id, humidite, date, capture FROM donnees WHERE id =%s", id)
        empRow = cursor_hum.fetchone()
        response_filt_hum = jsonify(empRow)
        response_filt_hum.status_code = 200
        return response_filt_hum
    except Exception as e:
        print(e)
    finally:
        cursor_hum.close()
        conn.close()


@app.route('/api/v1/donnees/temperature/<int:id>')
def filtrer_temperature(id):
    try:
        conn = mysql.connect()
        cursor_temp = conn.cursor(pymysql.cursors.DictCursor)
        cursor_temp.execute("SELECT id, farenheit, temperature, date, capture FROM donnees WHERE id =%s", id)
        empRow = cursor_temp.fetchone()
        response_filt_temp = jsonify(empRow)
        response_filt_temp.status_code = 200
        return response_filt_temp
    except Exception as e:
        print(e)
    finally:
        cursor_temp.close()
        conn.close()


@app.route('/api/v1/modifier/', methods=['PUT'])
def modifier_donnees():
    try:
        _json = request.json
        _farenheit = _json['farenheit']
        _id = _json['id']
        _temperature = _json['temperature']
        _humidity = _json['humidite']
        _date = _json['date']
        _capteur = _json['capture']
        if _id and _farenheit and _temperature and _humidity and _date and _capteur and request.method == 'PUT':
            sqlQuery = "UPDATE donnees SET farenheit=%s, temperature=%s, humidite=%s, date=%s, capture=%s WHERE id=%s"
            bindData_mod_don = (_id, _farenheit, _temperature, _humidity, _date, _capteur)
            conn = mysql.connect()
            cursor_mod_don = conn.cursor()
            cursor_mod_don.execute(sqlQuery, bindData_mod_don)
            conn.commit()
            response_mod_don = jsonify('les données ont été modifié avec succès')
            response_mod_don.status_code = 200
            return response_mod_don
        else:
            return not_found()
    except Exception as e: \
            print(e)
    finally:
        cursor_mod_don.close()
        conn.close()


@app.route('/api/v1/supprimer/<int:id>', methods=['DELETE'])
def supprimer_donnees(id):
    try:
        conn = mysql.connect()
        cursor_sup_don = conn.cursor()
        cursor_sup_don.execute("DELETE FROM donnees WHERE id=%s", id)
        conn.commit()
        response_sup_don = jsonify('Données ont été supprimées avec succès!')
        response_sup_don.status_code = 200
        return response_sup_don
    except Exception as e:
        print(e)
    finally:
        cursor_sup_don.close()
        conn.close()

# Add a new data into the database rows [table name : api]
@app.route('/api/v1/capteur/ajouter/', methods=['POST'])
def ajouter_capteur():
    _json = request.json
    _nom = _json['nom']
    _description = _json['description']
    _version = _json['version']
    _statut = _json['statut']

    if _nom and _description and _version and _statut and request.method == 'POST':
        sqlQuery = "INSERT INTO `api` (`id`, `nom`, `description`, `version`, `statut`) VALUES(NULL,%s, %s,%s ,%s)"
        bindData_add_cap = (_nom, _description, _version, _statut)
        conn = mysql.connect()
        cursor_add_cap = conn.cursor()
        cursor_add_cap.execute(sqlQuery, bindData_add_cap)
        conn.commit()
        response_add_cap = jsonify('les données ont été enregistrées avec succès !')
        response_add_cap.status_code = 200
        return response_add_cap
    else:
        return not_found()


@app.route('/api/v1/capteurs/')
def lire_capteur():
    try:
        conn = mysql.connect()
        cursor_read_cap = conn.cursor(pymysql.cursors.DictCursor)
        cursor_read_cap.execute("SELECT id, nom, description, version, statut FROM api")
        empRows = cursor_read_cap.fetchall()
        response_read_cap = jsonify(empRows)
        response_read_cap.status_code = 200
        return response_read_cap
    except Exception as e:
        print(e)
    finally:
        cursor_read_cap.close()
        conn.close()


@app.route('/api/v1/capteur/<int:id>')
def filtrer_capteur(id):
    try:
        conn = mysql.connect()
        cursor_filt_cap = conn.cursor(pymysql.cursors.DictCursor)
        cursor_filt_cap.execute(
            "SELECT id, nom, description, version, statut FROM api WHERE id =%s", id)
        empRow = cursor_filt_cap.fetchone()
        response_filt_cap = jsonify(empRow)
        response_filt_cap.status_code = 200
        return response_filt_cap
    except Exception as e:
        print(e)
    finally:
        cursor_filt_cap.close()
        conn.close()


@app.route('/api/v1/capteur/modifier/', methods=['PUT'])
def modifier_capteur():
    try:
        _json = request.json
        _id = _json['id']
        _nom = _json['nom']
        _description = _json['description']
        _version = _json['version']
        _statut = _json['statut']

        if _id and _nom and _description and _version and _statut and request.method == 'PUT':
            sqlQuery = "UPDATE `api` SET `nom` = %s, `description` = %s, `version` = %s, `statut` = %s WHERE `api`.`id` = %s"
            bindData_mod_cap = (_id, _nom, _description, _version, _statut)
            conn = mysql.connect()
            cursor_mod_cap = conn.cursor()
            cursor_mod_cap.execute(sqlQuery, bindData_mod_cap)
            conn.commit()
            response_mod_cap = jsonify('les données ont été modifié avec succès')
            response_mod_cap.status_code = 200
            return response_mod_cap
        else:
            return not_found()
    except Exception as e: \
            print(e)
    finally:
        cursor_mod_cap.close()
        conn.close()


@app.route('/api/v1/capteur/supprimer/<int:id>', methods=['DELETE'])
def supprimer_capteur(id):
    try:
        conn = mysql.connect()
        cursor_sup_cap = conn.cursor()
        cursor_sup_cap.execute("DELETE FROM api WHERE id=%s", id)
        conn.commit()
        response_sup_cap = jsonify('Données ont été supprimées avec succès!')
        response_sup_cap.status_code = 200
        return response_sup_cap
    except Exception as e:
        print(e)
    finally:
        cursor_sup_cap.close()
        conn.close()

# Add a new data into the database rows [table name : utilisateurs]
@app.route('/api/v1/user/ajouter/', methods=['POST'])
def ajouter_utilisateur():
    _json = request.json
    _nom = _json['nom']
    _prenom = _json['prenom']
    _email = _json['email']
    _password = _json['mot_de_passe']
    _type = _json['type']
    _color = _json['color']

    if  _nom and _prenom and _email and _password and _type and _color and request.method == 'POST':
        sqlQuery = "INSERT INTO utilisateurs( nom, prenom, email, mot_de_passe, type, color) VALUES( %s, %s, %s,%s, %s, %s)"
        bindData_add_user = (_nom, _prenom, _email,  _password, _type, _color)
        conn = mysql.connect()
        cursor_add_user = conn.cursor()
        cursor_add_user.execute(sqlQuery, bindData_add_user)
        conn.commit()
        response_add_user = jsonify('les données ont été enregistrées avec succès !')
        response_add_user.status_code = 200
        return response_add_user
    else:
        return not_found()


@app.route('/api/v1/utilisateurs/')
def lire_utilisateurs():
    try:
        conn = mysql.connect()
        cursor_read_user = conn.cursor(pymysql.cursors.DictCursor)
        cursor_read_user.execute("SELECT id, nom, prenom, email, mot_de_passe, type, color FROM utilisateurs")
        empRows = cursor_read_user.fetchall()
        response_read_user = jsonify(empRows)
        response_read_user.status_code = 200
        return response_read_user
    except Exception as e:
        print(e)
    finally:
        cursor_read_user.close()
        conn.close()


@app.route('/api/v1/utilisateur/<int:id>')
def filtrer_utilisateur(id):
    try:
        conn = mysql.connect()
        cursor_filt_user = conn.cursor(pymysql.cursors.DictCursor)
        cursor_filt_user.execute(
            "SELECT id, nom, prenom, email, mot_de_passe, type, color FROM utilisateurs WHERE id =%s", id)
        empRow = cursor_filt_user.fetchone()
        response_filt_user = jsonify(empRow)
        response_filt_user.status_code = 200
        return response_filt_user
    except Exception as e:
        print(e)
    finally:
        cursor_filt_user.close()
        conn.close()


@app.route('/api/v1/user/modifier/', methods=['PUT'])
def modifier_utilisateur():
    try:
        _json = request.json
        _id = _json['id']
        _nom = _json['nom']
        _prenom = _json['prenom']
        _email = _json['email']
        _password = _json['mot_de_passe']
        _type = _json['type']
        _color = _json['color']

        if _id and _nom and _prenom and _email and _password and _type and _color and request.method == 'PUT':
            sqlQuery = "UPDATE `utilisateurs` SET `id`= %s, `nom` = %s, `email` = %s, `mot_de_passe` = %s, `type` = %s, `color` = %s WHERE `utilisateurs`.`id` = %s"
            bindData_mod_use = (_id, _nom, _prenom, _email, _password, _type, _color)
            conn = mysql.connect()
            cursor_mod_use = conn.cursor()
            cursor_mod_use.execute(sqlQuery, bindData_mod_use)
            conn.commit()
            response_mod_use = jsonify('les données ont été modifié avec succès')
            response_mod_use.status_code = 200
            return response_mod_use
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor_mod_use.close()
        conn.close()


@app.route('/api/v1/user/supprimer/<int:id>', methods=['DELETE'])
def supprimer_utilisateur(id):
    try:
        conn = mysql.connect()
        cursor_sup_use = conn.cursor()
        cursor_sup_use.execute("DELETE FROM utilisateurs WHERE id=%s", id)
        conn.commit()
        response_sup_use = jsonify('Données ont été supprimées avec succès!')
        response_sup_use.status_code = 200
        return response_sup_use
    except Exception as e:
        print(e)
    finally:
        cursor_sup_use.close()
        conn.close()





@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Enregistrement introuvable mais l\'api marche : ' + request.url,
    }
    response_error = jsonify(message)
    response_error.status_code = 404
    return response_error


if __name__ == "__main__":
    app.run(host='192.168.43.60', port=5000)
