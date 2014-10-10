# coding: utf-8

from django.http import HttpResponse
from django.template import loader
from django.template import RequestContext
#from django.contrib.auth.decorators import login_required


from cms.models import Post


#@login_required
def post(request, post_id):

    # 通常の取得
    # post = Post.objects.get(id=post_id)

    # 関連オブジェクトを取得（JOIN)
    post = Post.objects.select_related().get(id=post_id)

    c = RequestContext(request, {
        "post": post,
    })

    t = loader.get_template('cms/post.html')

    return HttpResponse(t.render(c))