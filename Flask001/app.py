from flask import Flask
from flask import render_template
from flask import request, redirect, url_for
#new app
app = Flask(__name__)

blog = {
'name':'My first blog',
'posts': {}
}

@app.route('/')
#def home():
#    return 'Hello world!'
def home():
    return render_template('home.jinja2', blog=blog)

@app.route('/post/<int:post_id>')
def post(post_id):
    #post = blog['posts'][post_id] #crashes if key post_id doesn't exist
    #post = blog['posts'].get(post_id, 'Hello') #Hello if doesn't exist
    post = blog['posts'].get(post_id)
    #return post['title']
    if not post:
        return render_template('404.jinja2', message=f'The post {post_id} was not found')
    return render_template('post.jinja2', post_template=post)

@app.route('/post/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        post_id = len(blog['posts'])
        blog['posts'][post_id]={'title':title, 'content':content, 'post_id':post_id}
        return redirect(url_for('post',post_id=post_id)) #calling post method with arg post_id
    return render_template('create.html')


app.run()
