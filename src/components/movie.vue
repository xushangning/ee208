<template>
	<div class="card">
		<el-card :body-style="{padding: '0px'}">
			<el-row>
				<img :src="movie.imgurl" class="image">
				<div class="right">
					<h3>{{movie.name}}</h3>
					<el-row style="margin-bottom: 20px">
						<el-col :span="2"><strong>评分 </strong></el-col>
						<el-col :span="22">
							<el-rate
								v-model="parse"
								disabled
								show-score
								text-color="#ff9900"
								score-template="{value}"
								:max=10>
							</el-rate>
						</el-col>
					</el-row>
					<el-row>
						<el-col :span="2"><strong>导演 </strong></el-col>
						<el-col :span="22">
							<el-tag type="info" v-for="dr in movie.directors">{{dr}}</el-tag>
						</el-col>
					</el-row>
					<el-row>
						<el-col :span="2"><strong>主演 </strong></el-col>
						<el-col :span="22">
							<el-tag type="info" v-for="ca in movie.casts">{{ca}}</el-tag>
						</el-col>
					</el-row>
				</div>
			</el-row>
				<span>演职员表：</span>
				<el-row>
				  <el-col :span="4" v-for="dr in movie.directors">
				    <el-card :body-style="{ padding: '0px' }">
				    	<img :src="'../../static/image/' + dr + '.jpg'"
				    		class="image">
				    	<span class="sp">{{dr}}<br/><em>导演</em></span>
				    </el-card>
				  </el-col>
				  <el-col :span="4" v-for="ca in movie.casts">
				    <el-card :body-style="{ padding: '0px' }">
				    	<img :src="'../../static/image/' + ca + '.jpg'"
				    		class="image">
				    	<span class="sp">{{ca}}<br/><em>主演</em></span>
				    </el-card>
				  </el-col>
				</el-row>
				<el-row>
					<span>预告片：</span>
					<div class="video">
						<video :src="'../../static/video/' + movie.name + '.mp4'"
								v-on:canplay.once="changetime"
								height="400px"
								width="800px" 
								controls
								id="video1"></video>
					</div>
				</el-row>
				<el-row>
					<el-badge :value='5' class="item">
						<el-button type="info" @click="change">评论</el-button>
					</el-badge>
	  			    <el-row v-for="value,key in movie.comments" v-if="show" class='cm'>
	  			    	<transition name="el-zoom-in-top">	
	  			    		<el-card class="box-card">
								<div slot="header" class="clearfix">
									<span>{{key}}</span>
								</div>
								{{value}}
							</el-card>
				    	</transition>
				    </el-row>
				</el-row>	
		</el-card>
		<div class="grid" v-if="!show"></div>
	</div>
</template>

<script>
	export default {
		props: {
			movie: {
				type: Object,
				required: true
			}
		},
		data() {
			return {
				show:true
			}
		},
		computed: {
			parse() {
				var s = this.movie.rate;
				return parseFloat(s);
			}
		},
		methods: {
			change() {
				this.show = !this.show;
			},
			changetime() {
				var myvid = document.getElementById('video1');
	    		if (this.movie.name==='疯狂动物城')
	    		{
	    			myvid.currentTime=40;
	    		}
			}
		}
	}
</script>

<style>
	.sp {
		text-align: center;
		float: left;
		width: 100%;
	}
	.video {
		margin-left: 3%;
		width: 800px;
		height: 400px;
	}
	.image {
		width: 135px;
		height: 200px;
		float: left;
	}
	.right {
		float: left;
		margin-left: 10px;
		width:70%;
	}
	.el-card {
		border: 0px;
		background-color: rgba(37,37,37,0.7);
		color:#bbbbbb;
		margin-bottom: 10px;
		width:80%;
		margin-right: auto;
		margin-left: auto;
	}
	.el-card__body {
		margin-top: 2%;
		margin-left: 2%;
		margin-right: 2%;
	}
	.el-tag {
		padding: 0 5px;
	}
	.el-tag--info {
		color:#e7e7e7;
	}
	.cm {
		margin-top: 2%;
		margin-right: 2%;
	}
	.grid {
		height:367px;
	}
</style>