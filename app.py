# -*- coding: utf-8 -*

from flask import Flask, request, session, url_for, redirect, \
     render_template, abort, g, flash

import ArenaPy

# app settings
app = Flask('arena-flask')
app.config.from_pyfile('settings.py')

# views
@app.route('/')
def index():
    arenapy = ArenaPy()
    
    channel = arenapy.get_channel('arena-influences')
    title = arenapy.get_channel_title(channel)
    channel_blocks = channel.get('blocks')
    channel_blocks = arenapy.sort_blocks_by_created(channel_blocks)

    return render_template('content.html', 
            title = title,
            blocks = channel_blocks,
            )

# run the app
if __name__ == '__main__':
    app.run()
