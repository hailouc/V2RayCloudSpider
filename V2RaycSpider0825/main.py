from Panel.main_panel import *

"""欢迎使用V2Ray云彩姬"""
if __name__ == '__main__':
    hp = HomePanel()
    try:
        hp.start(init=True)
    except Exception as e:
        hp.kill(e)
