
from flask import Flask
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
import json
import sys
import logging
from logging.handlers import RotatingFileHandler

# # change routing of logs when running docker 
# logging.basicConfig(stream=sys.stderr) 

app = Flask(__name__)

@app.route("/")
def index():
  print('Rendering index template')
  return render_template("index.html")

# post request
@app.route('/', methods=['GET','POST'])
def python_function():
  import flask 
  import make_enr_clust
  import json 
  import json_scripts 
  import sys
  import cookielib, poster, urllib2, json

  error = None 

  # get the number of enriched terms 
  num_terms = int(request.form['num_terms'])

  # get the genes from the request 
  inst_genes = request.form['genes'].strip().split('\n')

  # convert to uppercase 
  inst_genes = [x.upper().strip() for x in inst_genes]

  # obtain unique genes 
  inst_genes = list(set(inst_genes))

  # get the gmt name
  gmt_name = request.form['gmt_name']

  # temporariy change
  gmt_name = 'GO_Biological_Process'

  # calc enrichment and cluster 
  network = make_enr_clust.main(gmt_name, inst_genes, num_terms, 'jaccard')

  # jsonify a list of dicts 
  return flask.jsonify( network )


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
 