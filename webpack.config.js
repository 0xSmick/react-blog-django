var path = require("path")
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')

module.exports = {
  entry: [
    './assets/src/index.js'
  ],
  output: {
    path: path.resolve('./assets/src/bundles/'),
    filename:"[name]-[hash].js", 
  },

	plugins: [
		new BundleTracker({filename: './webpack-stats.json'}),
	],
  module: {
    loaders: [{
      exclude: /node_modules/,
      loader: 'babel',
      query: {
        presets: ['react', 'es2015', 'stage-1']
      }
    }]
  },
  resolve: {
    extensions: ['', '.js', '.jsx']
  },
  devServer: {
    historyApiFallback: true,
    contentBase: './'
  }
};
