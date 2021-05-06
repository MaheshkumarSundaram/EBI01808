# EMBL - EBI01808 Software Developer Technical Assessment

The code consists of 3 basic parts:
* ```app.py```: Flask instance
* ```config.py```: Configurations for MYSQL Database
* ```main.py```: API endpoint

Read the README files under each project for more details.

## Installation for Flask and MYSQL support

```
pip install Flask
pip install flask-mysql
pip install Flask-Cors
```


### Run the API

```
python main.py
```

URL:
```
http://127.0.0.1:5000/gene_suggest
```

```
http://127.0.0.1:5000/gene_suggest?query=<query_name>&species=<species_name>&limit=<limit_val>
```

*Default* parameters for query, species and limit are "brc", "homo_sapiens" and 10 respectively.
