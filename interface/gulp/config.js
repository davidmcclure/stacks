

import yargs from 'yargs';
import loadPlugins from 'gulp-load-plugins';


export const $ = loadPlugins();

export const min = yargs.argv.min;

export const paths = {
  css:  './assets/stylesheets',
  js:   './assets/javascripts',
  out:  './static/interface',
};
