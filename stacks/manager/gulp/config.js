

import yargs from 'yargs';
import loadPlugins from 'gulp-load-plugins';


export const $ = loadPlugins();

export const prod = yargs.argv.prod;

export const paths = {
  css: './assets/stylesheets',
  out: './static',
};
