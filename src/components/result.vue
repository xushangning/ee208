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
	      	<movie-card :movie="result"
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
	import MovieCard from './movie.vue';
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
			var req = this.GetRequest();
			var data;
			if(req==="超凡蜘蛛侠")
				data = {
					id: 1,'name': '超凡蜘蛛侠', 'rate': '7.3', 'directors': ['马克·韦布'], 'casts': ['安德鲁·加菲尔德', '艾玛·斯通', '瑞斯·伊凡斯', '马丁·辛', '莎莉·菲尔德'], 'comments': {'Adam': '看点总结：加菲的笑，博士的药，警察的无能，蜘蛛侠的跳；艾玛的腿，特效的美，coldplay的音乐，“哥斯拉”的嘴。', '马逢春': '蜥蜴人最后拼死也要救批特！右手救不了换左手！Gwen的老爹死前嫩么含情脉脉的看着批特！天空飘着蓝晒的雪花！这！特！么！都！是！爱！啊！我肃然起敬', '一只阁子': '五星打给本色出演又萌又帅身材好屁股翘的加菲', '可乐': '绝不仅仅是新瓶装旧酒，小清新导演的小心思给蜘蛛侠增加了很多有爱的小细节，整体节奏流畅，尽管预告片里第一人称视角在电影中只是惊鸿一瞥，但3D出色，视效一流。石头姐隐约有Icon气场，最赞的还是加菲，演技出色，一双水汪汪的大眼睛可爱又迷人的苦逼着，身材修长穿着紧身衣还真是美好啊！！', '西西利亚冰百合': '打一星的人都是对男主cll的羡慕嫉妒恨！！！男主角长得帅演得萌，抹杀这个片子一切缺点！~ 全五分撒花~ '},'imgurl': '../../static/image/超凡蜘蛛侠.jpg'
				};
			if(req==="疯狂动物城")
				data = {
					id: 1,'name': '疯狂动物城', 'rate': '9.2', 'directors': ['拜伦·霍华德', '瑞奇·摩尔', '杰拉德·布什'], 'casts': ['金妮弗·古德温', '杰森·贝特曼', '伊德里斯·艾尔巴', '珍妮·斯蕾特', '内特·托伦斯'], 'comments': {'祥林嫂': '树懒太他妈好笑了！！那两分钟我嗓子都哑了！！卧槽！！真是太他妈好笑了！！', '悄悄': '看过了这一部，我好像能够更坚定地说我会当迪士尼一辈子的粉丝。迪士尼给我们营造的乌托邦就是这样，永远善良勇敢，永远出乎意料。', '多窜君': '无论是人设，世界观，动画制作，还是剧本，都挑不出毛病来啊啊啊！！细节多到爆！！好幸福！！！！>w< 最难能可贵的是配角们的人物性格和形象设置都非常饱满（教父梗好惊喜>< ） 虽然是动画，但是剧本还是隐射很多人类社会的种族问题，以及政治两党上位之争的问题。另外我狐Nick的眼神是在太苏了TwT...', '影评终结者': '完爆冰雪超能头脑，动物再次证明了动画片不止是给小朋友看的，而是全年龄段和世界级的，尖端数码特技、新意剧情、老梗新用搭配萌Q画风，乌托励志、搞笑温情、自然销魂、阴谋反转，用动物来映射人类，涉及种族歧视和两党斗争，无论从制作技术还是政治倾向或是社会意义来说，基本锁定今年奥斯卡最佳动画', '黄青蕉': '港真，面对人家动画片里连一把椅子扶手上的铝合金划痕都做得活灵活现的态度，咱们就默默低头学就好，不要一天到晚吹“国产视效大片”这个概念了，略尴尬'},'imgurl': '../../static/image/疯狂动物城.jpg'
				};
			if(req==="一出好戏")
				data = {
					id: 1,'name': '一出好戏', 'rate': '7.1', 'directors': ['黄渤'], 'casts': ['黄渤', '舒淇', '王宝强', '张艺兴', '于和伟'], 'comments': {'与碟私奔': '荒诞中揭示人性，导演处女作应该说太用心了，简直就是想费力而不只是想讨好(巧)观众；场景和特效都非常认真，荒岛，破船的造型……电影就是高度文明的人再退回到猴子原始时代的现代寓言，这也足见一个酝酿多年的演而优则导的处女作的良苦『野心』，如果多一些这样的的导演，那么我们的国产電影好看了', '掉线': '没想到黄渤居然拍了一出魔幻现实主义，故事相当好，但黄渤并没有被故事支配，十分自如的展现了自己的影像想法，作为处女作非常成熟。虽然片子也有些这样那样的遗憾，但该有的荒诞，该有的黑暗都成功地表达了出来，即便不带“演员跨界执导”的滤镜，这也是一年中排的上号的国产佳片。', '陆支羽': '1.与世孤绝的荒岛群像，物竞天择的社会缩影。2.没想到，黄渤真的拍了个“蝇王”式的反乌托邦寓言；无论票房口碑如何，这样的尝试已然足够攒脸。3.那场倒置船戏挺魔幻，有种集体着魔的快感，曾剑的摄影很加分。4.的确，这样一部电影，在华语影坛还不曾出现过同类。', '影志': '多人版《荒岛求生》，孤岛版《欢迎来到东莫村》…TB船车也太高级了，都想作死体验一把了，哈哈哈！故事其实挺通俗易懂、当荒岛生存冒险片看也不赖。可解读内容多，黄渤导演野心很大，也很努力想拍好，虽然想讲的东西略多，片子再短一点或许更好。看《瓣嘴》黄渤自造差评，看完正片后超出了预期。片尾两彩蛋，字幕最后的徐峥彩蛋加分。', '二十二岛主': '实名表扬张艺兴，在一众资深演员中竟然能够成为戏眼，这要感谢黄渤的剧本和信任，给了他一个有发挥的角色。说回电影本身，整个观影过程就像心电图一样起起伏伏，每当觉得挺好的地方，接下来很快就垮掉，可当不足的地方过去了，又会有新的亮点出现。毕竟是处女作，不能因为导演是黄渤就拿超级高的标准来要求他，第一部戏就敢挑战具有如此丰富元素的大群戏，这种勇气只怕姜文都不具备。姜文第5部才拍出了一步之遥，而黄渤第一部就拍出来了，结尾从悬崖上坠落的那场戏和马走日跳下来的那一幕太像，并留给了观众足够多的解读空间。所以已经可以预见到影片正式上映后可怕的两极分化，但我可以肯定的说，这是2018华语电影最具勇气的尝试之一。最后想说，下一部戏也别什么广告都植入，在末世寓言面前，开心消消乐和快手真的太low了。'},'imgurl': '../../static/image/一出好戏.jpg'
				};
			if(req==="网络谜踪")
				data = {
					id: 1,'name': '网络谜踪', 'rate': '8.5', 'directors': ['阿尼什·查甘蒂'], 'casts': ['约翰·赵', '米切尔·拉', '黛博拉·梅辛', '约瑟夫·李', '萨拉·米博·孙'], 'comments': {'凌睿': '男主应该感谢妻子的陪伴，感谢女儿的善良，还应该感谢谷歌、脸书、油管，要是他用的是百度，估计不但找不到女儿还会被莆田系广告骗走2万块。', 'Riku': 'Bieber concert (confirmed)', '马什么梅？': '看到结尾回想起一个细节，妈妈电脑里保存的班级电话簿，上面有真凶的联系方式来着，备注写着：家长在警局工作，离异家庭，喜欢玛格。', 'Cherry樱桃之远': '非常新颖的表现形式，整个故事都在电脑屏幕上完成，节奏感把握得极好，多处反转出人意料，想起前面的铺垫又觉得顺理成章，悬疑的氛围持续到结束。影片中各式social media玩得极溜，导演说想要通过影片表达网络有时候也不全是negative的。五个主创拍片十三天却在电脑前剪了两年！', '同志亦凡人中文站': '从头到尾都是电子屏幕这个设定太酷了！导演在形式主义上做到了完美。一个父亲在女儿失踪后抽丝剥茧的寻找真相，各种峰回路转都暗藏铺垫、合情合理，还有亲情的对比反思。是不是今年最好的悬疑片不好说，但绝对够原创、够新颖~~~感谢互联网救命之恩！！！'},'imgurl': '../../static/image/网络谜踪.jpg'
				};
			var n = data.name;
			return {
				index: '/result',
				items: [
					{id: 1,index: '/',name: '首页'},
					{id: 2,index: '/result',name: n}
				],
				bg: {
					backgroundImage: "url("+require("../assets/staticbg.png")+")",
					backgroundSize: '100% 100%',
					backgroundAttachment: 'fixed',
				},
				result: data,
				tp: {
					typ: 'info',
					imgurl: require("../assets/button.png")
				}
			}
		},
		methods: {
			GetRequest() {  
				var url = decodeURI(location.search);
				var req = url.split('?')[1];
				return req;
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
	    background-color: #202020;
	}
	::-webkit-scrollbar:horizontal {
	    height:10px;
	    margin-bottom:2px
	}
	::-webkit-scrollbar-track {  /* 外层轨道 */
	    background-color: #202020
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
	    line-height: 60px;
	    color: #333;
	    z-index:999;
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
	    margin-bottom: 10px;
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