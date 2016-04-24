

import gulp from 'gulp';
import merge from 'merge-stream';

import {$, paths, min} from '../config';


gulp.task('sass', () => {

  const opts = {
    includePaths: 'node_modules',
    outputStyle: min ? 'compressed' : 'nested',
  };

  return merge([
    'home',
  ].map(app => {

    return gulp.src(`${paths.css}/${app}/${app}.scss`)
      .pipe($.if(!min, $.sourcemaps.init()))
      .pipe($.sass(opts).on('error', $.sass.logError))
      .pipe($.if(!min, $.sourcemaps.write()))
      .pipe(gulp.dest(paths.out))
      .pipe($.livereload())

  }));

});
