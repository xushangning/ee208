<template>
	<div class="card">
		<el-card :body-style="{padding: '0px'}">
			<el-row>
				<img :src="movie.imgurl" class="image">
				<div class="right">
					<h3>{{movie.name}}</h3>
					<el-rate
						v-model="parse"
						disabled
						show-score
						text-color="#ff9900"
						score-template="{value}"
						:max=10>
					</el-rate>
					</br>
					<el-row>
						<el-col :span="2"><strong>导演 </strong></el-col>
						<el-col :span="22">
							<el-tag type="info" v-for="dr in movie.directors">{{dr}}</el-tag>
						</el-col>
					</el-row>
					<el-row>
						<el-col :span="2"><strong>演员 </strong></el-col>
						<el-col :span="22">
							<el-tag type="info" v-for="ca in movie.casts">{{ca}}</el-tag>
						</el-col>
					</el-row>
				</div>
			</el-row>
			<div class="down">
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
			</div>
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
			}
		}
	}
</script>

<style>
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
	}
	.el-card__body {
		margin-top: 2%;
		margin-left: 2%;
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