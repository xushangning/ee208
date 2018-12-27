<template>
	<div id="whole">
	    <el-container>
	      <el-header height='61px'>
	        <el-row>
	          <el-col :span="1">
	          	<a href="#"><img :src="imgurl" id="logo"></a>
	          </el-col>
	          <el-col :span="22" :offset="1">
	          	<vmenu></vmenu>
	          </el-col>
	          <el-col :span="2" :offset="20" id="time1"><time1></time1></el-col>
	        </el-row>
	      </el-header>
	      <el-main>
	      	<el-row>
	      		<el-col>
	          		<vform></vform>
	          	</el-col>
	          </el-row>
	        <el-row>
	        	<div class="grid-content">
	        	</div>
	        </el-row>
	        <el-row>
	        	<el-col :span="20" :offset="2">
	        		<carousel></carousel>
	        	</el-col>
	        </el-row>
	      </el-main>
	    </el-container>
	  </div>
</template>

<script>
	import VMenu from './vmenu.vue';
	import Time1 from './time1.vue';
	import VForm from './form.vue'; 
	import Carousel from './carousel.vue';
	export default {
		data () {
			return{
				imgurl:require('../assets/logo.png'),
			}
		},
		components:{
			'vmenu': VMenu,
			'time1': Time1,
			'vform': VForm,
			'carousel': Carousel
		}
	}
</script>

<style>
	.whole {
	    width:100%;
	    height: 100%;
	    bottom:0pX;
	    position: absolute;
	}
	.el-header, .el-footer {
	    background-color: #ffffff;
	    color: #333;
	    text-align: center;
	    line-height: 60px;
	}
	  
	.el-aside {
	    background-color: #D3DCE6;
	    color: #333;
	    text-align: center;
	    line-height: 200px;
	}

	.el-main {
	    color: #333;
	    text-align: center;
	    line-height: 160px;
	}
	  
	body > .el-container {
	    margin-bottom: 40px;
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
	#time1 {
		position:absolute;
		top:0px;
	}
	#logo {
		position:absolute;
		top:6px;
		left: 0px;
		height:50px;
		width:50px;
	}
</style>