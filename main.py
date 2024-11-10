from flask import Flask, request, render_template
from waitress import serve
from lib import get
import configparser

Retrofter = Flask(__name__)  
  
@Retrofter.route('/get-post', methods=['GET'])  
def post():  
    blog_id = request.args.get('blog_id', '836827109')
    post_id = request.args.get('post_id', '7733666170')
    posts = get.get_post(blog_id, post_id)['posts']
    for i in posts:
         title = i['post']['title']  
         content = i['post']['content']
    return render_template('post.html', title=title, content=content)

@Retrofter.route('/get-collection', methods=['GET'])  
def collection():  
    collection_id = request.args.get('collection_id', '19697033')
    limit_once = request.args.get('limit_once', '10')
    collection = get.get_collection_list(collection_id,  0, limit_once)
    post_count = collection['collection']['postCount']
    blog_id = collection['collection']['blogId']
    collection_name = collection['collection']['name']
    
    collection_list = []
    for i in range(0, int(post_count), int(limit_once)):
        collection_list += get.get_collection_list(collection_id,  i, limit_once)['items']
    
    html_parts = []  
    title_list = []
    for i, c in enumerate(collection_list):
            title = c['post']['title']
            postid = c['post']['id']          
            title_list.append(title)
            additional_html_fragments = f'<li><a href="/get-post?blog_id={blog_id}&post_id={postid}">{title}</a></li>\n        '  
            html_parts.extend(additional_html_fragments)  
            html_item = "".join(html_parts)
    return render_template('collection.html', collection_name=collection_name, html_item=html_item)

@Retrofter.route('/')  
def read_index():  
    return render_template('index.html')

if __name__ == '__main__':
    config = configparser.ConfigParser() 
    config.read('config.ini')
    bind = config.get('Server', 'bind')
    port = config.getint('Server', 'port')
    threads = config.getint('Server', 'threads')
    serve(Retrofter, host=bind, port=port, threads=threads)
    