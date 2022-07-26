<template>
  <div>
    {{/* eslint-disable */}}
    <ul>
      <li v-for="data in datas">{{data.name}}</li>
    </ul>
    <input type='button' value="送信" @click='getData()'>
    <h1>{{sampleHTML}}</h1>
  </div>
</template>

<script>
  export default{
    name: 'WordCloud',
    data(){
      return{
        datas:[{'name': 'サル痘', 'num': 723}, {'name': '感染', 'num': 432},
        {'name': '東京都', 'num':111}],
        textQuery: 'sample',
        sampleHTML: '',
      }
    },
    methods: {
      getData() {
        this.$axios
          .get("http://localhost:3000/api",{params:{textQuery:this.textQuery}})
          .then(
            function (res) {
              console.log("ok")
              console.log(res.data.wordCloud)
              this.sampleHTML = res.data.wordCloud
            }.bind(this)
          ) // Promise処理を行う場合は.bind(this)が必要
          .catch(function (error) {
            // バックエンドからエラーが返却された場合に行う処理について
            console.log(error)
          })
          .finally(function () {})
      },
    },
  }
</script>

<style>

</style>