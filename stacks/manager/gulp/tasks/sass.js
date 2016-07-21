

import gulp from 'gulp';

import { $, min } from '../config';


gulp.task('sass', () => {

  return gulp.src('./assets/stylesheets/export/index.scss')

    .pipe($.if(!min, $.sourcemaps.init()))
    .pipe($.sass().on('error', $.sass.logError))
    .pipe($.if(!min, $.sourcemaps.write()))

    .pipe($.rename('export.css'))
    .pipe(gulp.dest('./static'))

});
