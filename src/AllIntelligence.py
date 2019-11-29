from flask import Flask, Response, render_template, request, session                                                                                                                      
from allintelligence import osint, tech 

app = Flask(__name__)                                                                                                                                                                          


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    domain = request.form['domain']

    # To-Do: domain validation

    config = {
        'hunter': request.form.get('switchHunter', False),
        'pipl': request.form.get('switchPipl', False),
        'dehashed': request.form.get('switchDehashed', False),
    }

    tech_information = tech.analyze(domain)
    osint_information = osint.analyze(domain, config)

    return render_template('report.html', tech_information=tech_information, osint_information=osint_information)


if __name__ == '__main__':                                                                                                                                                                     
    app.run(debug=True)
