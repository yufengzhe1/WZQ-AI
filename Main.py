import multiprocessing
from tkinter import messagebox
from tkinter import *
from Chess import *
from PP_chess import *
win_num = 0

if __name__ == '__main__':
	top = Tk()
	top.title("五子棋博弈程序")
	top.iconbitmap('me.ico')
	def play(mod, option):
		global win_num
		confirm = messagebox.askokcancel('确认窗口', '确认开始' + mod + '模式 ' + option +' 对战吗?')
		if confirm:
			if mod == '人人对战':
				p = multiprocessing.Process(target=pp_main, args=(mod, option))
				p.start()
			else:
				p = multiprocessing.Process(target=Run_chess, args=(mod, option))
				p.start()
		else:
			return
	Button(top, text="人人对战", fg="blue", width=28, command=lambda: play('人人对战', '')).pack()
	Button(top, text="比普通人厉害的   人机", fg="blue",  width=28, command=lambda: play('比普通人厉害的', 'HM')).pack()
	Button(top, text="比普通人厉害的  机器", fg="blue", width=28, command=lambda: play('比普通人厉害的', 'MM')).pack()
	Button(top, text="比普通人厉害的  辅助", fg="blue", width=28, command=lambda: play('比普通人厉害的', 'HMM')).pack()
	Button(top, text="和普通人人一样水平的  人机", fg="blue",  width=28, command=lambda: play('和普通人人一样水平的', 'HM')).pack()
	Button(top, text="和普通人人一样水平的  机器", fg="blue", width=28, command=lambda: play('和普通人人一样水平的', 'MM')).pack()
	Button(top, text="和普通人人一样水平的  辅助", fg="blue", width=28, command=lambda: play('和普通人人一样水平的', 'HMM')).pack()
	#Button(top, text="固若金汤  人机", fg="blue", width=28, command=lambda: play('固若金汤', 'HM')).pack()
	#Button(top, text="固若金汤  机器", fg="blue", width=28, command=lambda: play('固若金汤', 'MM')).pack()
	top.mainloop()
