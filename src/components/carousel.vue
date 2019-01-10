<template>
	<div>
	    <el-carousel type="card" trigger="click" height="400px">
	      <el-carousel-item
	      v-for="movie in movies" 
	      :key="movie.id">
	      <el-col :offset="6">
	      	<a :href="'result?'+movie.name">
	      		<img :src="movie.img">
	      	</a>
	      </el-col>
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
	.el-carousel__item:nth-child(2n) {
		color: rgba(0,0,0,0);
	}
	.el-carousel__item:nth-child(2n+1) {
		color: rgba(0,0,0,0);
	}
	.el-carousel__mask {
  		background-color: rgba(0,0,0,0);
	}
	.image {
		padding-left: auto;
		padding-right: auto;
	}
</style>