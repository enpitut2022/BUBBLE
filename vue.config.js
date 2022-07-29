const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  assetsDir: 'static',
  devServer: {
  port: 8080,
  host: '127.0.0.1'
}
})
