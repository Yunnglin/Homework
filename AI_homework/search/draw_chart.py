from pyecharts.charts import Bar, Tree
from pyecharts import options as opts
# 内置主题类型可查看 pyecharts.globals.ThemeType
from pyecharts.globals import ThemeType


# bar = Bar()
# bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
# bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# bar.set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
# # render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# # 也可以传入路径参数，如 bar.render("mycharts.html")
# bar.render()
#
# bar = (
#     Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
#     .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
#     .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
#     .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
#     # 或者直接使用字典参数
#     # .set_global_opts(title_opts={"text": "主标题", "subtext": "副标题"})
# )
# bar.render('test.html')
def draw_tree(data, url:str):
    tree = (
        Tree(init_opts=opts.InitOpts(width='1800px',height='1000px',page_title=url.split('.')[0]))
        .add(layout='orthogonal', orient='TB', series_name='search_tree', data=data,pos_top='10%',pos_left='left')
        .set_global_opts(title_opts=opts.TitleOpts(title=url.split('.')[0]))
    )
    tree.render(url)
