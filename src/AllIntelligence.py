from flask import Flask, Response, render_template, request                                                                                                                         

import allintelligence


app = Flask(__name__)                                                                                                                                                                          


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    domain = request.form['domain'] 

    # To-Do: email validation 
 
    tech_information = allintelligence.tech.analyze(domain)
    osint_information = allintelligence.osint.analyze(domain)
    return render_template('report.html', tech_information=tech_information, osint_information=osint_information)


if __name__ == '__main__':                                                                                                                                                                     
    app.debug = True                                                                                                                                                                           
    app.run()
