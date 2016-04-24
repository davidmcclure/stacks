

import gulp from 'gulp';

import {$, paths} from '../config';


gulp.task('watch', () => {
  $.livereload.listen()
  gulp.watch(`${paths.css}/**/*.less`, ['less']);
});
