from flask import Flask, render_template, request,redirect,url_for,session,jsonify
from db import connect_db
from function import *
import secrets

app = Flask(__name__)
secret_key = secrets.token_hex(16)
app.secret_key = secret_key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if any of the fields are empty
        if not name or not username or not password:
            error_message = "All fields are required!"
            return render_template('register.html', error_message=error_message)
        if '@' not in username:
            error_message = "Please enter a valid username address "
            return render_template('register.html', error_message=error_message)


        conn = connect_db()
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM login WHERE username = %s", (username,))
        existing_user = cur.fetchone()
        if existing_user:
            error_message = "Username already taken. Please choose a different one."
            cur.close()
            conn.close()
            return render_template('register.html', error_message=error_message)

        try:
            cur.execute("INSERT INTO login (name, username, password, usertype) VALUES (%s, %s, %s, %s)", (name, username, password, 'user'))
            conn.commit()
            cur.close()
            conn.close()
            message = "Registration successful!"
            return render_template('login.html', message=message)
        except Exception as e:
            return f'Error: {str(e)}', 500

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        conn = connect_db()
        cur = conn.cursor()

        cur.execute("SELECT name, usertype FROM login WHERE username = %s AND password = %s", (username, password))
        user = cur.fetchone()

        cur.close()
        conn.close()

        if user:
            name, usertype = user
            session['username'] = username  # Store username in session
            if usertype == 'admin':
                return render_template('admin1.html', name=name)
            elif usertype == 'user':
                return render_template('admin.html', name=name)
        else:
            return render_template('login.html', message="Invalid username or password")

    return render_template('login.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/admin1')
def admin1():
    return render_template('admin1.html')

@app.route('/bmi_calculator', methods=['GET', 'POST'])
def bmi():
    return render_template('bmi.html')
#------------------------------------------------------------------------------
@app.route('/bmi_normal', methods=['GET', 'POST'])
def bmi_normal():
    vegetarian_plans, non_vegetarian_plans = load_normal_diet_plans()
    
    vegetarian_plan = random.choice(vegetarian_plans)
    non_vegetarian_plan = random.choice(non_vegetarian_plans)
    category = request.args.get('category')
    bmi = float(request.args.get('bmi', 0))
    return render_template('normal.html', vegetarian_diet=vegetarian_plan['plan'], non_vegetarian_diet=non_vegetarian_plan['plan'], title=vegetarian_plan['title'],category=category, bmi=bmi)

@app.route('/normal_exercise', methods=['GET', 'POST'])
def normal_exercise():
    return render_template('normal_exercise.html')

@app.route('/normal_doctor', methods=['GET', 'POST'])
def normal_doctor():
    return render_template('normal_doctor.html')

#------------------------------------------------------------------------------
@app.route('/mild_thinness', methods=['GET', 'POST'])
def underweight():
    vegetarian_plans, non_vegetarian_plans = load_mild_diet_plans()
    category = request.args.get('category')
    bmi = float(request.args.get('bmi', 0))
    vegetarian_plan = random.choice(vegetarian_plans)
    non_vegetarian_plan = random.choice(non_vegetarian_plans)
    
    return render_template('underweight.html', vegetarian_diet=vegetarian_plan['plan'], non_vegetarian_diet=non_vegetarian_plan['plan'], title=vegetarian_plan['title'],category=category, bmi=bmi)


@app.route('/mild_exercise', methods=['GET', 'POST'])
def underweight_exercise():
    return render_template('underweight_exercise.html')

@app.route('/mild_doctor', methods=['GET', 'POST'])
def underweight_doctor():
    return render_template('underweight_doctor.html')

#------------------------------------------------------------------------------

@app.route('/overweight', methods=['GET', 'POST'])
def overweight():
    vegetarian_plans, non_vegetarian_plans = load_overweight_diet_plans()
    category = request.args.get('category')
    bmi = float(request.args.get('bmi', 0))
    vegetarian_plan = random.choice(vegetarian_plans)
    non_vegetarian_plan = random.choice(non_vegetarian_plans)
    
    return render_template('overweight.html', vegetarian_diet=vegetarian_plan['plan'], non_vegetarian_diet=non_vegetarian_plan['plan'], title=vegetarian_plan['title'],category=category, bmi=bmi)


@app.route('/overweight_exercise', methods=['GET', 'POST'])
def overweight_exercise():
    return render_template('overweight_exercise.html')

@app.route('/overweight_doctor', methods=['GET', 'POST'])
def overweight_doctor():
    return render_template('overweight_doctor.html')

#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
@app.route('/severe_thinness', methods=['GET', 'POST'])
def severe_thinness():
    vegetarian_plans, non_vegetarian_plans = load_severe_diet_plans()
    category = request.args.get('category')
    bmi = float(request.args.get('bmi', 0))
    vegetarian_plan = random.choice(vegetarian_plans)
    non_vegetarian_plan = random.choice(non_vegetarian_plans)
    
    return render_template('severe_thinness.html', vegetarian_diet=vegetarian_plan['plan'], non_vegetarian_diet=non_vegetarian_plan['plan'], title=vegetarian_plan['title'],category=category, bmi=bmi)

@app.route('/severe_exercise', methods=['GET', 'POST'])
def severe_exercise():
    return render_template('severe_thinness_exercise.html')

@app.route('/severe_doctor', methods=['GET', 'POST'])
def severe_doctor():
    return render_template('severe_thinness_doctor.html')
#------------------------------------------------------------------------------

@app.route('/moderate_thinness', methods=['GET', 'POST'])
def moderate_thinness():
    vegetarian_plans, non_vegetarian_plans = load_moderate_diet_plans()
    category = request.args.get('category')
    bmi = float(request.args.get('bmi', 0))
    vegetarian_plan = random.choice(vegetarian_plans)
    non_vegetarian_plan = random.choice(non_vegetarian_plans)
    
    return render_template('moderate_thinness.html', vegetarian_diet=vegetarian_plan['plan'], non_vegetarian_diet=non_vegetarian_plan['plan'], title=vegetarian_plan['title'],category=category, bmi=bmi)

    

@app.route('/moderate_exercise', methods=['GET', 'POST'])
def moderate_exercise():
    return render_template('moderate_thinness_exercise.html')

@app.route('/moderate_doctor', methods=['GET', 'POST'])
def moderate_doctor():
    return render_template('moderate_thinness_doctor.html')

#------------------------------------------------------------------------------

#------------------------------------------------------------------------------

@app.route('/obese', methods=['GET', 'POST'])
def obese():
    vegetarian_plans, non_vegetarian_plans = load_obese_class_1_diet_plans()
    category = request.args.get('category')
    bmi = float(request.args.get('bmi', 0))
    vegetarian_plan = random.choice(vegetarian_plans)
    non_vegetarian_plan = random.choice(non_vegetarian_plans)
    
    return render_template('obese.html', vegetarian_diet=vegetarian_plan['plan'],category=category, bmi=bmi, non_vegetarian_diet=non_vegetarian_plan['plan'], title=vegetarian_plan['title'])


@app.route('/obese_exercise', methods=['GET', 'POST'])
def obese_exercise():
    return render_template('obese_exercise.html')

@app.route('/obese_doctor', methods=['GET', 'POST'])
def obese_doctor():
    return render_template('obese_doctor.html')

#------------------------------------------------------------------------------

@app.route('/obese2', methods=['GET', 'POST'])
def obese_2():
    vegetarian_plans, non_vegetarian_plans = load_obese_class_2_diet_plans()
    category = request.args.get('category')
    bmi = float(request.args.get('bmi', 0))
    vegetarian_plan = random.choice(vegetarian_plans)
    non_vegetarian_plan = random.choice(non_vegetarian_plans)
    
    return render_template('obese_2.html', vegetarian_diet=vegetarian_plan['plan'],category=category, bmi=bmi, non_vegetarian_diet=non_vegetarian_plan['plan'], title=vegetarian_plan['title'])


@app.route('/obese_2_exercise', methods=['GET', 'POST'])
def obese_2_exercise():
    return render_template('obese_2_exercise.html')

@app.route('/obese_2_doctor', methods=['GET', 'POST'])
def obese_2_doctor():
    return render_template('obese_2_doctor.html')

#------------------------------------------------------------------------------

@app.route('/obese_3', methods=['GET', 'POST'])
def obese_3():
    vegetarian_plans, non_vegetarian_plans = load_obese_class_3_diet_plans()
    category = request.args.get('category')
    bmi = float(request.args.get('bmi', 0))
    vegetarian_plan = random.choice(vegetarian_plans)
    non_vegetarian_plan = random.choice(non_vegetarian_plans)
    
    return render_template('obese_3.html', vegetarian_diet=vegetarian_plan['plan'],category=category, bmi=bmi, non_vegetarian_diet=non_vegetarian_plan['plan'], title=vegetarian_plan['title'])


@app.route('/obese_3_exercise', methods=['GET', 'POST'])
def obese_3_exercise():
    return render_template('obese_3_exercise.html')

@app.route('/obese_3_doctor', methods=['GET', 'POST'])
def obese_3_doctor():
    return render_template('obese_3_doctor.html')
    
#------------------------------------------------------------------------------

@app.route('/less_age', methods=['GET', 'POST'])
def less_age():
    return render_template('less_age.html')

    
@app.route('/viewuser')
def manage_users():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM bmi")
    users = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('manage_users.html', users=users, enumerate=enumerate)


@app.route('/logout')
def logout():
    return render_template('index.html') 

@app.route('/submit', methods=['POST'])
def submit():
    if 'username' not in session:
        return jsonify({'status': 'error', 'message': 'User not logged in'}), 403

    try:
        username = session['username']
        gender = request.form.get('gender')
        age = int(request.form.get('age'))
        height = float(request.form.get('height'))
        weight = float(request.form.get('weight'))

        # Calculate BMI
        bmi = weight / (height / 100) ** 2

        # Determine category based on age and BMI
        if age <= 16:
            category = 'Less Age'
            redirect_url = url_for('less_age', category=category, bmi=bmi)
        elif bmi <= 16:
            category = 'Severe Thinness'
            redirect_url = url_for('severe_thinness', category=category, bmi=bmi)
        elif 16 < bmi <= 17:
            category = 'Moderate Thinness'
            redirect_url = url_for('moderate_thinness', category=category, bmi=bmi)
        elif 17 < bmi <= 18.5:
            category = 'Mild Thinness'
            redirect_url = url_for('mild_thinness', category=category, bmi=bmi)
        elif 18.5 < bmi < 25:
            category = 'Normal'
            redirect_url = url_for('bmi_normal', category=category, bmi=bmi)
        elif 25 <= bmi < 30:
            category = 'Overweight'
            redirect_url = url_for('overweight', category=category, bmi=bmi)
        elif 30 <= bmi < 35:
            category = 'Obese Class-1'
            redirect_url = url_for('obese', category=category, bmi=bmi)
        elif 35 <= bmi < 40:
            category = 'Obese Class-2'
            redirect_url = url_for('obese2', category=category, bmi=bmi)
        else:
            category = 'Obese Class-3'
            redirect_url = url_for('obese_3', category=category, bmi=bmi)

        # Insert data into PostgreSQL table
        conn = connect_db()
        cur = conn.cursor()
        insert_query = """
            INSERT INTO public.bmi (age, height, weight, bmi, username, gender, category)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cur.execute(insert_query, (age, height, weight, bmi, username, gender, category))
        conn.commit()
        cur.close()
        conn.close()

        # Return a success response
        return redirect(redirect_url)

    except Exception as e:
        # Return an error response
        return jsonify({'status': 'error', 'message': str(e)}), 400



if __name__ == '__main__':
    app.run(debug=True)
