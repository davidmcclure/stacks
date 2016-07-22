

import gulp from 'gulp';
import merge from 'merge-stream';

import { $, paths, prod } from '../config';


gulp.task('sass', () => {

  const opts = {
    includePaths: 'node_modules',
  };

  return merge([
    'export',
  ].map(app => {

    return gulp.src(`${paths.css}/${app}/index.scss`)

      .pipe($.sourcemaps.init())
      .pipe($.sass(opts).on('error', $.sass.logError))

      .pipe($.if(prod, $.cleanCss()))
      .pipe($.if(!prod, $.sourcemaps.write()))

      .pipe($.rename(`${app}.css`))
      .pipe(gulp.dest(paths.out))
      .pipe($.livereload());

  }));

});
