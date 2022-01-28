const browserSync = require('browser-sync').create();
const gulp = require('gulp');
const sass = require('gulp-sass')(require('node-sass'));
const autoprefixer = require('gulp-autoprefixer')
const paths = {
    src: './scss/**/*.scss',
    dest: './css'
}

function style() {
    return gulp.src(paths.src)
        .pipe(sass())
        .pipe(autoprefixer({overrideBrowserslist: ['last 4 versions']}))
        .pipe(gulp.dest(paths.dest))
        .pipe(browserSync.stream())
}

function watch() {
    gulp.watch('./scss/**/*.scss', style);
}


exports.style = style;
exports.watch = watch;
gulp.task('default', watch)
