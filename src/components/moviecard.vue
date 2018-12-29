<template>
	<div class="card">
		<el-card :body-style="{padding: '0px'}">
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
					<el-col :span="3"><strong>导演 </strong></el-col>
					<el-col :span="21">
						<el-tag type="info" v-for="dr in movie.directors">{{dr}}</el-tag>
					</el-col>
				</el-row>
				<el-row>
					<el-col :span="3"><strong>演员 </strong></el-col>
					<el-col :span="21">
						<el-tag type="info" v-for="ca in movie.casts">{{ca}}</el-tag>
					</el-col>
				</el-row>
			</div>
		</el-card>
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
		computed: {
			parse() {
				var s = this.movie.rate;
				return parseFloat(s);
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
	}
	.el-card {
		border: 0px;
		background-color: rgba(50,50,50,0.4);
		color:#9b9b9b;
		margin-bottom: 10px;
	}
	.el-card__body {
		width: 90%;
		height: 96%;
		margin-top: 2%;
		margin-left: auto;
		margin-right: auto;
	}
</style>