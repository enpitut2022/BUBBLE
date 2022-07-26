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
        const headers = {
          'Content-Type': 'application/json;charset=UTF-8',
          'Access-Control-Allow-Origin': '*',
          }
        this.$axios
          .get("https://bubble-back.herokuapp.com",{params:{textQuery:this.textQuery}, headers: headers})
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