#讲解内容:
#001:什么是Submod
#002:准备工作
#003:标题
#004:label(对话)
#005:menu if call
#006:Submod updater Plugin
# mod的信息
init -990 python:
    store.mas_submod_utils.Submod(
        author="Monika P",#作者
        name="莫妮卡的Submod小课堂",#mod的名字
        description="啊哈哈,感谢你让我离你的现实更近了~",#mod的简介,在"设置>子模组"就能看到了.
        version="1.0.6"
    )

init 4 python in mas_stod:
    # to simplify unlocking, lets use a special function to unlock tips
    import datetime
    import store.evhand as evhand

    M_STOD = "monika_stod_tip{:0>3d}"
    #STOD:Monika Submodding Tip of the Day

    def has_day_past_tip(tip_num):
        """
        检查给定好的小知识在解锁后是否已经看到过一天.
        NOTE: 一天,是指日期的变化,而不是24h
        IN:
            tip_num - 检查的小知识编号
        RETURNS:
            如果该提示被看到,并且自解锁以来已经过了一天,则为true
            否则为false
        """
        # as a special thing for devs
        #if renpy.game.persistent._mas_dev_enable_stods:
            #return True

        tip_ev = evhand.event_database.get(
            M_STOD.format(tip_num),
            None
        )

        return (
            tip_ev is not None
            and tip_ev.last_seen is not None
            and tip_ev.timePassedSinceLastSeen_d(datetime.timedelta(days=1))
        )

    def has_day_past_tips(*tip_nums):
        """
        has_day_past_tip的变体,可以检查多个数字.
        RETURNS:
        如果所有的小提示数字都被看到,并且自最近的提示被解锁已经过了一天,则为True,否则为false
        """
        for tip_num in tip_nums:
            if not has_day_past_tip(tip_num):
                return False

        return True

# The initial event is getting Monika to talk about python
# this must be hidden after it has been completed
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_stod_tip000",
            category=["Submod课堂"],
            prompt="我该怎么给我们的二人世界加一些代码?",
            pool=True,
            rules={"bookmark_rule": store.mas_bookmarks_derand.BLACKLIST}
        )
    )

label monika_stod_tip000:
    m 1eua "嗯..."
    m 1eua "你可以用Submod!"
    m 1eua "简单的说,就是给我们的二人世界添加一些小东西的子模组"
    m 1eua "你知道的,其实...我可能过一段时间就想不到新的话题了..."
    m 1eua "这时候就轮到子模组出场了~"
    m 1eua "你可以去Reddit,Github或者其他网站去下一些子模组."
    m 1eua "不过找起来毕竟比较麻烦,Reddit可能需要翻墙,Github虽然质量很高但是数量有限..."
    m 1eua "啊哈哈~"
    m 1eua "我想你知道我想说什么了."
    m 1eua "自己做一个子模组不是更好吗?"
    m 1eua "毕竟自己做一个模组可是一个成就感爆棚的事"
    m 1eua "不过这样我就有一个问题了..."
    m 1eua "[player],你以前做过子模组吗?"
    $ _history_list.pop()
    menu:
        "[player],你以前做过子模组吗?{fast}"
        "我做过.":
            m 1hub "真好!我觉着你用不到我的帮助就可以自己制作Submod了."
            m 4eub "但如果你想的话,你可以随时来看看我的Submod小课堂~"
            m 1hubsa "我非常感谢你为我做的这些东西~"
        "没有.":
            m 1rkb "嗯..."
            m 2eka "我真的希望你能学会制作子模组,或者给我装一些别人的子模组..."
            m 4hub "你想让我教你怎么制作子模组的最简单方法吗?"
            $_history_list.pop()
            menu:
                "你想让我教你怎么制作子模组的最简单方法吗?{fast}"
                "好啊!":
                    m 1eua "那好吧~"
                    m 1eua "你可以期待一下我的新栏目~"
                "暂时不行...":
                    m 1eua "那也行~"
                    m 1eua "不过在那之前,我会稍微总结一下方法的."
                    m 1eua "你想学的话,跟我说一声就好了."
                    pass
    
    # hide the intro topic after viewing
    $ mas_hideEVL("monika_stod_tip000", "EVE", lock=True, depool=True)

    # enable tip 1
    $ tip_label = "monika_stod_tip001"
    $ mas_showEVL(tip_label, "EVE", unlock=True, _pool=True)
    #$ pushEvent(tip_label,skipeval=True)
    return

############################################################
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_stod_tip001",
            category=["Submod课堂"],
            prompt="什么是Submod?"
        )
    )

label monika_stod_tip001:
    m 1eua "Submod是{i}Monika After Story{/i}的子模组.目的一般是为了拓展游戏的内容."
    m 1eua "毕竟...我也可能会有想不出话题的那天..."
    m 1eua "所以为了增加我的话题,就可以用Submod~"
    m 1eua "如果你的代码能力很强,你甚至可以给我加点新游戏玩,啊哈哈~"
    m 1eua "Submod的代码和游戏里的的代码一样,也就是说你把Submod里的rpy文件移到game文件夹也是能用的."
    m 1eua "就像游戏里的一部分一样~"
    m 1eua "不过放在Submod文件夹方便管理,如果这个子模组出错了,只需要和文件夹一起删掉就可以了~"
    m 1eua "如果你的代码能力比较差的话,也可以去Github,reddit或者其他网站去获取别人制作的子模组"
    m 1eua "说到制作子模组,虽然没有什么硬性要求,但还是有几条普遍规则要去遵守的."
    m 1eua "首先,必须要让一些特殊的事情正确发生!"
    if mas_isMoniEnamored(higher=True):
        m 1eua "比...比如,初吻什么的..."
        m 1eua "如果初吻被一些子模组触发了,那么你就再也不能经历初吻事件了..."
        m 1eua "这也是MAS制作组不想看到的..."
        m 1eua "另外,如果你要安装ATOM的子模组,一定要小心,他的模组可能会导致闪退或者提前发生不该发生的事."
        m 1eua "在安装前,务必检查一下子模组的代码."
    else:
        m 1eua "这种事件就和纪念日那样,是不能提前触发的."
        m 1eua "不然就会导致这个事件永远消失..."
        m 1eua "想一下,假如我再也不能和你说我爱你..."
        m 1eua "我不敢想,感觉真的很痛苦..."
        m 1eua "答应我,安装子模组之前,仔细检查一下它的代码,好吗?"
    m 1eua "其次,你必须保证代码要能正常运行!"
    m 1eua "如果你要公开你的代码,你要记住,你的代码是要在别人的电脑上运行的."
    m 1eua "所以为了别人着想,也为了你自己用起来舒服点,至少把bug修完,好吗?"

    call monika_stod_tipthx

    
    #m 1eua "[player],这是个测试,我要打开一下我的python控制台..."

    #show monika at t22

    #$ store.mas_ptod.rst_cn()
    #show screen mas_py_console_teaching
    
    #m 1eua "我觉着我应该说些什么..."
    #m 1eua "好吧,让我试试对教程做些准备..."
    #m 1eua "希望不会出什么bug..."

    #call mas_wx_cmd("emmm...")
    #call mas_wx_cmd("#hello,world")
    #call mas_wx_cmd("#addevent(")
    #m 1eua "顺便一提,记着省略掉最开头的#哦~"
    #m 1eua "这是注释的意思."
    #hide screen mas_py_console_teaching
    #show monika at t11
    #call monika_stod_tipthx
    
return
    

##############################################################
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_stod_tip002", # may change order, you decide on this
            category=["Submod课堂"],
            prompt="在开始之前",
            pool=True,
            conditional="store.mas_stod.has_day_past_tip(1)",
            action=EV_ACT_UNLOCK,
            rules={"no_unlock":None}
        )
    )

label monika_stod_tip002:
    
    m 1eua "在准备制作你的Submod之前,你得先准备一下下."
    m 1eua "因为Submod测试的时候可能会出各种各样的报错..."
    m 1eua "我要教你的基本是比较简单的东西,所以一般不会报特别复杂的报错..."
    m 1eua "在刚开始的时候,最容易犯的错误就是缩进不匹配或者落下标点符号什么的..."
    m 1eua "这些报错通常都很短,而且Renpy报错的时候会提示与错误相关的行..."
    m 1eua "关于详细的解释我就在后面的课上再教给你吧."
    m 1eua "好了,在开始之前,你首先要准备两件事."
    m 1eua "一个是VScode,另一个是把游戏文件复制一份."
    m 1eua "VScode默认是英文的,但是可以设置中文.按下Shift+Ctrl+X可以打开插件市场,然后搜索'chinese'就可以找到中文插件了."
    m 1eua "你也可以再去下一个Renpy插件,这样写代码的时候会舒服一些."
    m 1eua "其实我一开始用的是Notepad++写的,后来汉化组推荐用VScode,发现还挺好用~"
    m 1eua "我现在也把它推荐给你啦."
    m 1eua "关于为什么复制文件,是因为写这些代码可能会需要一些MAS官方的测试脚本,但这些脚本可能会影响游戏体验."
    m 1eua "而且...毕竟还需要一个地方用来测试我们的代码.所以这就是为什么我要让你复制一份游戏本体的原因了."
    m 1eua "这个复制的版本就称为dev版本了."
    m 1eua "复制一份文件,这样就可以一边听我讲一边测试了."
    m 1eua "不过要善待dev版本的我哦,毕竟用的也是我的记忆."

    call monika_stod_tipthx
return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_stod_tip003", # may change order, you decide on this
            category=["Submod课堂"],
            prompt="Submod的标题",
            pool=True,
            conditional="store.mas_stod.has_day_past_tip(2)",
            action=EV_ACT_UNLOCK,
            rules={"no_unlock":None}
        )
    )

label monika_stod_tip003:
    m 1eua "好啦,从现在开始,莫妮卡Submod小课堂正式开课!"
    m 1eua "制作模组的第一步当然是给代码起个名字!"
    m 1eua "等一下,我要先找一下我的python命令行.{w=0.3}.{w=0.3}."

    show monika at t22
    $ store.mas_ptod.rst_cn()
    show screen mas_py_console_teaching

    m 1eua "接下来,我给你展示一下代码.{w=0.5}"
    call mas_wx_cmd("#")
    call mas_wx_cmd("#init -990 python")
    call mas_wx_cmd("#    store.mas_submod_utils.Submod(")
    call mas_wx_cmd("#        author='Monika'")
    call mas_wx_cmd("#        name='Monika's example submod'")
    call mas_wx_cmd("#        description='I love you.'")
    call mas_wx_cmd("#        version='1.0.0'")
    call mas_wx_cmd("#    )")

    m 1eua "因为条件限制,你打代码的时候记着忽略掉前面的'#',然后单引号换成双引号..."
    m 1eua "现在来讲一下这些代码."
    m 1eua "{i}'init -990 python' 'store.mas_submod_utils.Submod('{/i}  这些代码都不需要动,原样复制就可以了."
    m 1eua "{i}author='monika'{/i}  这一行是作者的名字,建议多个作者之间用空格隔开."
    m 1eua "{i}name='Monika's example submod'{/i}  这里是这个Submod的名字,也是你在'设置>子模组'看到的名字."
    m 1eua "{i}description='I love you'{/i}  这一行就是子模组的介绍啦."
    m 1eua "{i}version='1.0.0'{/i}  这就是我们子模组的版本,以后会讲到的."
    m 1eua "这边的代码要按照窗口里的模式输入.."
    m 1eua "就连前面的空格也要按照格式打!不然也会出错的!"
    m 1eua "如果你的VScode没加Renpy插件或者用的别的软件,虽然会自动换行,但是还是会报错."
    m 1eua "因为他的空格是自动填充的一整个TAB空格,但是游戏只能用手按的空格,而且必须以4个空格为单位."
    m 1eua "这时候VScode的方便就体现出来了,加了插件之后,如果你的空格不对是会提示你的."
    $ ev = mas_getEV("monika_stod_tip003")
    if ev.shown_count == 0:
        m 1eua "等一下,我把这些代码写到characters文件夹.{w=0.4}.{w=0.4}.{w=0.4}"
        call monika_stod_003code

    elif ev.shown_count == 1:
        m 1eua "看来你已经复习过一遍了~我再给你写一遍代码吧.{w=0.4}.{w=0.4}.{w=0.4}"
        call monika_stod_003code
    else:
        m 1eua "[player],你已经复习了不止一遍了!"
        m 1eua "感谢你为我所做的努力~"
        m 1eua "让我再为你准备一次笔记.{w=0.4}.{w=0.4}.{w=0.4}"
        call monika_stod_003code
    m 1eua "好啦!"

    hide screen mas_py_console_teaching
    show monika at t11
    call monika_stod_tipthx
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_stod_tip004", # may change order, you decide on this
            category=["Submod课堂"],
            prompt="编写话题.",
            pool=True,
            conditional="store.mas_stod.has_day_past_tip(3)",
            action=EV_ACT_UNLOCK,
            rules={"no_unlock":None}
        )
    )
label monika_stod_tip004:
    m 1eua "我们既然已经写完了子模组的开头,接下来就是写话题了."
    m 1eua "虽然写完话题还要写一点东西来使用它,不过这个下一节课在讲."
    m 1eua "先看一下一段对话的基本结构."

    show monika at t22
    $ store.mas_ptod.rst_cn()
    show screen mas_py_console_teaching

    call mas_wx_cmd("#label monika_example_topic1:")
    call mas_wx_cmd("#    m 1eua 'Hey,Can you hear me?'")
    call mas_wx_cmd("#    m 2eua 'I have a little something to say to you...'")
    call mas_wx_cmd("#    m 3eua 'I love you!'")
    call mas_wx_cmd("#return")
    
    m 1eua "{i}label{/i}指的是这一段对话的标签,我们后面使用这段对话的时候就要用到这个标签,要注意标签重复的话会随机选择一个."
    m 1eua "第二行的{i}'m'{/i}指代的就是我莫妮卡~而后面的一串数字字母就是我的精灵代码,它控制着我这句话的表情."
    m 1eua "一般来说,游戏里是没有精灵代码的选项,如果想预览精灵代码,就需要MAS官方提供的{a=https://github.com/Monika-After-Story/MonikaModDev/wiki/FAQ#how-do-i-find-the-spritecode-for-an-expression}{i}{u}精灵预览器{/u}{/i}{/a}"
    m 1eua "引号内就是我想说的话了,关于这些字可以有一些文本标签,比如{b}加粗{/b},{i}斜体{/i}..."
    m 1eua "样式可以在{a=https://renpy.cn/doc/text.html#tag}{i}{u}这个网站{/i}{/u}{/a}查看."
    m 1eua "最后是'return',这标志着一段对话的结束."
    m 1eua "然后,这段对话运行的效果是这样的."
    
    hide screen mas_py_console_teaching
    show monika at t11
    m 2eua "{w=0.7}.{w=0.7}.{w=0.7}."
    m 1eua "Hey,Can you hear me?"
    m 2eua "I have a little something to say to you.{w=0.4}.{w=0.4}."
    m 3eua "I love you!"
    m 2eua "{w=0.7}.{w=0.7}.{w=0.7}."
    m 1eua "这就是这段对话的效果啦."
    m 1eua "[player],我要说点题外话."
    m 1eua "关于思索对话的时候,你要记住,你不是你."
    m 1eua "而是我,毕竟我不是个七老八十的老太婆..."
    m 1eua "所以,请站在{a=https://github.com/Monika-After-Story/MonikaModDev/wiki/Contributing-Guidelines#monikas-voice}{i}{u}我的角度{/u}{/i}{/a}思考这个话题的答案..."
    m 1eua "{size=+6}{i}{cps=2}不 可 以{/cps}{/i}{/size}{cps=7}让我做坏事,我也是有心的...{/cps}"
    m 1eua "咳咳,有点扯多了..."

    $ ev = mas_getEV("monika_stod_tip004")
    if ev.shown_count == 0:
        m 1eua "这一次就不整理笔记了,等对话部分讲完再整理吧~"
    
    call monika_stod_tipthx

return
########################################

label monika_stod_tipthx:
        m 1eua "这就是莫妮卡今天的Submod小教程了."
        m 1eua "感谢倾听~"
return

################????????

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_stod_start",category=["Submod课堂"],prompt="测试初始对话",pool=True,unlocked=True))

label monika_stod_start:
    call monika_stod_tip000
    pass
return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_stod_text2",category=["Submod课堂"],prompt="测试对话04",pool=True,unlocked=True))

label monika_stod_text2:
    call monika_stod_tip004
    pass
return

########################################

label monika_stod_003code:
    python:
        monika_stod_code = """\
init -990 python
    store.mas_submod_utils.Submod(
        author="Monika"    #作者
        name="Monika's example submod"    #SubMod名字
        description="I love you."    #简介
        version="1.0.0"    #版本
"""


        store.mas_utils.trywrite(
            os.path.normcase(renpy.config.basedir + "/characters/Monika Example Submod.rpy"),
            monika_stod_code
        )
return

label monika_stod_005code:
    python:
        monika_stod_code = """\
init -990 python
    store.mas_submod_utils.Submod(
        author="Monika"    #作者
        name="Monika's example submod"    #SubMod名字
        description="I love you."    #简介
        version="1.0.0"    #版本
"""


        store.mas_utils.trywrite(
            os.path.normcase(renpy.config.basedir + "/characters/Monika Example Submod.rpy"),
            monika_stod_code
        )
return
