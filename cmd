pip install -U selenium
pip install behave
pip install behave-html-formatter
pip install -r requirements.txt

run test:
    behave -f html -o behave-report.html --tags=test
SAU
    behave -f html -o behave-ini-report.html