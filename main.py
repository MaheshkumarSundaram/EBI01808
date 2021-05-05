from app import app
from config import mysql
from flask import jsonify
from flask import flash, request


@app.route('/gene_suggest', methods=['GET'])
def gene_suggest():
    conn = mysql.connect()
    cursor = conn.cursor()
    search_query = request.args.get('query', default = "brc", type = str)
    species_name = request.args.get('species', default = "homo_sapiens", type = str)
    limit_val = request.args.get('limit', default = 10, type = int)
    if limit_val < 0:
        limit_val = 10

    query = ("SELECT display_label FROM gene_autocomplete WHERE display_label like (%s) AND species = (%s) LIMIT %s")
    data_tuple = ("%{0}%".format(search_query), species_name, limit_val)
    cursor.execute(query, data_tuple)
    display_labels = cursor.fetchall()
    print(display_labels)
    results = [item[0] for item in display_labels]
    cursor.close()
    conn.close()

    return jsonify(results)


if __name__ == "__main__":
    app.run()