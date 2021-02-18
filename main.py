from tkinter import *
from tkinter import font
import tkinter.messagebox
import winsound
import PIL
from PIL import Image,ImageTk
import random
import time
import copy
from sys import getsizeof


global k,frozen
frozen=False
#创建窗口
class Window():
    def __init__(self):
        self.root = Tk()
        self.scx = self.root.winfo_screenwidth()
        self.scy = self.root.winfo_screenheight()
        x=int((self.scx-1280)/2)
        y=int((self.scy-760)/2)
        self.root.geometry(f"1280x720+{x}+{y}")
        self.root.resizable(0, 0)
        self.root.title('我计算贼快 V1.0')
        self.root.iconbitmap('images/math game/ico.ico')
        self.cv = Canvas(self.root,  width = 1280,  height = 720, bg = 'white')
        self.cv.pack()


class Files():
    def __init__(self):
        self.background_img = Image.open('images/math game/bg3.jpg')
        self.start_img = PhotoImage(file='images/math game/开始界面.gif')
        self.start_b_img = PhotoImage(file='images/math game/开始游戏.gif')
        self.help_b_img = PhotoImage(file='images/math game/帮助.gif')
        self.record_b_img = PhotoImage(file='images/math game/纪录.gif')
        self.record_page_img = PhotoImage(file='images/math game/排行榜.png')
        self.help_page_img = PhotoImage(file='images/math game/help_page.png')
        self.restart_b_img = PhotoImage(file='images/math game/重新开始.gif')
        self.score_pad_img = Image.open('images/math game/记分牌.png')
        self.level_up_img = PhotoImage(file='images/math game/level_up.png')
        self.exit_b_img = Image.open('images/math game/退出.gif').resize((30, 30))
        self.exit_b0_img = PhotoImage(file='images/math game/退出.gif')
        self.skill_ui = PhotoImage(file='images/math game/skill_ui.png')

        self.shooter_img = [PhotoImage(file='images/math game/shooter/' + str(i) + '.png') for i in range(1, 9)]
        self.booms = [PhotoImage(file='images/math game/' + str(i) + '.gif') for i in range(1, 9)]
        self.big_booms = [PhotoImage(file='images/math game/big booms/' + str(i) + '.png') for i in range(1, 13)]
        self.cals = [PhotoImage(file='images/math game/calculator/' + str(i) + '.gif') for i in range(1, 9)]

        self.boom_ico = PhotoImage(file='images/math game/boom.gif')
        self.frozen_ico = PhotoImage(file='images/math game/frozen.gif')
        self.double_ico = PhotoImage(file='images/math game/double.gif')
        self.double_img = PhotoImage(file='images/math game/double_card.png')
        self.none_ico = PhotoImage(file='images/math game/none.gif')
        self.blood_ico = PhotoImage(file='images/math game/blood.gif')
        self.get_blood_img = PhotoImage(file='images/math game/get_blood.png')
        self.calculator_ico = PhotoImage(file='images/math game/calculator.gif')



class Start_UI():
    '开始界面'
    def __init__(self):
        self.photo1 = f.background_img.resize((1280, 720))
        self.photo = ImageTk.PhotoImage(self.photo1)
        self.bg = w.cv.create_image(640, 360, anchor='center', image=self.photo)
        self.start_game = w.cv.create_image(640, 360, image=f.start_img)
        self.start_b = w.cv.create_image(640, 380, image=f.start_b_img)
        self.help_b = w.cv.create_image(640, 450, image=f.help_b_img)
        self.record_b = w.cv.create_image(640, 520, image=f.record_b_img)
        self.nickname_text = w.cv.create_text(520, 310, font=('微软雅黑', 10), text="请输入昵称：")
        self.entry1 = Entry(w.root, justify='center')
        self.nickname_window = w.cv.create_window((640, 310), window=self.entry1)
        w.cv.tag_bind(self.start_b, "<Button-1>", self.start)
        w.cv.tag_bind(self.record_b, "<Button-1>", self.get_record)
        w.cv.tag_bind(self.help_b, "<Button-1>", self.get_help)
        if w.scx<=1280 or w.scy<=720:
            tkinter.messagebox.showinfo('提示', '如果您的显示器分辨率太低导致游戏窗口显示不完整，'
                                              '请前往“显示设置”将分辨率调高或者调整缩放比例。')


    def start(self,event):
        self.nickname=self.entry1.get()
        if self.nickname =='':
            self.nickname ='无名姓'
        q.create_UI()
        q.new_move()
        w.cv.delete(self.start_game,self.start_b,self.help_b,self.record_b,self.nickname_window,self.nickname_text)

    def get_help(self,event):
        w.cv.itemconfig(self.nickname_window, state='hidden')
        self.photo4 = ImageTk.PhotoImage(f.exit_b_img)
        help_page=w.cv.create_image(640, 400, image=f.help_page_img)
        self.exit_b2 = w.cv.create_image(640, 620, image=self.photo4)
        w.cv.tag_bind(self.exit_b2, "<Button-1>",
                      lambda event: (w.cv.delete(help_page,  self.exit_b2),
                                     w.cv.itemconfig(self.nickname_window, state='normal')))
    def get_record(self,event):
        w.cv.itemconfig(self.nickname_window,state='hidden')
        try:
            list1 = []
            list2 = []
            file = open('sounds/r.dll', 'r+')
            data = file.readlines()
            for x in data:
                list1.append(x.split('丨'))
            sort_it = sorted(list1, key=lambda x: int(x[1]), reverse=True)
            for i in sort_it:
                s = "丨".join(i)
                list2.append(s)
            if len(list2) > 20:
                list2 = list2[0:20]
            the_record = ''.join(list2)
            file.close()
        except:
            the_record='没有记录！'
        self.record_page = w.cv.create_image(640, 400, image=f.record_page_img)
        record_text= w.cv.create_text(630, 160, fill='black',anchor='n', font=('宋体', 10), text=the_record)
        self.photo3 = ImageTk.PhotoImage(f.exit_b_img)
        self.exit_b1 = w.cv.create_image(640, 620, image=self.photo3)
        w.cv.tag_bind(self.exit_b1, "<Button-1>",
                         lambda event:(w.cv.delete(self.record_page,record_text,self.exit_b1),
                                       w.cv.itemconfig(self.nickname_window,state='normal')))


class Animation():
    '动画类'
    def __init__(self,coord,num,images,time=80): # self，动画显示的位置，帧数，图片库,刷新时间。
        self.coord =coord
        self.num =num
        self.time=time
        self.t=0
        self.images = images
        self.first_img = w.cv.create_image(self.coord[0], self.coord[1],image=self.images[0])


    def move(self):
        self.t += 1
        animation = self.images[self.t]
        w.cv.itemconfig(self.first_img, image=animation)
        s = w.cv.after(self.time, self.move)  # 定时器
        if self.t == self.num-1:
            w.cv.after_cancel(s)
            w.cv.delete(self.first_img)


class Game():
    '游戏类'
    def __init__(self):
        self.the_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.question_list = {}
        self.skill_list = []
        self.q_text = None
        self.d = 0
        self.d9 = 4000
        self.how_many_q=0
        self.move_speed=1
        self.score = 0
        self.s_50 = True
        self.s_80 = True
        self.s_100 = True
        self.s_150 = True
        self.blood = 5
        self.double = False
        self.bang = False
        self.q_skill = 0
        self.w_skill = 0
        self.e_skill = 0
        self.r_skill = 0



    def create_UI(self):
        '生成游戏UI'
        self.score_pad_img = ImageTk.PhotoImage(f.score_pad_img)
        self.score_pad = w.cv.create_image(1150, 50, image=self.score_pad_img)
        self.score_text = w.cv.create_text(1150, 55, fill='black', font=('微软雅黑', 20,), text=f'分数:{self.score}')
        self.shooter = w.cv.create_image(640, 630, image=f.shooter_img[0])
        self.blood_text = w.cv.create_text(1150, 85, fill='black', font=('微软雅黑', 20,), text=f'生命:{self.blood}')

        w.cv.create_image(200, 660, image=f.skill_ui)
        self.q_num=w.cv.create_text(93, 640, fill='black', font=('Times', 10,'bold'), text=str(self.q_skill))
        self.w_num=w.cv.create_text(161, 640, fill='black', font=('Times', 10,'bold'), text=str(self.w_skill))
        self.e_num=w.cv.create_text(235, 640, fill='black', font=('Times', 10,'bold'), text=str(self.e_skill))
        self.r_num=w.cv.create_text(305, 640, fill='black', font=('Times',10,'bold'), text=str(self.r_skill))

        w.cv.create_text(500, 700, font=('微软雅黑', 20), text="请输入答案：")
        self.entry = Entry(w.root, justify='center')
        self.entry_win = w.cv.create_window((640, 700), window=self.entry)
        self.entry.bind("<Return>", self.destroy)
        self.entry.focus_set()



    def arithmetic(self):
        '随机生成算术题'
        opr = ['+', '-', '*','/']
        opr_math=['＋','－','×','÷']
        self.y = 10
        self.x = random.choice([100, 300, 500, 700, 900, 1100])


        # 10以内加减乘
        question_1 = f'{random.choice(range(1, 11))}{random.choice(opr[0:3])}{random.choice(range(1, 11))}' \
                     f'{random.choice(opr[0:3])}{random.choice(range(1, 11))}'

        #10以内除，用while循环保证整数
        while 1:
            question_2 = f'{random.choice(range(1, 11))}{random.choice(opr)}{random.choice(range(1, 11))}' \
                  f'{random.choice(opr)}{random.choice(range(1, 11))}'

            ans = eval(question_2)
            anslist=list(str(ans))
            if type(ans) == float and anslist[-1]=='0':
                break

        # 100以内两数加减
        question_3 = f'{random.choice(range(10, 101))}{random.choice(opr[0:2])}{random.choice(range(10, 101))}'
        # 100以内三数加减
        question_4 = f'{random.choice(range(10, 101))}{random.choice(opr[0:2])}{random.choice(range(10, 101))}' \
                     f'{random.choice(opr[0:2])}{random.choice(range(10, 101))}'
        # 1000以内两数加减
        question_5 = f'{random.choice(range(100,1001))}{random.choice(opr[0:2])}{random.choice(range(100,1001))}'
        # 1000以内三数加减
        question_6 = f'{random.choice(range(100, 1001))}{random.choice(opr[0:2])}{random.choice(range(100, 1001))}' \
                     f'{random.choice(opr[0:2])}{random.choice(range(100, 1001))}'
        #设置题目难度概率
        question_chose=[]
        for x in range(30):
            question_chose.append(question_1)
            question_chose.append(question_2)
        for x in range(20):
            question_chose.append(question_3)
        for x in range(10):
            question_chose.append(question_4)
        for x in range(10):
            question_chose.append(question_5)
        for x in range(5):
            question_chose.append(question_6)
        random.shuffle(question_chose)
        self.question = random.choice(question_chose)

        # 设置题目分值
        if self.question==question_1:
            self.value = 1
        elif self.question==question_2:
            self.value = 1
        elif self.question==question_3:
            self.value = 3
        elif self.question==question_4:
            self.value = 5
        elif self.question==question_5:
            self.value = 8
        elif self.question==question_6:
            self.value = 10
        #题目答案
        self.answer=str(int(eval(self.question)))
        #把题目替换成标准数学符号
        question_math01 = self.question.replace('+', '＋')
        question_math02 = question_math01.replace('-','－')
        question_math03 = question_math02.replace('*', '×')
        self.question_math = question_math03.replace('/', '÷')


        self.skill = random.choice(['frozen', 'frozen','double','double','double','blood','blood',
                                    'blood','boom','calculator', 'none','none', 'none', 'none', 'none', 'none',
                                    'none', 'none','none', 'none', 'none', 'none','none','none','none'])
        self.skill_ico = w.cv.create_image(self.x-5, self.y - 5, image=eval('f.' + self.skill + '_ico'))
        self.q_text = w.cv.create_text(self.x, self.y, fill='black',
                                       font=('Times', 15,), text=f'({self.value}分){self.question_math}=')
        # [题目对象] = [题目，技能图标，技能类型，答案，分数]
        self.question_list[self.q_text] = [self.question_math, self.skill_ico, self.skill, self.answer,self.value]

    def move_it(self, t, y, flag):
        """移动一个题目"""
        flag += 1
        speed = 20
        w.cv.move(t, 0, y)
        w.cv.update()
        global frozen
        if frozen == True:
            speed = 3000
        else:
            speed = 20
        self.s = w.cv.after(speed, self.move_it, t, y, flag)
        if flag >= (720 - self.y) / self.move_speed or self.blood==0:
            w.cv.after_cancel(self.s)
            w.cv.delete(t)
            if t in list(self.question_list.keys()) and self.blood>0:
                self.miss_blood()
                self.question_list.pop(t)


    def new_move(self):
        """创建新题"""
        self.how_many_q+=1
        self.arithmetic()
        self.move_it(self.q_text, self.move_speed, 0)
        self.move_it(self.question_list[self.q_text][1], self.move_speed, 0)
        self.m = w.cv.after(self.d9, self.new_move)


    def a_shoot(self, t, b):
        t += 1
        shoot = f.shooter_img[t]
        w.cv.itemconfig(self.shooter, image=shoot)
        s = w.cv.after(80, self.a_shoot, t, b)  # 定时器
        if t == 7:
            w.cv.after_cancel(s)

    def destroy(self, event):
        if self.entry.get() == 'q':
            if self.q_skill>0:
                sk.use_frozen()
                self.q_skill -= 1
                w.cv.itemconfig(self.q_num, text=str(self.q_skill))

        elif self.entry.get() == 'w':
            if self.w_skill > 0:
                sk.use_double()
                self.w_skill -= 1
                w.cv.itemconfig(self.w_num, text=str(self.w_skill))

        elif self.entry.get() == 'e':
            if self.e_skill > 0:
                sk.use_calculator()
                self.e_skill -= 1
                w.cv.itemconfig(self.e_num, text=str(self.e_skill))

        elif self.entry.get() == 'r':
            if self.r_skill > 0:
                sk.use_boom()
                self.r_skill -= 1
                w.cv.itemconfig(self.r_num, text=str(self.r_skill))


        else:
            copy0 = copy.deepcopy(self.question_list)
            for k in list(copy0.keys()):
                v = copy0[k]
                if self.entry.get() == v[3]:
                    exec(f'boom{k} = Animation(w.cv.coords({k}),8,f.booms)')  # 实例化一个动画类
                    exec(f'boom{k}.move()')  # 产生爆炸效果
                    exec(f'del boom{k}')
                    self.a_shoot(0, k)
                    if v[2] == 'frozen':
                        q_get = w.cv.create_text(93, 600, fill='tomato', font=('Times', 30),text='+1')
                        w.cv.after(2000,lambda :w.cv.delete(q_get))
                        self.q_skill+=1
                        w.cv.itemconfig(self.q_num,text=str(self.q_skill))
                    elif v[2] == 'blood':
                        sk.use_blood()
                    elif v[2] == 'calculator':
                        e_get = w.cv.create_text(235, 600, fill='tomato', font=('Times', 30), text='+1')
                        w.cv.after(2000, lambda: w.cv.delete(e_get))
                        self.e_skill+=1
                        w.cv.itemconfig(self.e_num, text=str(self.e_skill))
                    elif v[2] == 'boom':
                        r_get = w.cv.create_text(305, 600,fill='tomato', font=('Times', 30), text='+1')
                        w.cv.after(2000, lambda: w.cv.delete(r_get))
                        self.r_skill+=1
                        w.cv.itemconfig(self.r_num, text=str(self.r_skill))
                    elif v[2] == 'double':
                        w_get = w.cv.create_text(161, 600,fill='tomato', font=('Times', 30), text='+1')
                        w.cv.after(2000, lambda: w.cv.delete(w_get))
                        self.w_skill+=1
                        w.cv.itemconfig(self.w_num, text=str(self.w_skill))
                    if self.double == True:
                            v[4]*=2
                            x2=w.cv.create_text(w.cv.coords(k),font=('Times',50),fill='tomato',text='X2')
                            w.cv.after(2000,lambda :w.cv.delete(x2))
                            self.double = False
                            w.cv.delete(sk.double_card)
                    w.cv.delete(k)
                    w.cv.delete(v[1])
                    winsound.PlaySound("sounds\score.wav",
                                       winsound.SND_FILENAME | winsound.SND_ASYNC)
                    self.question_list.pop(k)
                    self.get_score(v[4])

            copy0.clear()
        self.entry.delete(0, "end")

    def get_score(self,the_score):
        self.score += the_score
        w.cv.itemconfig(self.score_text, text=f'分数:{self.score}')
        if self.score >= 50:
            if self.s_50==True:
                sk.clean_screen()
                level_up_label=w.cv.create_image(620, 320, image=f.level_up_img)
                while_50 = w.cv.create_text(690, 285, fill='black',font=('微软雅黑', 30), text='有点东西。')
                w.cv.after(2000,lambda :w.cv.delete(while_50,level_up_label))
                self.d9=3000
                self.s_50=False
        if self.score >= 100:
            if self.s_80 == True:
                sk.clean_screen()
                level_up_label = w.cv.create_image(620, 320, image=f.level_up_img)
                while_80 = w.cv.create_text(690, 285, fill='black',font=('微软雅黑', 30 ), text='是个人才。')
                w.cv.after(2000,lambda :w.cv.delete(while_80,level_up_label))
                self.move_speed=1.5
                self.s_80=False
        if self.score >= 150:
            if self.s_100 == True:
                sk.clean_screen()
                level_up_label = w.cv.create_image(620, 320, image=f.level_up_img)
                while_100 = w.cv.create_text(690, 285, fill='black',font=('方正剪纸简体', 30), text='你是神童！')
                w.cv.after(2000,lambda :w.cv.delete(while_100,level_up_label))
                self.move_speed=2
                self.d9=2000
                self.s_100 = False
        if self.score >= 200:
            if self.s_150 == True:
                sk.clean_screen()
                level_up_label = w.cv.create_image(620, 320, image=f.level_up_img)
                while_150 = w.cv.create_text(690, 285, fill='black',font=('微软雅黑', 30), text='最强大脑！')
                w.cv.after(2000,lambda :w.cv.delete(while_150,level_up_label))
                self.s_150 = False


    def miss_blood(self):
        self.blood -= 1
        w.cv.itemconfig(self.blood_text, text=f'生命:{int(self.blood)}')
        winsound.PlaySound("sounds\Fail1.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        if self.blood == 0:
            self.game_over()


    def game_over(self):
        winsound.PlaySound("sounds\game over.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        w.cv.after_cancel(self.m)
        self.restart_b = w.cv.create_image(580, 440, image= f.restart_b_img)
        self.exit_b = w.cv.create_image(700, 440, image=f.exit_b0_img)
        w.cv.tag_bind(self.exit_b, "<Button-1>",lambda event:w.root.quit())
        w.cv.tag_bind(self.restart_b, "<Button-1>", self.restart)
        self.gameover_text=w.cv.create_text(640, 250, fill='black',
                                    font=('微软雅黑', 60,), text='GAME OVER')
        file=open('sounds/r.dll','a')
        file.write(f'{st.nickname}丨{self.score}丨{self.the_time}\n')
        file.close()



    def restart(self,event):
        w.cv.delete(self.gameover_text, self.restart_b,self.exit_b,self.entry_win)
        st.__init__()
        self.blood=5
        self.score = 0
        self.d9=4000



class Skill():
    def __init__(self):
        pass
    def set_frozen(self):
        global frozen
        frozen=False
        q.m = w.cv.after(q.d9, q.new_move)
    def use_frozen(self):
        winsound.PlaySound('sounds\Frozen.wav',winsound.SND_FILENAME | winsound.SND_ASYNC)
        global frozen
        frozen=True
        w.cv.after_cancel(q.m)
        w.cv.after(3000, self.set_frozen)
    def use_double(self):
        winsound.PlaySound('sounds\card.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
        q.double=True
        self.double_card=w.cv.create_image(800, 620,image=f.double_img)
    def use_blood(self):
        get_blood = w.cv.create_image(800, 620, image=f.get_blood_img )
        w.cv.after(2000, lambda :w.cv.delete(get_blood))
        q.blood += 1
        w.cv.itemconfig(q.blood_text, text=f'生命:{int(q.blood)}')
    def clean_screen(self):
        for x in list(q.question_list.keys()):
            w.cv.delete(x)
            w.cv.delete(q.question_list[x][1])
        q.question_list.clear()
    def use_boom(self):
        winsound.PlaySound('sounds\Boom.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
        boom_effect = Animation([640, 360], 12, f.big_booms, time=100)
        boom_effect.move()
        self.clean_screen()
    def use_calculator(self):
        copy = list(q.question_list.keys())[:]
        cal_effect=Animation([800, 620], 8, f.cals, time=200)
        cal_effect.move()
        for k1 in copy:
            v1 = q.question_list[k1]
            w.cv.itemconfig(k1, anchor='center', font=('Times', 15,),text=f'({q.value}分){q.question_math}={v1[3]}')



if __name__ == '__main__':
    w = Window()
    f=Files()
    st=Start_UI()
    q = Game()
    sk=Skill()
    w.cv.mainloop()

