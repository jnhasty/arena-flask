# -*- coding: utf-8 -*

from flask import Flask, request, session, url_for, redirect, \
     render_template, abort, g, flash

from arenapy import ArenaPy

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

@app.route('/user/')
def user():
    arena = ArenaPy()

    user_string = 'john-michael-boling';
    user_channel = arena.get_channel(user_string);
    profile_channel = arena.get_user_channel(user_string);
    nav_channels = arena.get_channel_channels(profile_channel);

    # get the requested channel if one
    request_channel = request.args.get('channel');

    if request_channel:
        content_channel = arena.get_channel(request_channel);
        content_blocks = arena.get_channel_blocks(content_channel);
        connections = arena.get_channel_connections(content_channel);
    else: 
        content_blocks = arena.get_channel_blocks(user_channel);
        connections = arena.get_channel_connections(user_channel);
    

    # get sorted blocks to use as content
    sorted_blocks = arena.sort_blocks_by_created(content_blocks)

    return render_template('user.html', 
            profile_channel = profile_channel,
            nav_channels = nav_channels,
            sorted_blocks = sorted_blocks,
            connections = connections,
            )


@app.route('/channel/')
def channel():

    arena = ArenaPy()

    #get the channel you want to show
    page_channel = arena.get_channel('arena-influences')
    nav_items = arena.get_channel_content(page_channel)
    
    requested_item = None

    if request.args.get('block'):
        requested_item = request.args.get('block')
        current_item = arena.get_block(requested_item)
        blocks = [current_item]
        connections = arena.get_connections_for_block(current_item)
    
    if request.args.get('channel'):
        requested_item = request.args.get('channel')
        current_item = arena.get_channel(requested_item)
        connections = arena.get_channel_connections(current_item)
        blocks =  arena.get_channel_blocks(current_item)
    
    if not requested_item:
        # if nothing requested, get first item
        current_item = nav_items[0]
        blocks = [current_item]
        connections = arena.get_connections_for_block(current_item)
    
    return render_template('channel.html', 
            page_channel = page_channel,
            nav_items = nav_items,
            blocks = blocks,
            connections = connections,
            )

@app.route('/blog/')
def channel():

    arena = ArenaPy()
    channel = arena.get_channel('arena-influences')
    channel_blocks = arena.get_channel_blocks(channel)
    blog_content = arena.sort_blocks_by_created(channel_blocks)

    return render_template('blog.html',
            channel = channel,
            channel_blocks = channel_blocks,
            blog_content = blog_content,
            )

        

# run the app
if __name__ == '__main__':
    app.run()
