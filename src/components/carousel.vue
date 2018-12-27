<template>
	<div>
	    <el-carousel type="card" trigger="click" height="400px">
	      <el-carousel-item 
	      v-for="item in items" 
	      :key="item.id">
	        <h3>{{ item.file }}</h3>
	      </el-carousel-item>
	    </el-carousel>
	</div>
</template>

<script>
	export default {
		name:"Carousel",
		data (){
			return {
				items:[
				{id:0,file:'海王'},
				{id:1,file:'蜘蛛侠'},
				{id:2,file:'蝙蝠侠'}
				]
			}
		}
	}
</script>

<style>
	.el-carousel__item h3 {
	    color: #475669;
	    font-size: 14px;
	    opacity: 0.75;
	    line-height: 150px;
	    margin: 0;
	}

	.el-carousel__item:nth-child(2n) {
	    background-color: #99a9bf;
	}
	  
	.el-carousel__item:nth-child(2n+1) {
	    background-color: #d3dce6;
	}
</style>