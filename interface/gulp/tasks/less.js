

import gulp from 'gulp';
import merge from 'merge-stream';

import {$, paths, min} from '../config';


gulp.task('less', () => {

  const opts = {
    paths: 'node_modules',
    compress: min,
  };

  return merge([
    'home',
  ].map(app => {

    return gulp.src(`${paths.css}/${app}/${app}.less`)

      .pipe($.if(!min, $.sourcemaps.init()))

      .pipe($.less(opts).on('error', function(err) {
        console.log(err);
        this.end()
      }))

      .pipe($.if(!min, $.sourcemaps.write()))
      .pipe(gulp.dest(paths.out))
      .pipe($.livereload())

  }));

});
