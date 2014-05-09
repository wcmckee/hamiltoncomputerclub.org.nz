# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1399666896.243835
_enable_loop = True
_template_filename = u'themes/readable/templates/base.tmpl'
_template_uri = u'base.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'extra_head', u'sourcelink', u'belowtitle']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.TemplateNamespace(u'base', context._clean_inheritance_tokens(), templateuri=u'base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'base')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        def extra_head():
            return render_extra_head(context.locals_(__M_locals))
        body_end = _import_ns.get('body_end', context.get('body_end', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        def sourcelink():
            return render_sourcelink(context.locals_(__M_locals))
        search_form = _import_ns.get('search_form', context.get('search_form', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        content_footer = _import_ns.get('content_footer', context.get('content_footer', UNDEFINED))
        def content():
            return render_content(context.locals_(__M_locals))
        rel_link = _import_ns.get('rel_link', context.get('rel_link', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        blog_url = _import_ns.get('blog_url', context.get('blog_url', UNDEFINED))
        def belowtitle():
            return render_belowtitle(context.locals_(__M_locals))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        set_locale = _import_ns.get('set_locale', context.get('set_locale', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(unicode(set_locale(lang)))
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(unicode(base.html_headstart()))
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        # SOURCE LINE 7
        __M_writer(u'\n')
        # SOURCE LINE 8
        __M_writer(unicode(template_hooks['extra_head']()))
        __M_writer(u'\n</head>\n<body>\n<div class="container" id="container">\n    <!--Body content-->\n    <!--End of body content-->\n    <div>\n    <a href="')
        # SOURCE LINE 15
        __M_writer(unicode(blog_url))
        __M_writer(u'"><h1>')
        __M_writer(unicode(blog_title))
        __M_writer(u'</h1></a>\n    </div>\n    <div id="content">\n        ')
        # SOURCE LINE 18
        __M_writer(unicode(template_hooks['page_header']()))
        __M_writer(u'\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 19
        __M_writer(u'\n    </div>\n    <div class="row-fluid">\n        <div class="span6" style="text-align: right; border-right: 2px solid #ccc; padding-right: 20px;">\n            <ul class="unstyled bottom">\n')
        # SOURCE LINE 24
        for url, text in navigation_links[lang]:
            # SOURCE LINE 25
            if rel_link(permalink, url) == "#":
                # SOURCE LINE 26
                __M_writer(u'                        <li class="active"><a href="')
                __M_writer(unicode(url))
                __M_writer(u'">')
                __M_writer(unicode(text))
                __M_writer(u'</a>\n')
                # SOURCE LINE 27
            else:
                # SOURCE LINE 28
                __M_writer(u'                        <li><a href="')
                __M_writer(unicode(url))
                __M_writer(u'">')
                __M_writer(unicode(text))
                __M_writer(u'</a>\n')
        # SOURCE LINE 31
        __M_writer(u'                ')
        __M_writer(unicode(template_hooks['menu']()))
        __M_writer(u'\n            </ul>\n        </div>\n        <div class="span6" style="margin-left: 20px;">\n            <ul class="unstyled bottom">\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'belowtitle'):
            context['self'].belowtitle(**pageargs)
        

        # SOURCE LINE 46
        __M_writer(u'\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        # SOURCE LINE 47
        __M_writer(u'\n            <li>Shares: <div id="share"></div></li>\n            </ul>\n            <div>\n')
        # SOURCE LINE 51
        if search_form:
            # SOURCE LINE 52
            __M_writer(u'                ')
            __M_writer(unicode(search_form))
            __M_writer(u'\n')
        # SOURCE LINE 54
        __M_writer(u'            ')
        __M_writer(unicode(template_hooks['menu_alt']()))
        __M_writer(u'\n            </div>\n        </div>\n    </div>\n    <hr>\n    <div class="footer">\n    ')
        # SOURCE LINE 60
        __M_writer(unicode(content_footer))
        __M_writer(u'\n    ')
        # SOURCE LINE 61
        __M_writer(unicode(template_hooks['page_footer']()))
        __M_writer(u'\n    </div>\n</div>\n    ')
        # SOURCE LINE 64
        __M_writer(unicode(base.late_load_js()))
        __M_writer(u'\n    <script type="text/javascript" src="/assets/js/jquery.sharrre-1.3.4.min.js"></script>\n    <script type="text/javascript">\n        jQuery("a.image-reference").colorbox({rel:"gal",maxWidth:"80%",maxHeight:"80%",scalePhotos:true});\n        $(\'#share\').sharrre({\n        share: {\n            googlePlus: true,\n            twitter: true\n        },\n        buttons: {\n            googlePlus: {annotation:\'bubble\'},\n            twitter: {count: \'horizontal\'}\n        },\n        hover: function(api, options){\n            $(api.element).find(\'.buttons\').show();\n        },\n        hide: function(api, options){\n            $(api.element).find(\'.buttons\').hide();\n        },\n        enableTracking: true,\n        urlCurl: ""\n        });\n    </script>\n    ')
        # SOURCE LINE 87
        __M_writer(unicode(body_end))
        __M_writer(u'\n    ')
        # SOURCE LINE 88
        __M_writer(unicode(template_hooks['body_end']()))
        __M_writer(u'\n</body>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        # SOURCE LINE 47
        __M_writer(u' ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_belowtitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        def belowtitle():
            return render_belowtitle(context)
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        rel_link = _import_ns.get('rel_link', context.get('rel_link', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 36
        __M_writer(u'\n')
        # SOURCE LINE 37
        if len(translations) > 1:
            # SOURCE LINE 38
            __M_writer(u'                    <li>\n')
            # SOURCE LINE 39
            for langname in translations.keys():
                # SOURCE LINE 40
                if langname != lang:
                    # SOURCE LINE 41
                    __M_writer(u'                            <a href="')
                    __M_writer(unicode(rel_link(permalink, _link("index", None, langname))))
                    __M_writer(u'">')
                    __M_writer(unicode(messages[langname]["LANGUAGE"]))
                    __M_writer(u'</a>\n')
            # SOURCE LINE 44
            __M_writer(u'                    </li>\n')
        # SOURCE LINE 46
        __M_writer(u'            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


