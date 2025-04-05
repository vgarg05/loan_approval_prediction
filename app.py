from flask import Flask, render_template, request, redirect
import pickle
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

grid = pickle.load(open("models/grid.pkl", "rb"))
standard_scaler = pickle.load(open("models/scaler.pkl", "rb"))

@app.route("/")
def home():
    return redirect("/predict")
    

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        try:
            person_age = float(request.form.get('person_age'))
            person_gender = float(request.form.get('person_gender'))
            person_income = float(request.form.get('person_income'))
            person_emp_exp = float(request.form.get('person_emp_exp'))
            loan_amnt = float(request.form.get('loan_amnt'))
            loan_int_rate = float(request.form.get('loan_int_rate'))
            loan_percent_income = float(request.form.get('loan_percent_income'))
            cb_person_cred_hist_length = float(request.form.get('cb_person_cred_hist_length'))
            credit_score = float(request.form.get('credit_score'))
            previous_loan_defaults_on_file = float(request.form.get('previous_loan_defaults_on_file'))

            data_scaled = standard_scaler.transform([[person_age, person_gender, person_income, person_emp_exp,
                                                      loan_amnt, loan_int_rate, loan_percent_income,
                                                      cb_person_cred_hist_length, credit_score,
                                                      previous_loan_defaults_on_file]])

            result = grid.predict(data_scaled)
            message = "Loan is approved!" if result == 1 else "Loan is not approved."
            return render_template("form.html", results=message)

        except Exception as e:
            return f"Error occurred: {e}"
    else:
        return render_template("form.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
