from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Event
from . import db

bp = Blueprint('routes', __name__)

@bp.route('/create', methods=['GET', 'POST'])
def create_event():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        date = request.form.get('date')
        location = request.form.get('location')

        new_event = Event(title=title, description=description, date=date, location=location)
        db.session.add(new_event)
        db.session.commit()
        flash('Event created successfully!', 'success')
        return redirect(url_for('routes.create_event'))

    return render_template('create_event.html')
