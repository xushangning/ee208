<template>
	<div id="whole" :style="bg">
	    <el-container>
	      <el-header height='61px'>
	        <el-row>
	          <el-col :span="21" id="vmenu-header">
	          	<vmenu :activeIndex='index' :items='items'></vmenu>
	          </el-col>
	          <el-col :span="6" id="search">
	          	<vform :tp='tp'></vform>
	          </el-col>
	          <el-col :span='1' id='info1'><info1></info1></el-col>
	          <el-col :span="1" id="time1"><time1></time1></el-col>
	        </el-row>
	      </el-header>
	      <el-main>
	      	<movie-card v-for="result in results"
	      				:movie="result"
	      				:key="result.id"></movie-card>
	      </el-main>
	    </el-container>
	  </div>
</template>

<script>
	import VMenu from './vmenu.vue';
	import Time1 from './time1.vue';
	import VForm from './form.vue'; 
	import Carousel from './carousel.vue';
	import Info1 from './info1.vue';
	import MovieCard from './moviecard';
	export default {
		components:{
			'vmenu': VMenu,
			'time1': Time1,
			'vform': VForm,
			'carousel': Carousel,
			'info1': Info1,
			'movie-card': MovieCard,
		},
		data() {
			return {
				index: '/results',
				items: [
					{id: 1,index: '/',name: '首页'},
					{id: 2,index: '/hello',name: '电影大全'},
					{id: 3,index: '/results',name: '搜索结果'}
				],
				bg: {
					width: '100%',
					backgroundImage: "url("+require("../assets/staticbg.png")+")",
					backgroundSize: '100% 100%',
					backgroundAttachment: 'fixed',
				},
				results: [
					{id: 1,'name': '超凡蜘蛛侠', 'rate': '7.3', 'directors': ['马克·韦布'], 'casts': ['安德鲁·加菲尔德', '艾玛·斯通', '瑞斯·伊凡斯', '马丁·辛', '莎莉·菲尔德'], 'comments': {'Adam': '看点总结：加菲的笑，博士的药，警察的无能，蜘蛛侠的跳；艾玛的腿，特效的美，coldplay的音乐，“哥斯拉”的嘴。', '马逢春': '蜥蜴人最后拼死也要救批特！右手救不了换左手！Gwen的老爹死前嫩么含情脉脉的看着批特！天空飘着蓝晒的雪花！这！特！么！都！是！爱！啊！我肃然起敬', '一只阁子': '五星打给本色出演又萌又帅身材好屁股翘的加菲', '可乐': '绝不仅仅是新瓶装旧酒，小清新导演的小心思给蜘蛛侠增加了很多有爱的小细节，整体节奏流畅，尽管预告片里第一人称视角在电影中只是惊鸿一瞥，但3D出色，视效一流。石头姐隐约有Icon气场，最赞的还是加菲，演技出色，一双水汪汪的大眼睛可爱又迷人的苦逼着，身材修长穿着紧身衣还真是美好啊！！', '西西利亚冰百合': '打一星的人都是对男主cll的羡慕嫉妒恨！！！男主角长得帅演得萌，抹杀这个片子一切缺点！~ 全五分撒花~ '},'imgurl': '../../static/image/超凡蜘蛛侠.jpg'},
					{id: 2,'name': '超凡蜘蛛侠2', 'rate': '7.3', 'directors': ['马克·韦布'], 'casts': ['安德鲁·加菲尔德', '艾玛·斯通', '杰米·福克斯', '戴恩·德哈恩', '坎贝尔·斯科特'], 'comments': {'小津安': '可怜的小蜘蛛侠 自从被漫威亲妈卖了之后就开始苦逼的童养媳生活 一部里面打三个反派还死了女票 哭瞎了 看看人家复联都是六个打一个 QAQ', 'A L E X': '这是一个迷失方向的充电宝的故事。Dane Dehaan又扮演了一个蛊惑人心的诱受角色，几句I NEED YOU就把充电宝苏的晕头转向难以抗拒。', '扭腰客': '超多的主观镜头简直就像过山车，爽得一比，就这点而言，3D是真的用对地方了。石头姐美Cry，加菲猫蠢哭，小绿魔简直就是小李年轻20年，至于电光人——他的故事传奇而悲伤，一句话总结就是：一朝被电到，十年充电宝。', 'Obtson': '适宜观赏人群：1、加菲粉，2、石头黑，3、德哈恩症患者，4、光电类专业成绩排在系内前15%的同学。', 'Mona Lishark': '我得说，小男孩蜘蛛侠穿过栏杆跑到犀牛人面前的场景非常非常感动。'},'imgurl': '../../static/image/超凡蜘蛛侠2.jpg'},
					{id: 3,'name': '蜘蛛侠：英雄归来', 'rate': '7.4', 'directors': ['乔·沃茨'], 'casts': ['汤姆·赫兰德', '小罗伯特·唐尼', '玛丽莎·托梅', '迈克尔·基顿', '雅各布·巴特朗'], 'comments': {'shiki': '第二个彩蛋简直了。不剧透了自己体会', 'young': 'Tony对Peter说：如果你没有装备（蜘蛛服）就一无是处，那你就更不应该拥有它。Peter：爸爸你个亿万富翁好意思说这种话？', '圣诞艺仔🎄': '最可爱的小蜘蛛，最贱的彩蛋，全程都在笑。这种程度的反派可能钢铁侠1分钟就拍死了，小蜘蛛却打了两个小时，可以说是超级英雄的阶级差异了。', '大聪看电影': '“蜘蛛咬你的时候会痛吗？”  “你会产卵吗？”  “你能召唤一大群蜘蛛吗？” “你能射多远？”', '同志亦凡人中文站': '和“死侍”一样属于人物塑造比剧情更成功的偏锋电影。通过注入校园元素不但成功重启热门超级英雄，而且让观众见证了人物的长（yǎng）成。热血、话痨、中二、一心想向Tony爸爸证明自己的小蜘蛛太可爱鸟，请给我来一打！'},'imgurl': '../../static/image/蜘蛛侠：英雄归来.jpg'},
					{id: 4,'name': '蜘蛛侠', 'rate': '7.6', 'directors': ['山姆·雷米'], 'casts': ['托比·马奎尔', '威廉·达福', '克斯汀·邓斯特', '詹姆斯·弗兰科', '克里夫·罗伯逊'], 'comments': {'战国客': '不同以往的英雄设计，“平民英雄”看来更能打动人心，其中蜘蛛侠倒挂亲吻女主角的镜头相信是很多女性观众的梦想~~', '宋宋': '很喜欢这个不帅，带点腼腆，很勇敢很痴情的蜘蛛侠：）', '沉歌': '喜欢James Franco演Harry。', '梦梦梦梦': '我需要被猴子咬一口，然后变成孙悟空！！', '熊出没': '第一级还是很好看的！屌丝梦'},'imgurl': '../../static/image/蜘蛛侠.jpg'},
					{id: 5,'name': '蜘蛛侠2', 'rate': '7.3', 'directors': ['山姆·雷米'], 'casts': ['托比·马奎尔', '克斯汀·邓斯特', '詹姆斯·弗兰科', '阿尔弗雷德·莫里纳', '罗斯玛丽·哈里斯'], 'comments': {'甲🌈': '说实话，我觉得蜘蛛侠2是系列中最好的一部：故事的设定，人物的冲突，自我的矛盾，真挺不错的。我也是从这部开始变成了蜘蛛侠控。', 'Bill': '少数几部觉得比原作优秀的续集之一 英雄电影中的优秀典范', 'Lan~die': '最好的漫画电影之一，那种挣扎表现的很真实。很多三部曲都是第二部最好，比如这部。', '托尼·王大拿': '萨姆·雷米是玩B级片出身的，即便在《蜘蛛侠I》里也毫不隐藏自己的口味；但到了第二部，他真正的开始掌握商业大制作的要领了，多年后重看突然发现这部片子竟然可以看做是未来超级英雄电影的启示录：无论在节奏，故事，还是动作场面上，其影响存在至今；英雄的迷失和救赎永远是此类影片成功的不二法门。', '阅世书生': '你有与众不同的能力。那不是一种特权，而是一种天赋。\n能力愈强，责任愈大。'},'imgurl': '../../static/image/蜘蛛侠2.jpg'},
					{id: 6,'name': '蜘蛛侠3', 'rate': '7.2', 'directors': ['山姆·雷米'], 'casts': ['托比·马奎尔', '克斯汀·邓斯特', '詹姆斯·弗兰科', '托马斯·哈登·丘奇', '托弗·戈瑞斯'], 'comments': {'飞鸟凉': '剧本糟烂，腹黑的蜘蛛侠终于把他的情敌和职场竞争对手统统干掉了。应该让mary jane挂掉，这样就能让peter和harry演绎蜘蛛侠4：神奇侠侣', '文泽尔': '最落魄的超级英雄是谁？蜘蛛侠.穷宅男一枚，女友还许了别人.杯具中的杯具', '果酱☮': '最雷最囧最槑最脑残的主旋律。蜘蛛虾毁了哈蜊的俊美脸蛋，哈蜊反而冰释前嫌帮蜘蛛虾打怪还英勇牺牲了，临死还不忘强调蜘蛛虾是他的朋友。而哈蜊的死最后却被蜘蛛虾用来向人们显摆一道理：成为什么样的人在于你选择做什么样的人。“哈蜊选择当善良的人”，愿哈蜊在天有灵听到此话吐血重生再战伪人蜘蛛虾', '眠去': '他看着橱窗里可以分期付款的璀璨钻戒，露出甜蜜的微笑。', '顺其自燃': '朋友终归是朋友，英雄却不会一直是英雄'},'imgurl': '../../static/image/蜘蛛侠3.jpg'}


				],
				tp: {
					typ: 'info',
					imgurl: require("../assets/button.png")
				}
			}
		}
	}
</script>

<style> 
	::-webkit-scrollbar {  /* 滚动条整体部分 */
	    width:10px;
	    margin-right:2px
	}
	::-webkit-scrollbar-button { /* 滚动条两端的按钮 */
	    width:10px;
	    background-color: #000000;
	}
	::-webkit-scrollbar:horizontal {
	    height:10px;
	    margin-bottom:2px
	}
	::-webkit-scrollbar-track {  /* 外层轨道 */
	    background-color: #000
	}
	::-webkit-scrollbar-track-piece {  /*内层轨道，滚动条中间部分 */
	    background-color: #202020;
	    border-radius: 5px;
	}
	::-webkit-scrollbar-thumb {  /* 滑块 */
	    width:10px;
	    border-radius: 5px;
	    background: #606266;
	}
	::-webkit-scrollbar-corner { /* 边角 */
	    width: 10px;
	}
	::-webkit-scrollbar-thumb:hover { /* 鼠标移入滑块 */
	    background: #707070;
	}
	.demo {
	    width: 400px;
	    height: 200px;
	    overflow: auto;
	}
	html,body {
    margin: 0;
    height:100%;
	}
	a{text-decoration : none}
	#app {
		height:100%;
	}
	.whole {
	    width:100%;
	    height: 100%;
	}
	.el-header, .el-footer {
	    background-color: rgba(0,0,0,0);
	    color: #333;
	}
	  
	body > .el-container {
	    margin-bottom: 40px;
	}
	.el-container.is-vertical {
	    width: 90%;
	    margin-left: auto;
	    margin-right: auto;
	}
	.el-container:nth-child(5) .el-aside,
	.el-container:nth-child(6) .el-aside {
	    line-height: 260px;
	}
	  
	.el-container:nth-child(7) .el-aside {
	    line-height: 320px;
	}

	/*layout*/
	.el-row {
	    margin-bottom: 20px;
	    &:last-child {
	      margin-bottom: 0;
	    }
	}
	.grid-content {
		min-height: 40px;
	}
	#vmenu-header {
		position:fixed;
		top: 0px;
	}
	#time1 {
		position:fixed;
		top: 0px;
		left: 90%;
	}
	#info1 {
		position: fixed;
		top: 0px;
		left: 86.5%;
	}
	#search {
		position:fixed;
		top:10px;
		left: 57%;
	}
</style>