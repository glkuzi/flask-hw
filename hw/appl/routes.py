# -*- coding: utf-8 -*-
from appl import app
from flask import render_template, flash, redirect, url_for, session
from appl.forms import Footnote
import datetime, redis, json
STORAGE = 'redis'
if STORAGE == 'redis':
    r = redis.Redis(host='redis', port=6379, db=0)
    #r = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/', methods=['GET', 'POST'])
@app.route('/start', methods=['GET', 'POST'])
def start():
    if STORAGE == 'session':
        session['notes'] = []
        session['times'] = []
    if STORAGE == 'redis':
        # r = redis.Redis(host='localhost', port=6379, db=0)
        r.set('notes', json.dumps([]))
        r.set('times', json.dumps([]))
    form = Footnote()
    if form.validate_on_submit():
        note = chr(13) +  form.footnote.data
        if STORAGE == 'session':
            session['note'] = note
            session['notes'].append({'note': note,
                                     'time': str(datetime.datetime.now())})
            session['times'].append(str(datetime.datetime.now()))
        if STORAGE == 'redis':
            notes = json.loads(r.get('notes'))
            notes.append(note)
            r.set('notes', json.dumps(notes))
            times = json.loads(r.get('times'))
            times.append(str(datetime.datetime.now()))
            r.set('times', json.dumps(times))
        return redirect(url_for('result'))
    return render_template('index.html', title='Note', form=form)


@app.route('/result', methods=['GET', 'POST'])
def result():
    if STORAGE == 'session':
        texts = session['notes']
    if STORAGE == 'redis':
        # r = redis.
        notes = json.loads(r.get('notes'))
        times = json.loads(r.get('times'))
        texts = []
        for note, time in zip(notes, times):
            texts.append({'note': note, 'time': time})
    form = Footnote()
    if form.validate_on_submit():
        note = chr(13) + form.footnote.data
        if STORAGE == 'session':
            session['note'] = note
            session['notes'].append({'note': note,
                                     'time': str(datetime.datetime.now())})
            session['times'].append(str(datetime.datetime.now()))
        if STORAGE == 'redis':
            notes = json.loads(r.get('notes'))
            notes.append(note)
            r.set('notes', json.dumps(notes))
            times = json.loads(r.get('times'))
            times.append(str(datetime.datetime.now()))
            r.set('times', json.dumps(times))
        return redirect(url_for('result'))
    return render_template('result.html',
                           texts=texts, form=form)
