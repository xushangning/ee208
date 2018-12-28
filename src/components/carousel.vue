<template>
	<div>
	    <el-carousel type="card" trigger="click" height="400px">
	      <el-carousel-item
	      v-for="movie in movies" 
	      :key="movie.id">
	        <img :src="movie.img">
	      </el-carousel-item>
	    </el-carousel>
	</div>
</template>

<script>
	export default {
		name:"Carousel",
		props: {
			movies:{
				type: Array,
				required: true
			}
		}
	}
</script>

<style>
	.el-carousel__item h3 {
	    color: rgba(0,0,0,0);
	    font-size: 14px;
	    opacity: 0;
	    line-height: 150px;
	    margin: 0;
	}
  .el-carousel__item:nth-child(2n) {
    color: rgba(0,0,0,0);
  }
  
  .el-carousel__item:nth-child(2n+1) {
    color: rgba(0,0,0,0);
  }
  .el-carousel__mask, .el-cascader-menu, .el-cascader-menu__item.is-disabled:hover, .el-collapse-item__header, .el-collapse-item__wrap {
  	background-color: rgba(0,0,0,0);
  }
</style>