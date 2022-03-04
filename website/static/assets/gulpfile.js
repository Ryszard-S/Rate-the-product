const browserSync = require('browser-sync').create();
const gulp = require('gulp');
const sass = require('gulp-sass')(require('node-sass'));
const autoprefixer = require('gulp-autoprefixer')
const purgecss = require('gulp-purgecss')
const paths = {
    src_files: './scss/**/*.scss',
    css_files: './scss/**/*.css',
    src: './scss',
    dest: './css',
    html_files: '../../templates/**/*.html'
}

function style() {
    return gulp.src('./scss/**/*.scss')
        .pipe(sass())
.pipe(autoprefixer({overrideBrowserslist: ['last 4 version']}))
        .pipe(gulp.dest('css'))
        .pipe(purgecss({
            content: ['../../templates/**/*.html']
        }))
        .pipe(gulp.dest('purgecss'))

}

gulp.task('purgecss', () => {
    return gulp.src('scss/**/*.css')
        .pipe(purgecss({
            content: ['../../templates/**/*.html']
        }))
        .pipe(gulp.dest('css'))
})

function watch() {
    gulp.watch('./scss/**/*.scss', style);
}


exports.style = style;
exports.watch = watch;
gulp.task('default', watch)
