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
			return {
				index: '/result',
				items: [
					{id: 1,index: '/',name: '首页'},
					{id: 2,index: '/result',name: '超凡蜘蛛侠'}
				],
				bg: {
					width: '100%',
					backgroundImage: "url("+require("../assets/staticbg.png")+")",
					backgroundSize: '100% 100%',
					backgroundAttachment: 'fixed',
				},
				result: {
					id: 1,'name': '超凡蜘蛛侠', 'rate': '7.3', 'directors': ['马克·韦布'], 'casts': ['安德鲁·加菲尔德', '艾玛·斯通', '瑞斯·伊凡斯', '马丁·辛', '莎莉·菲尔德'], 'comments': {'Adam': '看点总结：加菲的笑，博士的药，警察的无能，蜘蛛侠的跳；艾玛的腿，特效的美，coldplay的音乐，“哥斯拉”的嘴。', '马逢春': '蜥蜴人最后拼死也要救批特！右手救不了换左手！Gwen的老爹死前嫩么含情脉脉的看着批特！天空飘着蓝晒的雪花！这！特！么！都！是！爱！啊！我肃然起敬', '一只阁子': '五星打给本色出演又萌又帅身材好屁股翘的加菲', '可乐': '绝不仅仅是新瓶装旧酒，小清新导演的小心思给蜘蛛侠增加了很多有爱的小细节，整体节奏流畅，尽管预告片里第一人称视角在电影中只是惊鸿一瞥，但3D出色，视效一流。石头姐隐约有Icon气场，最赞的还是加菲，演技出色，一双水汪汪的大眼睛可爱又迷人的苦逼着，身材修长穿着紧身衣还真是美好啊！！', '西西利亚冰百合': '打一星的人都是对男主cll的羡慕嫉妒恨！！！男主角长得帅演得萌，抹杀这个片子一切缺点！~ 全五分撒花~ '},'imgurl': '../../static/image/超凡蜘蛛侠.jpg'
				},
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