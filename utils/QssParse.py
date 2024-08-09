from PySideComponent.tailwind_colors import TAILWIND_COLORS


def toString(key:str,value:str):
    return f"{key}:{value};"

def toQss(selector,style_sheet):
    style = ""
    for properties,value in style_sheet.items():
        style += toString(properties,value)
    qss = selector + "{" + style + "}"
    return qss

style_sheet = {
    "background-color": TAILWIND_COLORS.ZINC_900,
    "color": TAILWIND_COLORS.ZINC_100,
    "padding":"8px 16px"
}