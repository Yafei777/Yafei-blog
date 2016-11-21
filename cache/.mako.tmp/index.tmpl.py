# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1479703241.067067
_enable_loop = True
_template_filename = '/Users/ek777/miniconda2/envs/nikola/lib/python3.5/site-packages/nikola/data/themes/base/templates/index.tmpl'
_template_uri = 'index.tmpl'
_source_encoding = 'utf-8'
_exports = ['content_header', 'content', 'extra_head']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content_header():
            return render_content_header(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        pagekind = context.get('pagekind', UNDEFINED)
        index_file = context.get('index_file', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        parent = context.get('parent', UNDEFINED)
        index_teasers = context.get('index_teasers', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        _link = context.get('_link', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        front_index_header = context.get('front_index_header', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_header():
            return render_content_header(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_header():
            return render_content_header(context)
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        index_teasers = context.get('index_teasers', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        _link = context.get('_link', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        front_index_header = context.get('front_index_header', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        pagekind = context.get('pagekind', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        def content():
            return render_content(context)
        posts = context.get('posts', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_header'):
            context['self'].content_header(**pageargs)
        

        __M_writer('\n')
        if 'main_index' in pagekind:
            __M_writer('    ')
            __M_writer(str(front_index_header))
            __M_writer('\n')
        __M_writer('<div class="postindex">\n')
        for post in posts:
            __M_writer('    <article class="h-entry post-')
            __M_writer(str(post.meta('type')))
            __M_writer('">\n    <header>\n        <h1 class="p-name entry-title"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" class="u-url">')
            __M_writer(filters.html_escape(str(post.title())))
            __M_writer('</a></h1>\n        <div class="metadata">\n            <p class="byline author vcard"><span class="byline-name fn">\n')
            if author_pages_generated:
                __M_writer('                <a href="')
                __M_writer(str(_link('author', post.author())))
                __M_writer('">')
                __M_writer(filters.html_escape(str(post.author())))
                __M_writer('</a>\n')
            else:
                __M_writer('                ')
                __M_writer(filters.html_escape(str(post.author())))
                __M_writer('\n')
            __M_writer('            </span></p>\n            <p class="dateline"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" rel="bookmark"><time class="published dt-published" datetime="')
            __M_writer(str(post.formatted_date('webiso')))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('">')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('</time></a></p>\n')
            if not post.meta('nocomments') and site_has_comments:
                __M_writer('                <p class="commentline">')
                __M_writer(str(comments.comment_link(post.permalink(), post._base_path)))
                __M_writer('\n')
            __M_writer('        </div>\n    </header>\n')
            if index_teasers:
                __M_writer('    <div class="p-summary entry-summary">\n    ')
                __M_writer(str(post.text(teaser_only=True)))
                __M_writer('\n')
            else:
                __M_writer('    <div class="e-content entry-content">\n    ')
                __M_writer(str(post.text(teaser_only=False)))
                __M_writer('\n')
            __M_writer('    </div>\n    </article>\n')
        __M_writer('</div>\n')
        __M_writer(str(helper.html_pager()))
        __M_writer('\n')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n')
        __M_writer(str(helper.mathjax_script(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        posts = context.get('posts', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        index_file = context.get('index_file', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if posts and (permalink == '/' or permalink == '/' + index_file):
            __M_writer('        <link rel="prefetch" href="')
            __M_writer(str(posts[0].permalink()))
            __M_writer('" type="text/html">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "index.tmpl", "filename": "/Users/ek777/miniconda2/envs/nikola/lib/python3.5/site-packages/nikola/data/themes/base/templates/index.tmpl", "line_map": {"128": 27, "129": 28, "130": 28, "131": 28, "132": 30, "133": 31, "134": 31, "135": 31, "136": 31, "137": 31, "138": 31, "139": 31, "140": 31, "141": 32, "142": 33, "143": 33, "144": 33, "145": 35, "146": 37, "147": 38, "148": 39, "149": 39, "150": 40, "23": 2, "152": 42, "153": 42, "26": 3, "155": 47, "156": 48, "154": 44, "158": 49, "159": 49, "32": 0, "161": 50, "167": 6, "157": 48, "177": 6, "178": 7, "179": 7, "180": 8, "181": 9, "182": 9, "183": 9, "56": 2, "57": 3, "58": 4, "151": 41, "189": 183, "63": 11, "160": 50, "68": 51, "74": 14, "85": 13, "103": 13, "108": 14, "109": 15, "110": 16, "111": 16, "112": 16, "113": 18, "114": 19, "115": 20, "116": 20, "117": 20, "118": 22, "119": 22, "120": 22, "121": 22, "122": 25, "123": 26, "124": 26, "125": 26, "126": 26, "127": 26}, "source_encoding": "utf-8"}
__M_END_METADATA
"""