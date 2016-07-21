

import gulp from 'gulp';

import { $, prod } from '../config';


gulp.task('sass', () => {

  return gulp.src('./assets/stylesheets/export/index.scss')

    .pipe($.sourcemaps.init())
    .pipe($.sass().on('error', $.sass.logError))

    .pipe($.if(!prod, $.sourcemaps.write()))
    .pipe($.if(prod, $.cleanCss()))

    .pipe($.rename('export.css'))
    .pipe(gulp.dest('./static'))

});
