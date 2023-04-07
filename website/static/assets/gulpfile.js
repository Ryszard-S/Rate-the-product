const browserSync = require('browser-sync').create();
const gulp = require('gulp');
const sass = require('gulp-sass')(require('node-sass'));
const autoprefixer = require('gulp-autoprefixer')
const purgecss = require('gulp-purgecss')
const paths = {
    scss_files: './scss/**/*.scss',
    css_files: './css/**/*.css',
    src: './scss',
    dest: './css',
    html_files: '../../templates/**/*.html'
}

function style() {
    return gulp.src(paths.scss_files)
        .pipe(sass())
        .pipe(autoprefixer({overrideBrowserslist: ['last 4 version']}))
        // .pipe(gulp.dest('css'))
        .pipe(purgecss({
            content: [paths.html_files]
        }))
        .pipe(gulp.dest('purgecss'))

}

function watch() {
    gulp.watch([paths.scss_files, paths.html_files], style);
}


exports.style = style;
exports.watch = watch;
gulp.task('default', watch)
