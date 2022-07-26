<template>
  <div>
    {{/* eslint-disable */}}
    <ul>
      <li v-for="data in datas">{{data.name}}</li>
    </ul>
  </div>
</template>

<script>
  // const datas = {'サル痘': 723, '感染': 43224, '東京都': 111}
  // const datas = [{'name': 'サル痘', 'num': 723}]
  export default{
    name: 'WordCloud',
    data(){
      return{
        datas:[{'name': 'サル痘', 'num': 723}, {'name': '感染', 'num': 432},
        {'name': '東京都', 'num':111}]
      }
    }
  }
</script>

<style>

</style>