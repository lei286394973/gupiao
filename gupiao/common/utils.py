#coding: utf-8
import re

def sub_string(target, max_length):
    """
    截取字符串
    target: 要操作的字符串
    max_length: 保留的最大长度
    """

    # 如果是unicode可以直接切
    if type(target) != type(u""):
        target = target.decode('utf-8')

    if len(target) > max_length:
        return target[: max_length] + u'...'
    else:
        return target


def get_summary_from_html(content, max_num=100):
    """
    @note: 通过内容获取摘要
    """
    summary = ''
    # 提取标签中的文字
    r = u'<.+?>([^\/\\\&\<\>]+?)</\w+?>'
    p = re.compile(r, re.DOTALL | re.IGNORECASE)
    rs = p.findall(content)
    for s in rs:
        if summary.__len__() > max_num:
            summary += '......'
            break
        if s:
            summary += s
    # 没有标签的
    if not summary:
        r = u'[\u4e00-\u9fa5\w\@]+'
        p = re.compile(r, re.DOTALL | re.IGNORECASE)
        rs = p.findall(content)
        for s in rs:
            if summary.__len__() > max_num:
                summary += '......'
                break
            if s:
                summary += s
    return summary