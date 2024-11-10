import json
import requests

def get_collection_list(collection_id, offset, limit=15, authkey=None, order=1):
    # 获取合集详情，包括列表
    # order为返回顺序
    url = "https://api.lofter.com/v1.1/postCollection.api"

    params = {
    'product': "lofter-android-7.6.12"
    }

    # payload = f"method=getCollectionDetail&offset={offset}&limit={limit}&collectionid={collection_id}&blogid={blog_id}&order={order}"
    payload = f"method=getCollectionDetail&offset={offset}&limit={limit}&collectionid={collection_id}&order={order}"

    headers = {
#    'Accept-Encoding': "br,gzip",
    'content-type': "application/x-www-form-urlencoded; charset=utf-8",
    }

    response = requests.post(url, params=params, data=payload, headers=headers)

    return json.loads(response.text)['response']

def get_post(blog_id, post_id):
    # 获取文章详情
    url = "http://api.lofter.com/oldapi/post/detail.api"

    params = {
    'product': "lofter-android-7.6.12"
    }

    payload = f"targetblogid={blog_id}&supportposttypes=1%2C2%2C3%2C4%2C5%2C6&offset=0&requestType=1&postdigestnew=1&postid={post_id}&blogId={blog_id}&checkpwd=1&needgetpoststat=1"

    headers = {
    'User-Agent': "LOFTER-Android 7.6.12 (V2272A; Android 13; null) WIFI",
#    'Accept-Encoding': "br,gzip",
    'Content-Type': "application/x-www-form-urlencoded",
    'lofproduct': "lofter-android-7.6.12",
    }

    response = requests.post(url, params=params, data=payload, headers=headers)

    if response.status_code == 200:
        return json.loads(response.text)['response']
    else:
        return None
