# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1399666896.852004
_enable_loop = True
_template_filename = u'themes/readable/templates/index.tmpl'
_template_uri = u'index.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 3
    ns = runtime.TemplateNamespace(u'comments', context._clean_inheritance_tokens(), templateuri=u'comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'comments')] = ns

    # SOURCE LINE 2
    ns = runtime.TemplateNamespace(u'helper', context._clean_inheritance_tokens(), templateuri=u'index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'helper')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        date_format = context.get('date_format', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        messages = context.get('messages', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context.locals_(__M_locals))
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        index_teasers = context.get('index_teasers', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 28
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        date_format = context.get('date_format', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        messages = context.get('messages', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        index_teasers = context.get('index_teasers', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'\n')
        # SOURCE LINE 6
        for post in posts:
            # SOURCE LINE 7
            __M_writer(u'        <div class="postdiv">\n        <a href="')
            # SOURCE LINE 8
            __M_writer(unicode(post.permalink()))
            __M_writer(u'"><h2>')
            __M_writer(unicode(post.title()))
            __M_writer(u'</a></h2>\n        ')
            # SOURCE LINE 9
            __M_writer(unicode(post.text(teaser_only=index_teasers)))
            __M_writer(u'\n        <p>\n        </div>\n        <div class="postmeta">\n        <small>&nbsp;\xa7&nbsp;\n            <span class="dateline"><a href="')
            # SOURCE LINE 14
            __M_writer(unicode(post.permalink()))
            __M_writer(u'" rel="bookmark"><time class="published dt-published" datetime="')
            __M_writer(unicode(post.date.isoformat()))
            __M_writer(u'" itemprop="datePublished" title="')
            __M_writer(unicode(messages("Publication date")))
            __M_writer(u'">')
            __M_writer(unicode(post.formatted_date(date_format)))
            __M_writer(u'</time></a></span>\n        </small>\n')
            # SOURCE LINE 16
            if not post.meta('nocomments') and site_has_comments:
                # SOURCE LINE 17
                __M_writer(u'             \xb7 ')
                __M_writer(unicode(comments.comment_link(post.permalink(), post.base_path)))
                __M_writer(u'\n')
            # SOURCE LINE 19
            for tag in post.tags:
                # SOURCE LINE 20
                __M_writer(u'             \xb7 ')
                __M_writer(unicode(tag))
                __M_writer(u'\n')
            # SOURCE LINE 22
            __M_writer(u'        </div>\n        <hr>\n')
        # SOURCE LINE 25
        __M_writer(u'    ')
        __M_writer(unicode(helper.html_pager()))
        __M_writer(u'\n    ')
        # SOURCE LINE 26
        __M_writer(unicode(comments.comment_link_script()))
        __M_writer(u'\n\t')
        # SOURCE LINE 27
        __M_writer(unicode(helper.mathjax_script(posts)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


