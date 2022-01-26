var browserSync = require('browser-sync').create();
var gulp = require('gulp');
var sass = require('gulp-sass')(require('node-sass'));
var sourcemaps = require('gulp-sourcemaps');


const paths = {
    styles: {
        src: './scss/**/*.scss',
        dest: './css'
  }
};

// Compile SCSS
gulp.task('scss', function() {
    return gulp.src([paths.styles.src])
        .pipe(sourcemaps.init())
        .pipe(sass().on('error', sass.logError))
        .pipe(sourcemaps.write('./maps'))
        .pipe(gulp.dest(paths.styles.dest))
        .pipe(browserSync.stream());
});

// Minify CSS
// gulp.task('minify:css', function() {
//     return gulp.src([
//             paths.src.css + '/soft-design-system.css'
//         ])
//         .pipe(cleanCss())
//         .pipe(rename(function(path) {
//             // Updates the object in-place
//             path.extname = ".min.css";
//         }))
//         .pipe(gulp.dest(paths.src.css))
// });

// Default Task: Compile SCSS and minify the result
gulp.task('default', gulp.series('scss'));
