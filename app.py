@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            total_tips = float(request.form['total_tips'])
            num_bartenders = int(request.form['num_bartenders'])
            num_barbacks = int(request.form['num_barbacks'])
            num_bouncers = int(request.form['num_bouncers'])

            tip_distribution = calculate_tip_out(total_tips, num_bartenders, num_barbacks, num_bouncers)

            return render_template(
                'index.html',
                tip_distribution=tip_distribution,
                total_tips=total_tips,
                num_bartenders=num_bartenders,
                num_barbacks=num_barbacks,
                num_bouncers=num_bouncers
            )
        except ValueError:
            return render_template('index.html', error="Please enter valid numbers.")

    return render_template('index.html')

