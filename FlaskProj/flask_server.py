from flask import Flask, render_template, send_file, request

"""
    First you want to make a flask "app"
        Class that flask made that allows us to run stuff.  
"""

my_app = Flask("My First Flask App")

html_main_page = \
    """
    <title>Hey This Worked</title>
    <body>
    This is a webpage
    </body>
    """


# @ decorator (don't ask)
# "/" just means the main page no additional page typed in.
@my_app.route('/')
def display_main_page():
    print('Attempting to render main page')
    return html_main_page


@my_app.route('/hamburger')
def display_hamburger():
    return render_template('hammy.html')


@my_app.route('/periodic')
def display_periodic_table():
    # we need to specify the variable that needs to be displayed.
    the_table = []
    with open('periodic_table.txt') as period_file:
        the_table = period_file.read().split()
    return render_template('periodic.html', periodic_table=the_table)


@my_app.route('/get_input', methods=['GET', 'POST'])
def get_some_user_input():
    the_answers = []
    if request.method == 'POST':
        our_name = request.form.get('username')
        the_quest = request.form.get('quest')
        fav_color = request.form.get('fav_color')
        fav_movie = request.form.get('fav_movie')
        fav_food = request.form.get('fav_food')
        the_answers = [our_name, the_quest, fav_color, fav_movie, fav_food]

    return render_template('user_form.html', answers=the_answers)


@my_app.route('/<image_name>.jpg')
def get_image(image_name):
    return send_file('static/' + image_name + '.jpg', mimetype="image/gif")


"""
    New goal: list all the elements from the periodic table.
        We are lazy, we dont' want to type all of them.  
"""

if __name__ == "__main__":
    # secret is that there's a while loop in this function.
    my_app.run(port=1729)
    # not port 80, 480
    # ports 0 - 32767
