from pyecharts import Liquid, Page
from .constants import WIDTH, HEIGHT


def liquid_charts():
    page = Page()

    chart = Liquid("水球图-单数据", width=WIDTH, height=HEIGHT)
    chart.add("Liquid", [0.6])
    page.add(chart)

    chart = Liquid("水球图-多数据", width=WIDTH, height=HEIGHT)
    chart.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_outline_show=False)
    page.add(chart)

    chart = Liquid("水球图-圆角", width=WIDTH, height=HEIGHT)
    chart.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_outline_show=False,
              shape='roundRect')
    page.add(chart)

    chart = Liquid("水球图-箭头", width=WIDTH, height=HEIGHT)
    chart.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_outline_show=False,
              shape='arrow')
    page.add(chart)

    chart = Liquid("水球图-动画静止", width=WIDTH, height=HEIGHT)
    chart.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_animation=False,
              shape='diamond')
    page.add(chart)

    return page
