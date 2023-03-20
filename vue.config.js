const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy: { // proxyTable 설정
      '/search': {
        "target":'https://search.naver.com/',
        "pathRewrite":{'^/':''},
        "changeOrigin":true,
        "secure":false
      },
      '/entertainment': {
        "target":'https://www.yna.co.kr/',
        "pathRewrite":{'^/':''},
        "changeOrigin":true,
        "secure":false
      },
    }
  }
})