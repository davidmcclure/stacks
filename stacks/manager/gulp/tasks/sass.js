

import gulp from 'gulp';
import merge from 'merge-stream';

import { $, paths, prod } from '../config';


gulp.task('sass', () => {

  return merge([
    'export',
  ].map(app => {

    return gulp.src(`${paths.css}/${app}/index.scss`)

      .pipe($.sourcemaps.init())
      .pipe($.sass().on('error', $.sass.logError))

      .pipe($.if(prod, $.cleanCss()))
      .pipe($.if(!prod, $.sourcemaps.write()))

      .pipe($.rename(`${app}.css`))
      .pipe(gulp.dest(paths.out));

  }));

});
