# -*- coding: utf-8 -*

from flask import Flask, request, session, url_for, redirect, \
     render_template, abort, g, flash

from arena import ArenaPy

app = Flask('arena-flask')
app.config.from_pyfile('settings.py')

@app.route('/')
def index():
    arenapy = ArenaPy()
    channel = arenapy.get_channel('paperweight')

    info =  arenapy.get_channel_channels_count(channel)

    return render_template('content.html', 
            content = channel['blocks'],
            channel = channel,
            info = info,
            )

if __name__ == '__main__':
    app.run()
