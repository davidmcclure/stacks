

import gulp from 'gulp';

import { $ } from '../config';


gulp.task('sass', () => {

  return gulp.src('./assets/stylesheets/export/index.scss')
    .pipe($.sourcemaps.init())
    .pipe($.sass().on('error', $.sass.logError))
    .pipe($.sourcemaps.write())
    .pipe(gulp.dest('./static/export.css'))

});
