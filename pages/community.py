from flask import jsonify, render_template, request, Response
from flask.ext.login import current_user, login_user
from functions import app
from models import User
from models._helpers import db
import sqlalchemy


@app.route('/community', methods=['GET'])
def community():

    # users = User.query.order_by('-signup_date').limit(5).all()
    sql_query = db.engine.execute('''SELECT display_name, tier, point_balance
    FROM user 
    ORDER BY signup_date DESC
    LIMIT 5
    ''')
    args = {
            'gift_card_eligible': True,
            'cashout_ok': True,
            'user_below_silver': current_user.is_below_tier('Silver'),
            'sql_query': sql_query,
    }
    return render_template("community.html", **args)

