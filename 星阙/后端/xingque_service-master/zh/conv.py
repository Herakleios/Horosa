import zhconv


def simple_to_traditional(simple_text):
    traditional_text = zhconv.convert(simple_text, 'zh-hant')
    return traditional_text


def traditional_to_simple(traditional_text):
    simple_text = zhconv.convert(traditional_text, 'zh-hans')
    return simple_text
