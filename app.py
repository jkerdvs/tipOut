from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_tip_out(total_tips, num_bartenders, num_barbacks, num_bouncers):
    bartender_weight = 1
    barback_weight = 1/3
    bouncer_weight = 1/4
    total_weight = (num_bartenders * bartender_weight) + (num_barbacks * barback_weight) + (num_bouncers * bouncer_weight)

    if total_weight == 0:
        return {"error": "Total workers must be greater than zero"}

    tip_per_weight = total_tips / total_weight
    return {
        "Bartender": round(tip_per_weight * bartender_weight, 2),
        "Barback": round(tip_per_weight * barback_weight, 2),
        "Bouncer": round(tip_per_weight * bouncer_weight, 2)
    }

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            total_tips = float(request.form['total_tips'])
            num_bartenders = int(request.form['num_bartenders'])
            num_barbacks = int(request.form['num_barbacks'])
            num_bouncers = int(request.form['num_bouncers'])

            tip_distribution = calculate_tip_out(total_tips, num_bartenders, num_barbacks, num_bouncers)

            return render_template('index.html', tip_distribution=tip_distribution, total_tips=total_tips)
        except ValueError:
            return render_template('index.html', error="Please enter valid numbers.")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
